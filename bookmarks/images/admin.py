from django.contrib import admin

from .models import Image,Bookmark



@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug','category','image','blogType', 'created']
    list_filter = ['created']

admin.site.register(Bookmark)