from django.contrib import admin
from .models import Image, Customer, Order, Product, Cart

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Image, ImageAdmin)


class CustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)

class OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Order, OrderAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)


class CartAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cart, CartAdmin)