from django.contrib import admin
from .models import Part2, Image

# Register your models here.
class Part2Admin(admin.ModelAdmin):
    pass

admin.site.register(Part2, Part2Admin)

class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Image, ImageAdmin)
