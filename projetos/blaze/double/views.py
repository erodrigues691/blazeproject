from django.shortcuts import render
from django.views.generic import ListView
from .models import Double

class ListaDoubleView(ListView) :
    model = Double
    queryset = Double.objects.all().order_by('nome')
