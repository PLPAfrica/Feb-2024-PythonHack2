import requests
from django.shortcuts import render 

def index(request):
    response = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
    data = response.json()
    fact = data['text']

    r3 = requests.get('https://dog.ceo/api/breeds/image/random')
    res3 = r3.json()
    dog = res3['message']

    response2 = requests.get('https://freetestapi.com/api/v1/students')
    data2 = response2.json()
    name = data2[0]['name']

    return render(request, 'templates/index.html', {'fact': fact, 'dog': dog, 'name': name})
  
