# Refer: https://flask.palletsprojects.com/en/stable/testing/

import random
import pytest
from datetime import datetime as dt
from datetime import timedelta as td
from config import TestingConfig
from app import create_app, db
from app.models import CityWeather, Forecast


@pytest.fixture
def app():
    app = create_app(config_name="testing")
    app.config.from_object(TestingConfig)
    with app.app_context():
        # This part is setUp
        # print registered routes to check routes
        # print ("All my routes")
        # for rule in app.url_map.iter_rules():
        #     print(rule)

        # db setup
        db.create_all()
        yield app
        # This part is teardown
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def add_test_data(app):
    """Create test data for GET apis"""
    condition_list = ["Sunny", "Cloudy", "Windy", "Cold", "Rainy"]

    # Create a city weather object
    with app.app_context():
        cw = CityWeather(city="Vienna")
        db.session.add(cw)
        db.session.commit()
        created_cw = db.session.query(CityWeather).filter_by(city="Vienna").first()
        city_name = created_cw.city

        list_forecast = []
        for i in range(7):
            f = Forecast(
                date=(dt.today() + td(days=i)).strftime("%Y-%m-%d"),
                temperature=f"{random.randint(10, 40)}C",
                humidity=f"{random.randint(0, 100)}%",
                condition=random.choice(condition_list),
                wind_speed=f"{random.randint(5, 25)} km/h",
                city_id=created_cw.id,
            )
            list_forecast.append(f)
    
        db.session.add_all(list_forecast)
        db.session.commit()

        # Ensure session is flushed
        db.session.expire_all()
    return city_name

