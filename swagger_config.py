swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "City Weather API",
        "description": "API for managing city weather data",
        "version": "1.0.0"
    },
    "definitions": {
        "CityWeather": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                    "example": 1
                },
                "city": {
                    "type": "string",
                    "example": "Vienna"
                }
            }
        },
        "Forecast": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                    "example": 1
                },
                "date": {
                    "type": "string",
                    "example": "2025-03-19"
                },
                "temperature": {
                    "type": "string",
                    "example": "25°C"
                },
                "humidity": {
                    "type": "string",
                    "example": "60%"
                },
                "condition": {
                    "type": "string",
                    "example": "Sunny"
                },
                "wind_speed": {
                    "type": "string",
                    "example": "10 km/h"
                },
                "city_id": {
                    "type": "integer",
                    "example": 1
                }
            }
        }
    }
}
