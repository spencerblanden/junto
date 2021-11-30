from django.forms import ModelForm, TextInput, widgets
from django import forms
from .models import Category, Post


class UserForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)