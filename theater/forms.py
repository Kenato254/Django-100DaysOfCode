from django import forms

from theater.models import SearchModel

class SearchModelForm(forms.ModelForm):
    class Meta:
        model = SearchModel
        fields = "__all__"