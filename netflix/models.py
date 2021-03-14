from django.db import models


# Create your models here.

   
class Category(models.Model):
    name = models.CharField(max_length=100, null=True) 
    def __str__(self):
        return self.name

class Movies(models.Model):
    tittle = models.CharField(max_length=255)
    description = models.TextField()
    year = models.DateField()
    poster = models.ImageField(upload_to='movies/posters')
    video = models.FileField(upload_to='movies/video')
    categories = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.tittle
