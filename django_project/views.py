import requests
from django.shortcuts import render

def home(request):
    # generating random dog images
    dog_image_response = requests.get('https://dog.ceo/api/breeds/image/random')
    dog_image = dog_image_response.json()
    random_dog_image = dog_image['message']
    
    return render(request, 'index.html', {'random_dog_image': random_dog_image})

    # generating facts

def get_random_dog_fact(request):
    response = requests.get('https://api.dog-facts-api.dog/facts/random')
    data = response.json()
    random_dog_fact = data['fact']
    
    return render(request, 'index.html', {'random_dog_fact': random_dog_fact})
