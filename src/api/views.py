from django import http
from django.shortcuts import render

import requests
API_KEY = '2f7465f8536c40cfb8f14889230503b4'

# Create your views here.


def home(request):
    url = f'http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    print(data)

    articles = data['articles']

    context = {
        'articles' : articles
    }

    return render(request, 'home.html', context)


