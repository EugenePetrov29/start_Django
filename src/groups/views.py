from django.shortcuts import render
from django.http import HttpResponse
from groups.models import Authors
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from .models import Authors, Genres

# Create your views here.
class AuthorsList(ListView):
    model = Authors

class AuthorUpdate(UpdateView):
    model = Authors
    success_url = "/authors/"
    fields = ('author_name', 'author_description')
    template_name_suffix = '_update'

class AuthorCreate(CreateView):
    model = Authors
    success_url = "/authors/"
    fields = ('author_name', 'author_description')

class AuthorDetail(DetailView):
    model = Authors


class AuthorDelete(DeleteView):
    success_url = "/authors/"
    model = Authors

class GenresList(ListView):
    model = Genres

class GenresCreate(CreateView):
    model = Genres
    success_url = "/genres/"
    fields = ('genres_name', 'genres_description')
    template_name_field = 'genres'

class GenresDetail(DetailView):
    model = Genres

class GenresDelete(DeleteView):
    success_url = "/genres/"
    model = Genres

class GenresUpdate(UpdateView):
    model = Genres
    success_url = "/genres/"
    fields = ('genres_name', 'genres_description')
    template_name_suffix = '_update'