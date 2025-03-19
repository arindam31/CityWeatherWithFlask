import requests
from app import db
from datetime import datetime
from app.models import CityWeather, Forecast
from flask_restful import Resource
from flask import jsonify


class CityWeatherFromWeatherService(Resource):
    """This API serves data from a weather service (openweathermap.org)

    - The limitations are 60 request per minute.
    - The response is only for current day. Past and future data is only for Paid customers.
    - The data recieved from this API is NOT saved in database
    """

    def get(self, city):
        """Example endpoint returning a single forecast for TODAY from a weather service ONLY.
        This does not save the received info in the database.
    ---
    parameters:
      - name: city
        in: path
        type: string
        required: true
        description: The city name to get the forecast for
    
    responses:
      200:
        description: A forecast for the given city
        schema:
          $ref: '#/definitions/Forecast'
        examples:
          application/json:
            {
              "condition": "Haze",
              "humidity": "78%",
              "temperature": "27.96°C",
              "wind_speed": "5.14 km/h"
            }
"""
        API_KEY = "83b03dc17f497f2c21275f9287b4ac86"

        location_url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
        loc_api_response = requests.get(location_url)

        if loc_api_response.status_code != 200:
            return jsonify({"error": "Failed to fetch location data"}), 500
        loc_data = loc_api_response.json()

        if not loc_data:
            return jsonify({"error": "City not found"}), 404

        # Finally collect the lat and lon
        lat, lon = loc_data[0]["lat"], loc_data[0]["lon"]

        # Get weather data using above lat & lon
        weather_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
        weather_api_response = requests.get(weather_URL)

        if weather_api_response.status_code != 200:
            return jsonify({"error": "Failed to fetch weather data"}), 500
        weather_data = weather_api_response.json()

        return jsonify(
            {
                "condition": weather_data["weather"][0]["main"],
                "temperature": weather_data["main"]["temp"],
                "humidity": weather_data["main"]["humidity"],
                "wind_speed": weather_data["wind"]["speed"],
            }
        )


class CityWeatherFromWeatherServiceOrDb(Resource):
    """This API serves data from EITHER database or weather API

    - We check if data is already available in database
    - If yes, return from db.
    - Or else, get data from external service and write it in db.
    """

    def get(self, city):
        """Example endpoint returning a single forecast for TODAY from database or weather service
    ---
    parameters:
      - name: city
        in: path
        type: string
        required: true
        description: The city name to get the forecast for
    
    responses:
      200:
        description: A forecast for the given city
        schema:
          $ref: '#/definitions/Forecast'
        examples:
          application/json:
            {
              "condition": "Haze",
              "humidity": "78%",
              "temperature": "27.96°C",
              "wind_speed": "5.14 km/h"
            }
"""
        
        API_KEY = "83b03dc17f497f2c21275f9287b4ac86"

        today = datetime.today().strftime("%Y-%m-%d")

        # Check if we already have today's forecast in DB
        city_weather = CityWeather.query.filter_by(city=city).first()
        if city_weather:
            forecast = Forecast.query.filter_by(
                city_id=city_weather.id, date=today
            ).first()
            if forecast:
                return jsonify(
                    {
                        "condition": forecast.condition,
                        "temperature": forecast.temperature,
                        "humidity": forecast.humidity,
                        "wind_speed": forecast.wind_speed,
                    }
                )

        # Fetch lat/lon from OpenWeatherMap
        location_url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
        loc_api_response = requests.get(location_url)

        if loc_api_response.status_code != 200:
            return jsonify({"error": "Failed to fetch location data"}), 500

        loc_data = loc_api_response.json()
        if not loc_data:
            return jsonify({"error": "City not found"}), 404

        lat, lon = loc_data[0]["lat"], loc_data[0]["lon"]

        # Fetch weather data
        weather_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        weather_api_response = requests.get(weather_URL)

        if weather_api_response.status_code != 200:
            return jsonify({"error": "Failed to fetch weather data"}), 500

        weather_data = weather_api_response.json()

        # Save to DB
        if not city_weather:
            city_weather = CityWeather(city=city)
            db.session.add(city_weather)
            db.session.commit()

            db.session.flush()  # To ensure city_weather.id is available

        forecast = Forecast(
            date=today,
            temperature=f"{weather_data['main']['temp']}°C",
            humidity=f"{weather_data['main']['humidity']}%",
            condition=weather_data["weather"][0]["main"],
            wind_speed=f"{weather_data['wind']['speed']} km/h",
            city_id=city_weather.id,
        )

        db.session.add(forecast)
        db.session.commit()

        return jsonify(
            {
                "condition": forecast.condition,
                "temperature": forecast.temperature,
                "humidity": forecast.humidity,
                "wind_speed": forecast.wind_speed,
            }
        )
