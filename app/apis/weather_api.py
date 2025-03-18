from app import mock_data, db
from app.models import CityWeather, Forecast
from flask_restful import Resource
from flask import jsonify, request, make_response


class CityWeatherWithMockDataListAPI(Resource):
    """This api gets data from a json file present physically in the project directory.
    Purpose: Demo
    """
    def get(self, city, date=None):
        for item in mock_data:
            if "city" in item.keys() and item["city"] == city:
                if date:
                    for forecast in item["forecast"]:
                        if forecast["date"] == date:
                            return forecast
                else:
                    forecast = item["forecast"]
                    return forecast                  
                break
            else:
                return {"message": "Invalid city"}, 404
        return {"message": "City not found"}, 404
    

class CityWeatherFromDatabaseListAPI(Resource):
    """This api gets data from database after mock data was loaded into database.
    The data was loaded with custom commands into db from same weather.json file.
    Note: User command : `flask load_data` to load data before trying this API.
    """
    def get(self, city, date=None):
        city_weather = CityWeather.query.filter_by(city=city).first()
        if not city_weather:
            return {"message": "Invalid city"}, 404

        if date:
            forecast = Forecast.query.filter_by(city_id=city_weather.id, date=date).first()
            if forecast:
                return jsonify({
                    "id": forecast.id,
                    "date": forecast.date,
                    "temperature": forecast.temperature,
                    "humidity": forecast.humidity,
                    "condition": forecast.condition,
                    "wind_speed": forecast.wind_speed,
                })
            return {"message": f"No forecast data found for {city} and date: {date}"}, 404

        # Get all forecasts for the city
        forecasts = Forecast.query.filter_by(city_id=city_weather.id).all()
        return jsonify([
            {
                "id": f.id,
                "date": f.date,
                "temperature": f.temperature,
                "humidity": f.humidity,
                "condition": f.condition,
                "wind_speed": f.wind_speed,
            }
            for f in forecasts
        ])

    def post(self):
        data = request.get_json()
        city_weather = CityWeather(city=data["city"])
        db.session.add(city_weather)
        db.session.commit()
        return make_response(city_weather.to_dict(), 201)
    

class CityWeatherDetailsFromDatabase(Resource):
    def get(self, id):
        city_weather = CityWeather.query.filter_by(id=id).first()
        if not city_weather:
            return {"message": "Invalid city"}, 404
        return city_weather.to_dict(), 200
        
    def patch(self, id):
        data = request.get_json()
        city_weather = CityWeather.query.filter_by(id=id).first()

        for attr in data:
            setattr(city_weather, attr, data[attr])

        db.session.add(city_weather)
        db.session.commit()
        return city_weather.to_dict(), 202
    
    def delete(self, id):
        city_weather = CityWeather.query.filter_by(id=id).first()
        db.session.delete(city_weather)
        db.session.commit()
        return make_response('', 204)

