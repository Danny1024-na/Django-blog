from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.
'''
vaidation
html widget
field types
(dei Vorteiele von Verebung svon models)

'''

class Post(models.Model): #vererbung von models
    #eien Tabbele von models hat zwei Spalten title und content
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=10000)
    image =models.ImageField(upload_to='posts/',default='default.jpg')
    author = models.ForeignKey(User,related_name='Post_author',on_delete=models.CASCADE)
    tags =TaggableManager()

    #um die Name des Posts zu zeigen
    def __str__(self):
        return self.title
