from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Double
from .forms import DoubleForm

class ListaDoubleView(ListView) :
    model = Double
    queryset = Double.objects.all().order_by('nome')

class DoubleCreateView(CreateView):
    model = Double
    form_class = DoubleForm
    success_url = '/double/'