
from django.urls import path

from weatherapp import views

app_name = 'weatherapp'

urlpatterns = [
    # path('index/', views.index, name='index'),
    path('', views.weather, name='weather'),

]  