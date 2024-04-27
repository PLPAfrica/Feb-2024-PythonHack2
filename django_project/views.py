import requests
from django.shortcuts import render

def home(request):
  # USING APIS => Example 1
  # views.py
  import requests
from django.shortcuts import render

def home(request):
    # Fetching data from the Car API
    car_response = requests.get('https://api.Bentley.com/cars')
    car_data = car_response.json()
    car_result = car_data["cars"]

    # Fetching data from the Ship API
    ship_response = requests.get('https://api.maersk.com/ships')
    ship_data = ship_response.json()
    ship_result = ship_data["ships"]

    return render(request, 'index.html', {'car_result': car_result, 'ship_result': ship_result})
