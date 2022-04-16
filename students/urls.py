from django.contrib import admin
from django.urls import path

from .views import std_home_view

app_name = 'students' 

urlpatterns = [
    path('home/', std_home_view, name='std_home'),
]
