from django.urls import path
from . import views

urlpatterns = [
    path('', views.produkt_list, name='produkt_list'),
    path('dodaj/', views.produkt_create, name='produkt_create'),
]
