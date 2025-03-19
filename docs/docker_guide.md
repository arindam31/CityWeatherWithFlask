# Docker setup (assuming docker is installed)

Start the docker container
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

Endpoint                                        Methods             Rule
----------------------------------------------  ------------------  ---------------------------------------------------
flasgger.<lambda>                               GET                 /apidocs/index.html
flasgger.apidocs                                GET                 /apidocs/
flasgger.apispec_1                              GET                 /apispec_1.json
flasgger.oauth_redirect                         GET                 /oauth2-redirect.html
flasgger.static                                 GET                 /flasgger_static/<path:filename>
get_city_forecast                               GET                 /forecast/<city>/<date>
get_city_forecast                               GET                 /forecast/<city>/
static                                          GET                 /static/<path:filename>
weather.cityweatherdetailsfromdatabase          DELETE, GET, PATCH  /api/cityweather/db/<int:id>
weather.cityweatherfromdatabaselistapi          GET, POST           /api/cityweather/db/<string:city>/<string:date>    
weather.cityweatherfromdatabaselistapi          GET, POST           /api/cityweather/db/<string:city>
weather.cityweatherwithmockdatalistapi          GET                 /api/cityweather/mocked/<string:city>/<string:date>
weather.cityweatherwithmockdatalistapi          GET                 /api/cityweather/mocked/<string:city>
weather_live.cityweatherfromweatherservice      GET                 /api/weather/live/<string:city>
weather_live.cityweatherfromweatherserviceordb  GET                 /api/weather/today/<string:city>
 ```