from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.template import loader
from .models import Image
from django.core.serializers import serialize
from django.shortcuts import render
from json import dumps
from django.http import JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import TemplateView
import datetime



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
      return render(request, 'part4.html')


def products(request):
      return render(request, 'products.html')

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