from app import db
from sqlalchemy.orm import relationship


class CityWeather(db.Model):
    __tablename__ = "city_weather"

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), unique=True)
    
    forecast = relationship("Forecast", back_populates="city_weather", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<CityWeather(id={self.id}, city={self.city})>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'city': self.city,
        }


class Forecast(db.Model):
    __tablename__ = 'forecast'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10))
    temperature = db.Column(db.String(10))
    humidity = db.Column(db.String(4))
    condition = db.Column(db.String(20))
    wind_speed = db.Column(db.String(10))
    city_id = db.Column(db.Integer, db.ForeignKey('city_weather.id'))
    city_weather = db.relationship("CityWeather", back_populates="forecast")

    def __repr__(self):
        return f"<Forecast(id={self.id}, date={self.date}, city_id={self.city_id})>"