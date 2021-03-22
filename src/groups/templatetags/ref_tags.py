from django import template
from groups.models import Authors, Genres, Publishing_house, Series, Book
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def book_img_safe(pk):
    book = Book.objects.get(pk=pk).book_img
    return mark_safe('/static/' + str(book))