# Flask Template project
- User auth with JWT
- Online API document with Swagger
- Connexions usage
- Logging
- Permissions

# QUICK Start
- create a .env file at root. Add variables as shown below.
- On shell, use: flask run
- Visit url: 127:0.0.1:5000

# ENV file contents
Add these in the .env file:
```
FLASK_APP=app
FLASK_ENV=development
```


# Running the project
- With flask command directly:
 ```bash
 flask run
 ```

- Start the docker container
 ```bash
 docker compose up --build
 ```

# Command execution with docker.
- To execute commands inside the container:
 ```bash
docker exec -ti flask_app_container bash
 ```

 # To see flask routes
 ```bash
docker exec -it flask_app_container flask routes

Endpoint                                Methods    Rule
-------------------------------------  ---------  ---------------------------------
get_city_forecast                       GET        /forecast/<city>/<date>
get_city_forecast                       GET        /forecast/<city>/
static                                  GET        /static/<path:filename>
weather.cityweatherfromdatabaselistapi  GET, POST  /api/cityweather/db/<string:city>/<string:date>
weather.cityweatherfromdatabaselistapi  GET, POST  /api/cityweather/db/<string:city>
weather.cityweatherwithmockdatalistapi  GET        /api/cityweather/mocked/<string:city>/<string:date>
weather.cityweatherwithmockdatalistapi  GET        /api/cityweather/mocked/<string:city>
 ```