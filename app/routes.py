from app import app, mock_data


@app.route("/forecast/<city>/")
@app.route("/forecast/<city>/<date>")
def get_city_forecast(city, date: str = None):
    """Example endpoint returning a list of forecasts from mock data loaded from weather.json file.
    ---
    parameters:
      - name: city
        in: path
        type: string
        required: true
        description: The city name to filter forecasts
      - name: date
        in: path
        type: string
        required: false
        description: "Optional. The specific date to filter forecasts (Format: YYYY-MM-DD)"
    responses:
      200:
        description: A list of forecasts for the given city and optional date
    """
    if date == 'undefined':
        date = None

    for item in mock_data:
        if "city" in item.keys() and item["city"] == city:
            if date:
                for forecast in item["forecast"]:
                    if forecast["date"] == date:
                        return forecast
            else:
                return item["forecast"]
            break
        else:
            return "Invalid city"

