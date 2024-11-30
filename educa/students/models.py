from django.db import models
from courses.models import Subject, Content,Course,Module,ContentType
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.loader import render_to_string

from courses.fields import OrderField
from django.core.validators import FileExtensionValidator 

# Create your models here.
class StudentWork(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    module = models.ForeignKey(Module,on_delete=models.CASCADE)
    content_type = models.CharField(max_length=50)
    content = models.TextField(null= True ,blank=True)
    image = models.ImageField(upload_to = 'uploads/images/',null =True , blank=True, validators=[FileExtensionValidator(['png'])])
    video =models.FileField(upload_to = 'uploads/videos/',null =True , blank=True, validators=[FileExtensionValidator(['mp4'])])
    file = models.FileField(upload_to = 'uploads/files/',null =True , blank=True, validators=[FileExtensionValidator(['pdf'])])
    link = models.URLField(blank=True, null =True)

    def __str__(self):
        return self.title

class ItemBase(models.Model):
   
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def render(self):
        return render_to_string(
            f'students/content/{self._meta.model_name}.html',
            {'item': self},
        )


class Text(ItemBase):
    content = models.TextField()


class File(ItemBase):
    file = models.FileField(upload_to='files')


class Image(ItemBase):
    file = models.FileField(upload_to='images')


class Video(ItemBase):
    url = models.URLField()
