from django.forms import ModelForm
from .models import Category


class UserForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

