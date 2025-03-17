from flask import Blueprint
from flask_restful import Api
from app.apis.weather_api import (
    CityWeather,
    CityWeatherFromDatabaseListAPI,
    CityWeatherWithMockDataListAPI,
)

weather_bp = Blueprint("weather", __name__)
weather_api = Api(weather_bp)

weather_api.add_resource(
    CityWeatherWithMockDataListAPI,
    "/cityweather/mocked/<string:city>",
    "/cityweather/mocked/<string:city>/<string:date>",
)
weather_api.add_resource(
    CityWeatherFromDatabaseListAPI,
    "/cityweather/db/<string:city>",
    "/cityweather/db/<string:city>/<string:date>",
    )