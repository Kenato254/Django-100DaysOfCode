from django import forms
from django.core.mail import send_mail
from .models import Author, BookModel, User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password")

class BookModelForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = (
            'name', 
            'pub_date',
        )

class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "class": "text-input-props",
        "placeholder": "Your name",
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "text-input-props",
        "placeholder": "Your email address"
    }))
    body = forms.CharField(widget=forms.Textarea(attrs={
        "class": "text-area-props",
        "placeholder": "Your message",
    }))

class MessageMeForm(forms.Form):
        body = forms.CharField(widget=forms.Textarea(attrs={
        "rows":3,
        "cols":6,
        "class": "text-area-props",
        "placeholder": "Leave a message",
    }))