# tests for weather api
import random
from datetime import datetime as dt
from datetime import timedelta as td


def test_get_valid_city_and_date(client, add_test_data):
    """Test fetching weather for a valid city from database using API."""

    url = f"/api/cityweather/db/{add_test_data}/{(dt.today() + td(days=random.randint(0,7))).strftime("%Y-%m-%d")}"
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.json.keys()) == [
        "condition",
        "date",
        "humidity",
        "id",
        "temperature",
        "wind_speed",
    ]

def test_get_invalid_city(client, add_test_data):
    """Test fetching weather for a INvalid city using API."""

    url = f"/api/cityweather/db/DOESNOTEXIST/2025-03-18"
    response = client.get(url)
    assert response.status_code == 404
    assert response.json ==  {'message': 'Invalid city'}