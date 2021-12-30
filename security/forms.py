from django import forms
from django.forms import fields

from .models import UserInput

class UserInputModelForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = '__all__'