from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Double
from .forms import DoubleForm

class ListaDoubleView(ListView) :
    model = Double
    queryset = Double.objects.all().order_by('nome')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome= self.request.GET.get('nome') or None
        
        if filtro_nome:
          queryset = queryset.filter(nome__contains=filtro_nome).order_by('nome')         
        return queryset
    

class DoubleCreateView(CreateView):
    model = Double
    form_class = DoubleForm
    success_url = '/double/'

class DoubleUpdateView(UpdateView):
    model = Double
    form_class = DoubleForm
    success_url = '/double/'
    
class DoubleDeleteView(DeleteView):
    model = Double
    success_url = '/double/'

