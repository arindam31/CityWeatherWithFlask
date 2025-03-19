import React, { useState } from 'react';
import WeatherDisplay from './WeatherDisplay.jsx';
import SearchBox from './SearchBox.jsx';

const App = () => {
  const [weatherData, setWeatherData] = useState(null);

  const fetchWeather = async (city) => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/api/cityweather/db/${city}`);
      const data = await response.json();
      
      
      // Mapping API response to your display format
      const formattedData = data.map(item => ({
        city: city,
        temp: item.temperature,
        humidity: item.humidity,
        condition: item.condition,
        date: item.date,
      }));
      
      setWeatherData(formattedData);
    } catch (error) {
      console.error("Error fetching weather data:", error);
    }
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
