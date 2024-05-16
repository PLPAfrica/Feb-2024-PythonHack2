

import requests
import json 
from django.shortcuts import render


def weather(request):
  response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=66048f26223dbab85dbd25354dc61f58')
  data = response.json() 
  result3 = data ['icon']
  
  return render(request, 'templatesweather/weather.html',{'result3':result3})
# Create your views here.
  
