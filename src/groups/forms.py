from django import forms
from django.db.models import fields
from . import models

class SearchForm(forms.Form):
    query = forms.CharField(label="")
    fields = forms.CharField(widget=forms.HiddenInput)
    direction = forms.CharField(widget=forms.HiddenInput)  