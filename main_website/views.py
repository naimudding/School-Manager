from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index_view(request):
	context = {"tab":"home"}
	return render(request, 'main_website/index.html',context)

class ServiceWorkerView(TemplateView):
    template_name = "main_website/serviceworker.js"
    content_type = 'application/javascript'

    def get_context_data(self, **kwargs):
        return {
            'version': '3.0.1',
        }

def offline_page(request):
    return render(request, 'main_website/offline.html', context={})

