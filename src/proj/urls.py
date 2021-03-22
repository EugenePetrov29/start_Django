"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accs import urls as accs_urls
from cart import urls as cart_urls
from order import urls as order_urls

from groups import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page_list'),

    path('slovary', views.slovary, name='slovary'),

    path('admin/', admin.site.urls),
    path('accs/', include(accs_urls)),
    path('cart/', include(cart_urls, namespace="cart")),
    path('order/', include(order_urls, namespace="order")),

    path('authors/', views.AuthorsList.as_view(), name='authors_list'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('author-delete/<int:pk>/', views.AuthorDelete.as_view(), name='author_delete'),
    path('author-update/<int:pk>/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author-create/', views.AuthorCreate.as_view(), name='author_create'),

    path('genres/', views.GenresList.as_view(), name='genres_list'),
    path('genres-create/', views.GenresCreate.as_view(), name='genres_create'),
    path('genress/<int:pk>/', views.GenresDetail.as_view(), name='genres_detail'),
    path('genres-delete/<int:pk>/', views.GenresDelete.as_view(), name='genres_delete'),
    path('genres-update/<int:pk>/', views.GenresUpdate.as_view(), name='genres_update'),

    path('publishing_house/', views.PHList.as_view(), name='publishing_house_list'),
    path('publishing_house-create/', views.PHCreate.as_view(), name='publishing_house_create'),
    path('publishing_houses/<int:pk>/', views.PHDetail.as_view(), name='publishing_house_detail'),
    path('publishing_house-delete/<int:pk>/', views.PHDelete.as_view(), name='publishing_house_delete'),
    path('publishing_house-update/<int:pk>/', views.PHUpdate.as_view(), name='publishing_house_update'),

    path('series/', views.SeriesList.as_view(), name='series_list'),
    path('series-create/', views.SeriesCreate.as_view(), name='series_create'),
    path('seriess/<int:pk>/', views.SeriesDetail.as_view(), name='series_detail'),
    path('series-delete/<int:pk>/', views.SeriesDelete.as_view(), name='series_delete'),
    path('series-update/<int:pk>/', views.SeriesUpdate.as_view(), name='series_update'),

    path('book/', views.BookList.as_view(), name='book_list'),
    path('book-create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('book-delete/<int:pk>/', views.BookDelete.as_view(), name='book_delete'),
    path('book-update/<int:pk>/', views.BookUpdate.as_view(), name='book_update'),
]