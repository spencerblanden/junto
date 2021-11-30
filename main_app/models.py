from django.db import models
import datetime
from django import forms
# from django.forms import widgets, TextInput
from django.urls import reverse
from django.contrib.auth.models import User

TITLES = (
    ('J', 'Junto'),
    ('C', 'CSS'),
    ('H', 'HTML'),
)




# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=250)
    description = models.TextField(max_length=250)
    date = models.DateField(("Date"), default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_post')
    
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

  
    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_id': self.id})

    class Meta:
        ordering = ['-id']

class Category(models.Model):
    name = models.CharField(
        max_length=1,
        choices=TITLES,
        default=TITLES[0][0],
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


    def __str__(self):
        return (self.get_name_display())
