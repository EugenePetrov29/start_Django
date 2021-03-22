from django.urls import path

from . import views
app_name = "order"
urlpatterns = [
    path('checkout_cart/', views.OrderUpdate.as_view(), name='checkout_cart'),
    
]
