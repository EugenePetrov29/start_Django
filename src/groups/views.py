from django.shortcuts import render
from django.http import HttpResponse
from groups.models import Authors
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from .models import Authors

# Create your views here.
class AuthorsList(ListView):
    model = Authors

class AuthorUpdate(UpdateView):
    model = Authors
    success_url = "/authors/"
    fields = ('author_name', 'author_description')

class AuthorCreate(CreateView):
    model = Authors
    success_url = "/authors/"
    fields = ('author_name', 'author_description')

class AuthorDetail(DetailView):
    model = Authors


class AuthorDelete(DeleteView):
    success_url = "/authors/"
    model = Authors



