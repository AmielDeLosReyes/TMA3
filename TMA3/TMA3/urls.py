from django.urls import path, include
from django.contrib import admin
from . import views
from django.views.generic import TemplateView


app_name = 'TMA3'

urlpatterns = [
    path('TMA3', views.home, name='index'),
    path('home', views.home, name='home'),
    path('part1', views.ip, name='part1'),
    path('part2', views.part2, name='part2'),
    path('part3', views.part3, name='part3'),
    path('part4', views.part4, name='part4'),
    path('ip', views.ip),
    path('products', views.products, name='products'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    
]