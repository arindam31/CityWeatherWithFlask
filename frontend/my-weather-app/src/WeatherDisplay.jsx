import React from 'react';

const WeatherDisplay = ({ weatherData }) => {
  return (
    <div>
      {weatherData ? (
        <div className="card p-4 shadow-sm mx-auto" style={{ maxWidth: '400px' }}>
          <h3>{weatherData.city}</h3>
          <p><strong>Temperature:</strong> {weatherData.temp}°C</p>
          <p><strong>Humidity:</strong> {weatherData.humidity}%</p>
          <p><strong>Condition:</strong> {weatherData.condition}</p>
        </div>
      ) : (
        <p className="text-muted">Enter a city to get the weather forecast.</p>
      )}
    </div>
  );
};

export default WeatherDisplay;
