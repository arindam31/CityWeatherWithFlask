# Weather data APIs with Flask and React

![Build](https://img.shields.io/github/actions/workflow/status/arindam31/CityWeatherWithFlask/ci.yml?branch=master) ![Python](https://img.shields.io/badge/python-3.12%2B-blue) ![Flask](https://img.shields.io/badge/Flask-000?logo=flask&logoColor=fff)

![React](https://img.shields.io/badge/React-%2320232a.svg?logo=react&logoColor=%2361DAFB) ![Vite](https://img.shields.io/badge/Vite-646CFF?logo=vite&logoColor=fff)

## A flask project that stores and provides APIs for usage.

Following things are demoed:

  ✅ Receiving data from mock data (json file included) in an API.  
  ✅ Receiving data from MySQL database (loaded from json file)  
  ✅ Get live weather data for current day with an API.  
  ✅ Usage of docker to orchestrate complete setup with mock data loaded.

## Backend Project Features
🛡️ Live data from online weather service  
🛡️ Fully Dockerized  
🛡️ MySQL database used  
🛡️ Synchronized data  
🛡️ Restfull APIs  
🛡️ Continuous testing with github actions. (see github actions history)  
🛡️ Swagger document for trying APIs  
🛡️ Minimal Frontend with React to see weather data and search for cities to see current weather.


## 🚀 QUICK Start
```bash
  git clone https://github.com/arindam31/Flask_Construction_Gis.git
  cd Flask_Construction_Gis
```

For backend (create venv and activate it)
```bash
  pip install -r requirements.txt
  flask create-db
  flask load-data
  flask run
```
For frontend:
```bash
  cd .\frontend\my-weather-app\
  npm install
  npm run dev
```
- Visit and browse API lists with Swagger docs: http://127.0.0.1:5000/apidocs/
- Visit the frontend and try searching cities: http://localhost:5173/

With docker (recommended):
```bash
docker compose -f docker-compose-all-service.yaml up --build
```


## Setting up local environment:
- Clone the project from github/gitlab
- Create a virtual environment.
    ```bash
    python -m venv .venv
    ```
- Activate it (for windows)
  ```bash
  .venv/Scrpts/activate
  ```
- Create a local database and populate data.
  ```bash
  flask create-db
  flask load-data
  ```
- Test your setup
  - Check for routes or run API tests
  ```bash
  flask routes
  pytest -v
  ```

## 🧪 Running Tests

📌 The tests are located under `/tests`.  

```bash
  pytest
  pytest -s # To see prints too
  pytest -s -k "keyword" # Run tests matching a keyword
  ```

  ## 📜 Documentation

📄 Detail documentation on sub topics are available in the docs/ directory.

📙 [Docker](docs/docker_guide.md), 📙 [Database](docs/db_wiki.md)

  ## 🙌 Contributors
👤 Arindam Roychowdhury