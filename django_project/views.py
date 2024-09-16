import requests
from django.shortcuts import render

def home(request):
  # USING APIS => Example 1
  response = requests.get('https://official-joke-api.appspot.com/random_joke')
  data = response.json()
  result = data['setup']
  
  response2 = requests.get('https://www.boredapi.com/api/activity')
  data2 = response2.json()
  result2 = data2['activity']
  
  response3 = requests.get('https://catfact.ninja/fact')
  data3 = response3.json()
  result3 = data3['fact']
  
  print('Result 1',result)
  print('Result 2', result2)
  print('Result 3',result3)

  
  return render(request, 'templates/index.html', {'result': result, 'result2': result2,'result3' : result3})