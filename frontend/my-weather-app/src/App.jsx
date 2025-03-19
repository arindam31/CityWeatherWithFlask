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

  const fetchTodaysWeather = async (city) => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/api/weather/live/${city}`);
      const data = await response.json();
      
      // Directly use the data since it's a single object
      const formattedData = {
        city: city,
        temp: data.temperature, // Correct field names from the API response
        humidity: data.humidity,
        condition: data.condition,
        date: new Date().toLocaleDateString(), // Set today's date manually
      };

      setWeatherData([formattedData]); // Set today's weather wrapped in an array
    } catch (error) {
      console.error("Error fetching today's weather:", error);
    }
  };

  return (
    <div className="d-flex justify-content-center align-items-center vh-100">
      <div className="text-center">
        <h1 className="mb-4">Weather App</h1>
        <SearchBox onSearch={fetchWeather} fetchTodaysWeather={fetchTodaysWeather}/>
        <WeatherDisplay weatherData={weatherData} />
      </div>
    </div>
  );
};


export default App;
