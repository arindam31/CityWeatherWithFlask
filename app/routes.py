from app import app

@app.route("/forecast/<city>")
def get_city_forecast(city):
    # Find the city in the data
    city_data = "bala"
    return city_data