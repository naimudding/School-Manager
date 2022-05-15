from django.shortcuts import render

# Create your views here.
def index_view(request):
	context = {"tab":"home"}
	return render(request, 'main_website/index.html',context)
