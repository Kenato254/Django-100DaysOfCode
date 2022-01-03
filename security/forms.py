from django import forms
from .models import Feedback, UserInput

class UserInputModelForm(forms.ModelForm):
    class Meta:
        model = UserInput
        fields = '__all__'

class FeedbackModelForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name',)