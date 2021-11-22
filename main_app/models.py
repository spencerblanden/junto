from django.db import models
from datetime import date
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=250)
    description = models.TextField(max_length=250)
    tags = models.IntegerField()
    date = models.DateField('post date')

    def __str__(self):
        return self.title

  
    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.id})