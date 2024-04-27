import requests
from django.shortcuts import render

def home(request):
  # USING APIS => Example 1
  response = requests.get('https://api.github.com/events')
  data = response.json()
  result = data[0]["repo"]

  # Example 2
  reponse2 = requests.get('https://dog.ceo/api/breeds/image/random')
  data2 = reponse2.json()
  result2 = data2["message"]

  # USING APIS => Example 3
  response3 = requests.get('https://api.chucknorris.io/jokes/random')
  data3 = response3.json()
  result3 = data3["value"]
  
