from django.db import models
from django.views.generic import TemplateView

# Creates a table 
class Part2(models.Model):
    # blank is required, null allows a null value
    image_source = models.CharField(max_length=140, blank=False, null=False)
    image_caption = models.CharField(max_length=140, blank=False, null=False)


    def __str__(self):
        return self.image_source
    
    def __str__(self):
        return self.image_caption
    
# Part 2 Images class
class Image(models.Model):
    image_name = models.CharField(max_length=140, blank=False, null=False)
    image_location = models.CharField(max_length=140, blank=False, null=False)
    image_caption = models.CharField(max_length=140, blank=False, null=False)
    
    def __str__(self):
        return self.image_location
    
    
    
