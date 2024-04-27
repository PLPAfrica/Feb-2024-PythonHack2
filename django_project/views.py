import requests
from django.shortcuts import render
import random

def index(request):
      # Fetch a random fact
    fact_response = requests.get('https://uselessfacts.jsph.pl/random.json?          language=en')
    fact_data = fact_response.json()
    fact = fact_data['text']

      # Fetch student data
    student_response = requests.get('https://freetestapi.com/api/v1/students')
    student_data = student_response.json()
    students = student_data['students']

      # Shuffle the list of students
    random.shuffle(students)

      # Get the name of the first student
    if students:
      first_student_name = students[0]['name']
    else:
      first_student_name = "No students available"

      # Render the index.html template with data
    return render(request, 'index.html', {'fact': fact, 'name':             
      first_student_name})
