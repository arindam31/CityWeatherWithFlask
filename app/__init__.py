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
weather_api = Api(app)
weather_api.add_resource(weather.CityWeatherAPI, "/cityweather/<string:city>",  "/cityweather/<string:city>/<string:date>")
