from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http.response import HttpResponseNotAllowed
from django.http import HttpResponse, Http404

from .models import Double, Contato
from .forms import DoubleForm, ContatoForm

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


def Contatos(request, pk_double):    
    contato = Contato.objects.filter(double=pk_double)
    return render(request, 'contato/contato_list.html', {'contato': contato, 'pk_double': pk_double})


def contato_novo(request, pk_double):
    form = ContatoForm()
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save(commit=False)
            contato.double_id = pk_double
            contato.save()
            return redirect(reverse('double.contatos', args=[pk_double]))

    return render(request, 'contato/contato_form.html', {'form': form})


def contato_editar(request, pk_double, pk):
    contato = get_object_or_404(Contato, pk=pk)
    form = ContatoForm(instance=contato)
    if request.method == "POST":
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return redirect(reverse('double.contatos', args=[pk_double]))

    return render(request, 'contato/contato_form.html', {'form': form})


def contato_remover(request, pk_double, pk):
    contato = get_object_or_404(Contato, pk=pk)
    contato.delete()
    return redirect(reverse('double.contatos', args=[pk_double]))
