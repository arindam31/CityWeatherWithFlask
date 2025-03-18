from flask import Blueprint
from flask_restful import Api
from app.apis.weather_api import (
    CityWeatherFromDatabaseListAPI,
    CityWeatherWithMockDataListAPI,
    CityWeatherDetailsFromDatabase,
)
from app.apis.open_weather_api import (
    CityWeatherFromWeatherService,
    CityWeatherFromWeatherServiceOrDb,
)

weather_bp = Blueprint("weather", __name__)
live_weather_bp = Blueprint("weather_live", __name__)
weather_api = Api(weather_bp)
live_weather_api = Api(live_weather_bp)

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

weather_api.add_resource(
    CityWeatherDetailsFromDatabase,
    "/cityweather/db/<int:id>",
)

live_weather_api.add_resource(
    CityWeatherFromWeatherService,
    "/weather/live/<string:city>",
)

live_weather_api.add_resource(
    CityWeatherFromWeatherServiceOrDb,
    "/weather/today/<string:city>",
)
