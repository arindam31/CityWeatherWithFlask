import React, { useState } from 'react';

const SearchBox = ({ onSearch, fetchTodaysWeather }) => {
  const [city, setCity] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch(city); // Search weather by city name
  };

  const handleGetTodaysWeather = () => {
    fetchTodaysWeather(city); // Fetch today's weather
  };

  return (
    <form onSubmit={handleSubmit} className="mb-4">
      <div className="input-group">
        <input
          type="text"
          value={city}
          onChange={(e) => setCity(e.target.value)}
          placeholder="Enter city"
          className="form-control"
        />
        <button type="submit" className="btn btn-primary">Search</button>
        <button 
          type="button" 
          className="btn btn-secondary ms-2" 
          onClick={handleGetTodaysWeather}
        >
          Get Today's Weather
        </button>
      </div>
    </form>
  );
};

export default SearchBox;
