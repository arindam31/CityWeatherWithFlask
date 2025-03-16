from flask_restful import Resource
from app import mock_data

class CityWeatherAPI(Resource):
    def get(self, city, date=None):  # date is optional, defaults to None
        for item in mock_data:
            if "city" in item.keys() and item["city"] == city:
                if date:
                    for forecast in item["forecast"]:
                        if forecast["date"] == date:
                            return forecast
                else:
                    forecast = item["forecast"]
                    return [bytes(d["temperature"], "utf-8") for d in forecast]                    
                break
            else:
                return {"message": "Invalid city"}, 404
        return {"message": "City not found"}, 404
