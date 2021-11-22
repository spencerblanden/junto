from django.db import models
from datetime import date

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=250)
    description = models.TextField(max_length=250)
    tags = models.IntegerField()
    date = models.DateField('post date')