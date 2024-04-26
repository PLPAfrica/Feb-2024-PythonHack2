from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from blog.views import index
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('index/', index, name='index'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile_manager, name='profile'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
]
