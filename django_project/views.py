import requests
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Generating random dog breed images
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    random_dog_image = data['message']

    feedback = None  # Initializing feedback variable

    breed_name = request.GET.get('breed_name')

    if breed_name:
        # Make API request to fetch breed information
        url = f'https://api.thedogapi.com/v1/breeds/search?q={breed_name}'
        breed_response = requests.get(url)
        breed_data = breed_response.json()
        breed_info = breed_data[0] if breed_data else None

        if breed_info:
            return render(request, 'templates/index.html', {'random_dog_image': random_dog_image, 'breed_info': breed_info})
        else:
            error_message = 'Breed information not found.'
            return render(request, 'templates/index.html', {'random_dog_image': random_dog_image, 'error_message': error_message})

    if request.method == 'POST':
        user_guess = request.POST.get('user_guess').lower()
        actual_breed = data['message'].split('/')[-2].replace('-', ' ')  
        if user_guess == actual_breed.lower():
            feedback = 'Correct guess!'
        else:
            feedback = f'Incorrect guess! The actual breed is {actual_breed}.'

    return render(request, 'templates/index.html', {'random_dog_image': random_dog_image, 'feedback': feedback})
