from django.contrib import admin

# Register your models here.
from .models import StudentWork
from courses.models import Module

admin.site.register(Module)
admin.site.register(StudentWork)