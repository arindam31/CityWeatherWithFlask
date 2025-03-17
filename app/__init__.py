import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from config import Config


db = SQLAlchemy()
migrate = Migrate()


def load_mock_data(filename):
    with open(filename) as fop:
        json_data = json.load(fop)
    return json_data


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)

    return app


app = create_app()
mock_data = load_mock_data("weather.json")

from app import routes, models
from app.apis import weather
from app.commands import load_mock_data_command, purge_db

weather_api = Api(app)
weather_api.add_resource(
    weather.CityWeatherWithMockDataListAPI,
    "/cityweather/mocked/<string:city>",
    "/cityweather/mocked/<string:city>/<string:date>",
)
weather_api.add_resource(
    weather.CityWeatherFromDatabaseListAPI,
    "/cityweather/db/<string:city>",
    "/cityweather/db/<string:city>/<string:date>",
    )

# Command registration
app.cli.add_command(name="load_data", cmd=load_mock_data_command)
app.cli.add_command(name="purge_data", cmd=purge_db)
