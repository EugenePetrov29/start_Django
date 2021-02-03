from django.shortcuts import render
from django.http import HttpResponse
from groups.models import Authors

# Create your views here.
def home_page(request):
    author = Authors.objects.last()
    context = {'author': author}
    return render(request, template_name='home.html', context=context)