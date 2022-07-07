from dataclasses import fields
from django import forms   
from django.forms import fields, models
from .models import Double

class DoubleForm(forms.ModelForm):
    class Meta:
        model = Double
        fields = ['nome', 'data_nascimento', 'ativo']