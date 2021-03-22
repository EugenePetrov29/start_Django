from django.conf import settings
from django.db import models
import datetime

# Create your models here.


class Authors(models.Model):
    author_name = models.CharField("Имя автора", max_length=50)
    author_description = models.TextField("Краткая биография", null = True, blank = True) 
    author_img = models.ImageField(
        upload_to = 'images',
        null = True, 
        blank = True
        ) 

    def __str__(self):
        return self.author_name

class Genres(models.Model):
    genres_name = models.CharField("Жанр", max_length=50)
    genres_description = models.TextField("Описание", null = True, blank = True)

    def __str__(self):
        return self.genres_name

class Publishing_house(models.Model):
    publishing_house_name = models.CharField("Издательство", max_length=50)
    publishing_house_description = models.TextField("Описание", null = True, blank = True)

    def __str__(self):
        return self.publishing_house_name

class Series(models.Model):
    series_name = models.CharField("Серия", max_length=50)
    series_description = models.TextField("Описание", null = True, blank = True)
    
    def __str__(self):
        return self.series_name

class Book(models.Model):
    book_name = models.CharField("Название", max_length=50)
    book_desc = models.TextField("Описание", null = True, blank = True)
    book_auth = models.ForeignKey(Authors, verbose_name="Автор", on_delete = models.PROTECT)
    book_genre = models.ForeignKey(Genres, verbose_name="Жанр", on_delete = models.PROTECT)
    book_ph = models.ForeignKey(Publishing_house, verbose_name="Издательство", on_delete = models.PROTECT, null = True, blank = True)
    book_sery = models.ForeignKey(Series, verbose_name="Серия", on_delete = models.PROTECT, null = True, blank = True)
    book_add = models.DateTimeField(
        verbose_name="Время добавления",
        auto_now=False,
        auto_now_add=True
    )
    book_img = models.ImageField(
        upload_to = 'images',
        null = True, 
        blank = True
        )
    price = models.DecimalField(
        verbose_name="Цена/бел.руб",
        default=0,
        max_digits=5,
        decimal_places=2
    )