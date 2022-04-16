
from django.shortcuts import render

# Create your views here.
def std_home_view(request):
    return render(request, 'students/student_main.html')
