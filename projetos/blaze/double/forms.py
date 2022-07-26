from dataclasses import fields
from tkinter import Widget
from django import forms  
from django.forms import fields, models 
from .models import Double
class DateInput(forms.DateInput):
    input_type = 'date'
class DoubleForm(forms.ModelForm):
    data_nascimento = forms.DateField(widget = DateInput)
    
    class Meta:
        model = Double
        fields = ['nome', 'data_nascimento', 'ativo']