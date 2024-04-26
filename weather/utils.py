from .models import WeatherData
from django.utils.timezone import now
from datetime import timedelta
import requests
import logging
import os

logger = logging.getLogger(__name__)

API_KEY = os.environ.get('WEATHER_API_KEY')  # Use environment variable for API key
API_BASE_URL = 'http://api.weatherapi.com/v1/current.json'


def get_weather_data_for_location(location):
    recent_time_threshold = now() - timedelta(hours=1)
    recent_weather = WeatherData.objects.filter(location=location, timestamp__gte=recent_time_threshold).first()

    if recent_weather:
        logger.info(f"Found recent weather data for location: {location}")
        return recent_weather
    else:
        try:
            response = requests.get(f"{API_BASE_URL}?key={API_KEY}&q={location}")
            if response.status_code == 200:
                weather_data = response.json()
                temperature = weather_data['current']['temp_c']
                conditions = weather_data['current']['condition']['text']
                weather = WeatherData(location=location, temperature=temperature, conditions=conditions)
                weather.save()
                logger.info(f"Saved new weather data for location: {location}")
                return weather
            else:
                logger.error(
                    f"Failed to fetch weather data for location: {location}. Status code: {response.status_code}")
        except Exception as e:
            logger.error(f"Error fetching weather data for location: {location}. Error: {e}", exc_info=True)
