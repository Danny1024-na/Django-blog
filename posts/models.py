from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.
'''
vaidation
html widget
field types
(drei Vorteiele von Verebung von models)

'''

class Post(models.Model): #vererbung von models
    #eien Tabbele von models hat zwei Spalten title und content
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=10000)
    image =models.ImageField(upload_to='posts/',default='default.jpg')
    author = models.ForeignKey(User,related_name='Post_author',on_delete=models.CASCADE)
    tags =TaggableManager()
    category = models.ForeignKey('Category',related_name='post_category',on_delete=models.CASCADE,null=True,blank=True)

    #um die Name des Posts zu zeigen
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# class Chefs(models.Model):
#     name = models.CharField(max_length=10)
#     work = models.CharField(max_length=15)
#     image =models.ImageField(upload_to='posts/',default='default.jpg')

#     def __str__(self):
#         return self.name

# class Client(models.Model):
#     name = models.CharField(max_length=10)
#     Profession = models.CharField(max_length=15)
#     about= models.TextField(max_length=50)
#     image =models.ImageField(upload_to='posts/',default='default.jpg')
    
#     def __str__(self):
#         return self.name
