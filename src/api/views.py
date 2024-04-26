from django.shortcuts import render
import requests

API_KEY = '2f7465f8536c40cfb8f14889230503b4'

def home(request):
    country = request.GET.get('country', 'us')
    category = request.GET.get('category')

    if country and category:  
        url = f'http://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={API_KEY}'
    elif country:  
        url = f'http://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
    elif category:  
        url = f'http://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
    else:  
        url = f'http://newsapi.org/v2/top-headlines?apiKey={API_KEY}'

    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    context = {
        'articles': articles
    }

    return render(request, 'home.html', context)
