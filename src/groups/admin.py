from django.contrib import admin
from . models import Authors, Publishing_house, Genres, Series

class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'author_name'
    ]

# Register your models here.
admin.site.register(Authors, AuthorAdmin)
admin.site.register(Publishing_house)
admin.site.register(Genres)
admin.site.register(Series)
