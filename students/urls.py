from django.contrib import admin
from django.urls import path

from .views import std_home_view, add_std_view, std_list_view, std_profile_view, std_doc_view, std_terminate_view

from .rest_view import students_list
app_name = 'students' 

urlpatterns = [
    path('home/', std_home_view, name='std_home'),
    path('add_student/', add_std_view, name='add_student'),
    path('list_student/', std_list_view, name='list_student'),
    path('std_profile/<int:student_id>/', std_profile_view, name='std_profile'),
    path('std_docs/<int:student_id>/', std_doc_view, name='std_docs'),
    path('std_terminate/<int:student_id>/', std_terminate_view, name='std_terminate'),

    ##APIs
    path('ajax_list_students/', students_list),
]
