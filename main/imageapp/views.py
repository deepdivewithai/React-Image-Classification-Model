from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from imageapp.models import Image

class MainView(TemplateView):
    template_name = 'main.html'


def file_upload_view(request):
    # print(request.FILES)
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        Image.objects.create(file=my_file)
        return HttpResponse('')
    return JsonResponse({'post': 'false'})
