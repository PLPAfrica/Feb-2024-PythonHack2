import os
import requests
from django.shortcuts import render
from django.utils.timezone import now
from datetime import timedelta
from .models import WeatherData
import logging
import dotenv

logger = logging.getLogger(__name__)

API_BASE_URL = 'https://api.weatherapi.com/v1/current.json'
API_KEY = dotenv.get_key('.env', 'WEATHER_API_KEY')


def get_weather_for_location(request, location):
    try:
        # Check if we have recent weather data in cache
        recent_time_threshold = now() - timedelta(hours=1)  # considers data recent for 1 hour
        recent_weather = WeatherData.objects.filter(location=location, timestamp__gte=recent_time_threshold).first()

        if recent_weather:
            logger.info(f"Found recent weather data for location: {location}")
            return render(request, 'weather_data.html', {'weather': recent_weather})

        # Make a request to the weather API if no recent data is found
        response = requests.get(f"{API_BASE_URL}/current.json?key={API_KEY}&q={location}")
        if response.status_code == 200:
            weather_data = response.json()
            # Extract necessary fields from the API response
            temperature = weather_data['current']['temp_c']
            conditions = weather_data['current']['condition']['text']
            icon = weather_data['current']['condition']['icon']
            # Save the new weather data to the database
            weather = WeatherData(location=location, temperature=temperature, conditions=conditions,
                                  condition_icon=icon,
                                  timestamp=now())  # Added timestamp when saving new weather data
            weather.save()
            logger.info(f"Saved new weather data for location: {location}")
            return render(request, 'weather_data.html', {'weather': weather})
        else:
            logger.error(f"Failed to fetch weather data for location: {location}. Status code: {response.status_code}")
            return render(request, 'weather_error.html',
                          {'error': f"Failed to fetch weather data for location: {location}."})
    except Exception as e:
        logger.error(f"Error fetching weather data for location: {location}. Error: {e}", exc_info=True)
        return render(request, 'weather_error.html',
                      {'error': f"Error fetching weather data for location: {location}."})
