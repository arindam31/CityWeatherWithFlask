# Weather data APIs with Flask

![Build](https://img.shields.io/github/actions/workflow/status/arindam31/Interview_management/django.yml?branch=main) ![Python](https://img.shields.io/badge/python-3.12%2B-blue)

## A flask project showing

  ✅ Receiving data from mock data (json file included) in an API.  
  ✅ Receiving data from MySQL database (loaded from json file)  
  ✅ Get live weather data for current day with an API  
  ✅ Usage of docker to orchestrate complete setup with test data loaded

## Features
🛡️ Live data from online weather service  
🛡️ Fully Dockerized  
🛡️ MySQL database used  
🛡️ Synchronized data  
🛡️ Restfull APIs  
🛡️ Continuous testing with github actions. (see github actions history)


## 🚀 QUICK Start
```bash
  git clone https://github.com/arindam31/Flask_Construction_Gis.git
  cd Flask_Construction_Gis
```
```bash
  pip install -r requirements.txt
  flask create-db
  flask load-data
  flask run
```
- Visit url: 127:0.0.1:500/api/cityweather/db/Vienna


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
  flask db upgrade
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