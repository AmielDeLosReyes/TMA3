from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.template import loader
from .models import Image, Customer, Order, Product, Cart
from django.core.serializers import serialize
from django.shortcuts import render
from json import dumps
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import TemplateView
import datetime
from django import forms
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect



# Create your views here.
def home(request):
      return render(request, 'index.html')

def productSummary(request):
     return render(request, 'productSummary.html')
    
def part2(request):
      template = loader.get_template('part2.html')

      images = Image.objects.all().values()
      imageName = Image.objects.values_list('image_name', flat=True)
      imageLocation = Image.objects.values_list('image_location', flat=True)
      imageCaption = Image.objects.values_list('image_caption', flat=True)

      
      context = {
          'image_name': imageName,
          'image_location': imageLocation,
          'image_caption': imageCaption
      }
      
      
      return render(request, 'part2.html', context)
      

def part3(request):
      return render(request, 'part3.html')


def part4(request):

      products = Product.objects.all().values()

      product_name = Product.objects.values_list('product_name', flat=True)
      product_image = Product.objects.values_list('product_image', flat=True)
      produce_price = Product.objects.values_list('product_price', flat=True)

      context = {
          'product_name': product_name,
          'product_image': product_image,
          'produce_price': produce_price
      }

      context1 = {
            'myProducts': products
      }

      
      # return HttpResponse(st)
      return render(request, 'part4.html', context1)

def orders(request):
      products = Product.objects.all().values()

      context1 = {
            'myProducts': products
      }
      return render(request, 'orders.html', context1)

def signup(request):
      if request.method == 'POST':
           if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('email') and request.POST.get('password'):
                  
                  if len(request.POST.get('password')) < 8:
                        return HttpResponse("Password mus be 8 characters or more! Please hit back.")
                  
                  else:
                        customer = Customer()
                        customer.customer_firstname = request.POST.get('firstname')
                        customer.customer_lastname = request.POST.get('lastname')
                        customer.customer_email = request.POST.get('email')
                        customer.customer_pass = request.POST.get('password')
                        customer.save()

                        request.session['firstname'] = customer.customer_firstname
                        request.session['lastname'] = customer.customer_lastname
                        request.session['email'] = customer.customer_email
                        products = Product.objects.all().values()
                        context = {
                              'firstname': request.session['firstname'],
                              'lastname': request.session['lastname'],
                              'email': customer.customer_email,
                              'myProducts': products
                        }
                        return render(request, 'part4.html', context)
      else:
            return render(request, 'signup.html')
      
# Needs some fix
def add_to_cart(request, pk):
      products = Product.objects.all().values()

      cart = Cart()

      product_name_selected = Product.objects.values_list('product_name', flat=True).get(product_id=pk)
      product_image_selected = Product.objects.values_list('product_image', flat=True).get(product_id=pk)
      product_price_selected = Product.objects.values_list('product_price', flat=True).get(product_id=pk)


      cart.cart_product_name = product_name_selected
      cart.cart_product_image = product_image_selected
      cart.cart_product_price = product_price_selected

      cart_products = []

      # cart_products.append()


      context = {
            'cart_product_name': cart.cart_product_name,
            'cart_product_image': cart.cart_product_image,
            'cart_product_price': cart.cart_product_price

      }
      return render(request, 'p4cart.html', context)


def add_to_wishlist(request, pk):
      products = Product.objects.all().values()

      cart = Cart()

      product_name_selected = Product.objects.values_list('product_name', flat=True).get(product_id=pk)
      product_image_selected = Product.objects.values_list('product_image', flat=True).get(product_id=pk)
      product_price_selected = Product.objects.values_list('product_price', flat=True).get(product_id=pk)


      cart.cart_product_name = product_name_selected
      cart.cart_product_image = product_image_selected
      cart.cart_product_price = product_price_selected
      cart.save()

      cart_products = []

      # cart_products.append()


      context = {
            'cart_product_name': cart.cart_product_name,
            'cart_product_image': cart.cart_product_image,
            'cart_product_price': cart.cart_product_price

      }
      return render(request, 'p4wishlist.html', context)


def login(request):
      if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            userEmail = Customer.objects.values_list('customer_email', flat=True).get(customer_email=email)
            userPass = Customer.objects.values_list('customer_pass', flat=True).get(customer_email=email)
            userFname = Customer.objects.values_list('customer_firstname', flat=True).get(customer_email=email)
            userLname = Customer.objects.values_list('customer_lastname', flat=True).get(customer_email=email)
            products = Product.objects.all().values()

            
            if userEmail == email and userPass == password:
                  context = {
                        'firstname': userFname,
                        'lastname': userLname,
                        'myProducts': products
                  }
                  return render(request, 'part4.html', context)
      return render(request, 'login.html')
      

def products(request):
      return render(request, 'products.html')

def p4products(request):
      products = Product.objects.all().values()

      context1 = {
            'myProducts': products
      }

      return render(request, 'p4products.html', context1)

def p4wishlist(request):
      products = Product.objects.all().values()

      context1 = {
            'myProducts': products
      }

      return render(request, 'p4wishlist.html', context1)

def p4cart(request):
      return render(request, 'p4cart.html')

def p4checkout(request):
      return render(request, 'p4checkout.html')

def wishlist(request):
      return render(request, 'wishlist.html')

def cart(request):
      return render(request, 'cart.html')

def checkout(request):
      return render(request, 'checkout.html')


# Grabbing Client's IP Address and setting persistent cookie
def ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

# Set persistent cookie
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

#     now = timezone.now()
    now = datetime.datetime.now()

    context = {'ipAddress' : ip, 'timezone': now, 'num_visits': request.session['num_visits']}

    return render(request, 'part1.html', context)


# Query all images
def getImages(request):
     myData = Image.objects.all().values
     template = loader.get_template('part2.html')
     
     context = {
          'allImages': myData
     }

     return HttpResponse(template.render(context, request))
        
# Query image infos        
def getImageInfo(request):
     imageName = Image.objects.values_list('image_name')
     imageLocation = Image.objects.values_list('image_location')
     imageCaption = Image.objects.values_list('image_caption')

     template = loader.get_template('part2.html')

     context = {
          'imageName': imageName,
          'imageLocation': imageLocation,
          'imageCaption': imageCaption
     }

     return HttpResponse(template.render(context, request))

# JSON grab data
def django_models_json(request):
    template = loader.get_template('part2.html')

    qs = Image.objects.all()
    data = serialize("json", qs, fields=('image_name', 'image_location', 'image_caption'))
    return HttpResponse(template.render(data, request, content_type="application/json"))