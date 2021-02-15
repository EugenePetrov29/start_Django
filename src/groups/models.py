from django.db import models

# Create your models here.
class Authors(models.Model):
    author_name = models.CharField("Имя автора", max_length=50)
    author_description = models.TextField("Краткая биография", null = True, blank = True)  

    def __str__(self):
        return self.author_name

class Genres(models.Model):
    genres_name = models.CharField("Жанр", max_length=50)
    genres_description = models.TextField("Описание", null = True, blank = True)

    def __str__(self):
        return self.genres_name

class Publishing_house(models.Model):
    publishing_house_name = models.CharField("Издательство", max_length=50)

    def __str__(self):
        return self.publishing_house_name

class Series(models.Model):
    series_name = models.CharField("Серия", max_length=50)
    
    def __str__(self):
        return self.series_name