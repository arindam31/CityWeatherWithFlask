from app import app, mock_data


@app.route("/forecast/<city>/")
@app.route("/forecast/<city>/<date>")
def get_city_forecast(city, date:str=None):

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

