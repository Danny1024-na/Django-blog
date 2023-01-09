from django.db import models

# Create your models here.
class Post(models.Model): #vererbung von models
    #eien Tabbele von models hat zwei Spalten title und content
    title = models.CharField(max_length=20)
    content = models.TextField(max_length=10000)
    image =models.ImageField(upload_to='posts/',default='default.jpg')
    #author = models.ForeignKey(User,related_name='Post_author',on_delete=models.CASCADE)
    # tags =TaggableManager()

    def __str__(self):
        return self.title
