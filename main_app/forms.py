from django.forms import ModelForm, TextInput, widgets
from django import forms
from .models import Category, Post


class UserForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

# class PostForm(forms.ModelForm):
#     class Meta: 
#         model = Post
#         fields = ('title', 'content', 'description')

#     widget = {
#         'title': forms.TextInput(attrs={'class': 'formFields'}),
#         'content': forms.TextInput(attrs={'class': 'formFields'}),
#         'description': forms.TextInput(attrs={'class': 'formFields'}),
#     }