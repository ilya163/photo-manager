from django.contrib import admin
from .models import Image

class imageAdmin(admin.ModelAdmin):
    list_display = ["id","title", "image_url", "pub_date", "reporter"]

admin.site.register(Image, imageAdmin)