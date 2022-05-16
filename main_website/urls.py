from django.contrib import admin
from django.urls import path

from .views import index_view, ServiceWorkerView, offline_page

app_name = 'main_website' 

urlpatterns = [
    path('home/', index_view, name='home'),
    path('offline/', offline_page, name='offline'),
    path('serviceworker', ServiceWorkerView.as_view(), name='sw'),
]