import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


db = SQLAlchemy()
migrate = Migrate()


def load_mock_data(filename):
    """Function to read data from json file."""
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

# Loading mock data
mock_data = load_mock_data("weather.json")

from app import routes, models
from app.commands import load_mock_data_command, purge_db
from app.blueprints import weather_bp

# Blueprints registration.
app.register_blueprint(weather_bp, url_prefix="/api")

# Command registration
app.cli.add_command(name="load_data", cmd=load_mock_data_command)
app.cli.add_command(name="purge_data", cmd=purge_db)
