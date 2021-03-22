from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('detail/<int:pk>/', views.ProfileDetail.as_view(), name='profile_detail'),
    path('update/<int:pk>/', views.ProfileUpdate.as_view(), name='profile_update'),
]
