import json
from flask.cli import with_appcontext
from .models import Forecast, CityWeather
import click

@click.command('load_data')
@with_appcontext
def load_mock_data_command():
    from app import db

    with open("weather.json") as fop:
        json_data = json.load(fop)


    for city_data in json_data:
        # Create city weather
        city_weather = CityWeather(city=city_data["city"])
        db.session.add(city_weather)

        # since we need the id and it wont be available before we commit.
        db.session.flush()

        # Create forecast objects for city
        for fore_cast in city_data["forecast"]:
            forecast = Forecast(
                date=fore_cast["date"],
                temperature=fore_cast["temperature"],
                humidity=fore_cast["humidity"],
                condition=fore_cast["condition"],
                wind_speed=fore_cast["wind_speed"],
                city_id=city_weather.id,
            )
            db.session.add(forecast)
    
    db.session.commit()
    click.echo("Mock data loaded successfully!")
    

@click.command("purge-data")
@with_appcontext
def purge_db():
    """Deletes all data from the database."""
    from app import db

    db.session.query(Forecast).delete()  # Delete Forecast records first (due to FK constraint)
    db.session.query(CityWeather).delete()  # Then delete CityWeather records
    db.session.commit()
    click.echo("Database purged successfully.")
