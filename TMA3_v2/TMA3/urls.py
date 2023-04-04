from django.urls import path, include
from django.contrib import admin
from . import views
from django.views.generic import TemplateView


app_name = 'TMA3'

urlpatterns = [
    path('', views.home, name='index'),
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
    path('p4products', views.p4products, name='p4products'),
    path('p4wishlist', views.p4wishlist, name='p4wishlist'),
    path('p4cart', views.p4cart, name='p4cart'),
    path('p4checkout', views.p4checkout, name='p4checkout'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('add_to_cart/<int:pk>', views.add_to_cart, name='add_to_cart'),
    path('add_to_wishlist/<int:pk>', views.add_to_wishlist, name='add_to_wishlist'),
    path('add_to_wishlist/part4', views.part4, name='add_to_wishlist_part4'),
    path('add_to_cart/part4', views.part4, name='add_to_cart_part4'),
    path('add_to_cart/p4checkout', views.p4checkout, name='add_to_cart_p4checkout'),
    path('add_to_cart/p4cart', views.p4cart, name='add_to_cart_p4cart'),
    path('add_to_cart/p4products', views.p4products, name='add_to_cart_p4products'),
    path('add_to_cart/p4wishlist', views.p4wishlist, name='add_to_cart_p4wishlist'),
    path('orders', views.orders, name='orders'),
    
]