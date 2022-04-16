from django.contrib import admin
from django.urls import path

from .views import index_view

app_name = 'main_website' 

urlpatterns = [
    path('home/', index_view, name='home'),
]