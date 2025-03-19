from app import mock_data, db
from app.models import CityWeather, Forecast
from flask_restful import Resource
from flask import jsonify, request, make_response


class CityWeatherWithMockDataListAPI(Resource):
    def get(self, city: str, date: str = None):
        """This API gets data from a JSON file present physically in the project directory.
        ---
        parameters:
          - name: city
            in: path
            type: string
            required: true
            description: The city name to filter forecasts
          - name: date
            in: path
            type: string
            required: false
            description: "Optional. Date to filter forecasts (Format: YYYY-MM-DD)"
        
        definitions:
          Forecast:
            type: object
            properties:
              condition:
                type: string
                example: "Haze"
              humidity:
                type: string
                example: "78%"
              temperature:
                type: string
                example: "27.96°C"
              wind_speed:
                type: string
                example: "5.14 km/h"
        
        responses:
          200:
            description: A list of forecasts for the given city and optional date
            schema:
              type: array
              items:
                $ref: '#/definitions/Forecast'
            examples:
              application/json:
                [
                  {
                    "condition": "Haze",
                    "humidity": "78%",
                    "temperature": "27.96°C",
                    "wind_speed": "5.14 km/h"
                  },
                  {
                    "condition": "Cloudy",
                    "humidity": "82%",
                    "temperature": "25.4°C",
                    "wind_speed": "3.2 km/h"
                  }
                ]
        """
        # Need to do this check for swagger issue.
        if date == 'undefined':
            date = None

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
    Or later mode data might be added using live apis.
    To begin with, the data was loaded with custom commands into db from same weather.json file.
    Note: User command : `flask load_data` to load data before trying this API. This has been already executed 
    if docker was used to start the project.
    """
    def get(self, city, date=None):
        """This API gets all data from the database.
        ---
        parameters:
          - name: city
            in: path
            type: string
            required: true
            description: The city name to filter forecasts
          - name: date
            in: path
            type: string
            required: false
            description: "Optional. Date to filter forecasts (Format: YYYY-MM-DD)"
        
        definitions:
          Forecast:
            type: object
            properties:
              condition:
                type: string
                example: "Haze"
              humidity:
                type: string
                example: "78%"
              temperature:
                type: string
                example: "27.96°C"
              wind_speed:
                type: string
                example: "5.14 km/h"
        
        responses:
          200:
            description: A list of forecasts for the given city and optional date
            schema:
              type: array
              items:
                $ref: '#/definitions/Forecast'
            examples:
              application/json:
                [
                  {
                    "condition": "Haze",
                    "humidity": "78%",
                    "temperature": "27.96°C",
                    "wind_speed": "5.14 km/h"
                  },
                  {
                    "condition": "Cloudy",
                    "humidity": "82%",
                    "temperature": "25.4°C",
                    "wind_speed": "3.2 km/h"
                  }
                ]
        """
        if date == 'undefined':
            date = None

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
        forecasts = Forecast.query.filter_by(city_id=city_weather.id).order_by(Forecast.id.desc()).limit(7).all()
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
        """
    Creates a new city weather entry.

    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - city
          properties:
            city:
              type: string
              example: "Vienna"
              description: The name of the city to create a weather record for.

    responses:
      201:
        description: City weather entry successfully created.
        schema:
          $ref: '#/definitions/CityWeather'
      400:
        description: Invalid input.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Invalid request payload"
        """
        data = request.get_json()
        city_weather = CityWeather(city=data["city"])
        db.session.add(city_weather)
        db.session.commit()
        return make_response(city_weather.to_dict(), 201)
    

class CityWeatherDetailsFromDatabase(Resource):
    """
    API for managing city weather details from the database.
    
    This class provides endpoints for:
    - Retrieving weather details for a specific city by ID (`GET`).
    - Updating city weather details by ID (`PATCH`).
    - Deleting city weather records by ID (`DELETE`).
    """
    
    def get(self, id):
        """
        Retrieves weather details for a specific city by its ID.

        ---
        parameters:
          - name: id
            in: path
            type: integer
            required: true
            description: The ID of the city weather record to retrieve.
        
        responses:
          200:
            description: Successfully retrieved the city weather details.
            schema:
              $ref: '#/definitions/CityWeather'
          404:
            description: City not found.
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Invalid city"
        """        
        city_weather = CityWeather.query.filter_by(id=id).first()
        if not city_weather:
            return {"message": "Invalid city"}, 404
        return city_weather.to_dict(), 200
        
    def patch(self, id):
        """
        Updates the weather details for a specific city by its ID.

        ---
        parameters:
          - name: id
            in: path
            type: integer
            required: true
            description: The ID of the city weather record to update.
          - name: city_weather
            in: body
            required: true
            description: A JSON object containing the city weather fields to update.
            schema:
              type: object
              properties:
                city:
                  type: string
                  example: "Vienna"

        responses:
          202:
            description: Successfully updated the city weather details.
            schema:
              $ref: '#/definitions/CityWeather'
          400:
            description: Bad request if invalid data is provided.
        """
        data = request.get_json()
        city_weather = CityWeather.query.filter_by(id=id).first()

        for attr in data:
            setattr(city_weather, attr, data[attr])

        db.session.add(city_weather)
        db.session.commit()
        return city_weather.to_dict(), 202
    
    def delete(self, id):
        """
        Deletes a specific city weather record by its ID.

        ---
        parameters:
          - name: id
            in: path
            type: integer
            required: true
            description: The ID of the city weather record to delete.

        responses:
          204:
            description: Successfully deleted the city weather record.
          404:
            description: City not found.
        """
        city_weather = CityWeather.query.filter_by(id=id).first()
        db.session.delete(city_weather)
        db.session.commit()
        return make_response('', 204)

