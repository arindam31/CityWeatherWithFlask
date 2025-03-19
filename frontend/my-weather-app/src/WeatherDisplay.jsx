import React from 'react';

const WeatherDisplay = ({ weatherData }) => {
  return (
    <div className="d-flex flex-wrap justify-content-center">
      {weatherData ? (
        weatherData.map((weatherItem, index) => (
          <div className="card p-4 shadow-sm mx-2 my-3" style={{ maxWidth: '300px' }} key={index}>
            <div className="card-body">
              <h5 className="card-title">{weatherItem.city}</h5>
              <p className="card-text"><strong>Date:</strong> {weatherItem.date}</p>
              <p className="card-text"><strong>Temperature:</strong> {weatherItem.temp}</p>
              <p className="card-text"><strong>Humidity:</strong> {weatherItem.humidity}</p>
              <p className="card-text"><strong>Condition:</strong> {weatherItem.condition}</p>
            </div>
          </div>
        ))
      ) : (
        <p className="text-muted">Enter a city to get the weather forecast.</p>
      )}
    </div>
  );
};


export default WeatherDisplay;
