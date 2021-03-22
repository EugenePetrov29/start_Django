from django.shortcuts import render
from django.http import HttpResponse
from groups.models import Authors
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from .models import Authors, Genres, Publishing_house, Series, Book
from groups import models as ref_models


# Create your views here.


class HomePage(ListView):
    model = Book
    template_name ='groups/homepage_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = ref_models.Book.objects.all().order_by("-pk")[:5]
        context["authors"] = ref_models.Authors.objects.all().order_by("-pk")[:5]
        return context
    
    

#Страница со словарями
def slovary(request):
    context = {}
    return render(request, template_name="slovary.html", context=context)



#АВТОРЫ
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



#ЖАНРЫ
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



#Издательства
class PHList(ListView):
    model = Publishing_house

class PHCreate(CreateView):
    model = Publishing_house
    success_url = "/publishing_house/"
    fields = ('publishing_house_name', 'publishing_house_description')
    template_name_field = 'publishing_house'

class PHDetail(DetailView):
    model = Publishing_house

class PHDelete(DeleteView):
    success_url = "/publishing_house/"
    model = Publishing_house

class PHUpdate(UpdateView):
    model = Publishing_house
    success_url = "/publishing_house/"
    fields = ('publishing_house_name', 'publishing_house_description')
    template_name_suffix = '_update'



#СЕРИИ
class SeriesList(ListView):
    model = Series

class SeriesCreate(CreateView):
    model = Series
    success_url = "/series/"
    fields = ('series_name', 'series_description')
    template_name_field = 'series'

class SeriesDetail(DetailView):
    model = Series

class SeriesDelete(DeleteView):
    success_url = "/series/"
    model = Series

class SeriesUpdate(UpdateView):
    model = Series
    success_url = "/series/"
    fields = ('series_name', 'series_description')
    template_name_suffix = '_update'



#КНИГИ
class BookList(ListView):
    model = Book

class BookCreate(CreateView):
    model = Book
    success_url = "/book/"
    fields = (
        'book_img',
        'book_name',
        'book_desc',
        'book_genre',  
        'book_auth',
        'book_ph',
        'book_sery',
        'price'
    )
    template_name_field = 'book'

class BookDetail(DetailView):
    model = Book

class BookDelete(DeleteView):
    success_url = "/book/"
    model = Book

class BookUpdate(UpdateView):
    model = Book
    success_url = "/book/"
    fields = (
        'book_img',
        'book_name',
        'book_desc',
        'book_genre',  
        'book_auth',
        'book_ph',
        'book_sery',
        'price'
    )
    template_name_suffix = '_update'