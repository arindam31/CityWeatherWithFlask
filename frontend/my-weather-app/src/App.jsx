import React, { useState } from 'react';
import WeatherDisplay from './WeatherDisplay.jsx';
import SearchBox from './SearchBox.jsx';

const App = () => {
  const [weatherData, setWeatherData] = useState(null);

  const fetchWeather = async (city) => {
    const mockData = {
      city: city,
      temp: 22,
      humidity: 60,
      condition: 'Clear',
    };
    setWeatherData(mockData);
  };

  return (
    <div className="d-flex justify-content-center align-items-center vh-100">
      <div className="text-center">
        <h1 className="mb-4">Weather App</h1>
        <SearchBox onSearch={fetchWeather} />
        <WeatherDisplay weatherData={weatherData} />
      </div>
    </div>
  );
};

export default App;
