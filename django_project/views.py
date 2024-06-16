import requests
import random
from django.http import HttpRequest
from django.shortcuts import render
from decouple import config

def main(request: HttpRequest):
               #THE WEATHER API
  BASE_URL = 'https://api.weatherapi.com/v1/current.json?'
  API_KEY = 'cf8227e228814bd894a131010242604'
  CITY = str(request.GET.get('city', 'London'))
  cityContext = CITY

  url = BASE_URL + 'key=' + API_KEY + '&q=' + CITY
  response = requests.get(url)
  data = response.json()
  time = data["location"]["localtime"]
  region = data["location"]["region"]
  country = data["location"]["country"]
  latitude = data["location"]["lat"]
  longitude = data["location"]["lon"]
  timezone = data["location"]["tz_id"]
  current_time = data["current"]["last_updated"]
  temp_degrees = data["current"]["temp_c"]
  temp_farenheit = data["current"]["temp_f"]
  weather_description = data["current"]["condition"]["text"]
  wind_speedKPH = data["current"]["wind_kph"]
  wind_speedMPH = data["current"]["wind_mph"]
  humidity = data["current"]["humidity"]

  weatherAPI =  {'time': time, 'region': region, 'country': country, 'latitude': latitude, 'longitude': longitude, 'timezone': timezone, 'current_time': current_time, 'temp_degrees': temp_degrees, 'temp_farenheit': temp_farenheit,'weather_description': weather_description, 'wind_speedKPH': wind_speedKPH, 'wind_speedMPH': wind_speedMPH, 'humidity': humidity}



                  #THE RANDOM QUOTES API
  resp = requests.get('https://type.fit/api/quotes')
  QUOTES = resp.json()
  quote_index = random.randint(0, len(QUOTES) - 1)
  quote = QUOTES[quote_index]["text"]
  author = QUOTES[quote_index]["author"]

  quotesAPI = {'quote': quote, 'author': author}


                #THE UNSPLASH API
  BASE_URL = 'https://api.unsplash.com/search/photos?'
  client_id = 'Sxv9jRKP7YRhBpKSkyK8Y4wPbu2wU9_I75lZeawIOYo'
  url = BASE_URL + 'client_id=' + client_id + '&query=' + CITY

  response = requests.get(url)
  images = response.json()
  image_index = random.randint(0, len(images) - 1)
  image_display = images["results"][image_index]["urls"]["regular"]

  imageAPI = {'image_display': image_display}

  #Building the context for both the APIs
  context = {**{'cityContext': cityContext}, **weatherAPI, **quotesAPI, **imageAPI}

  return render(request, 'templates/index.html', context)




