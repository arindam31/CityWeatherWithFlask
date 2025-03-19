import json
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config, TestingConfig


db = SQLAlchemy()
migrate = Migrate()


def load_mock_data(filename):
    """Function to read data from json file."""
    with open(filename) as fop:
        json_data = json.load(fop)
    return json_data

# Loading mock data
mock_data = load_mock_data("weather.json")


def create_app(config_name="default"):
    app = Flask(__name__)

    CORS(app, origins=["http://localhost:5173"])

    if config_name == "testing":
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Blueprints registration.
    from app.blueprints import weather_bp, live_weather_bp
    app.register_blueprint(weather_bp, url_prefix="/api")
    app.register_blueprint(live_weather_bp, url_prefix="/api")
    return app


app = create_app()

from app import routes, models
from app.commands import load_mock_data_command, purge_db, create_db_file

# Command registration
app.cli.add_command(name="load-data", cmd=load_mock_data_command)
app.cli.add_command(name="purge-data", cmd=purge_db)
app.cli.add_command(name="create-db", cmd=create_db_file)
