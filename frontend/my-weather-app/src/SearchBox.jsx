import React, { useState } from 'react';

const SearchBox = ({ onSearch }) => {
  const [city, setCity] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch(city);
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
      </div>
    </form>
  );
};

export default SearchBox;
