from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


class IndexView(ListView):
    model = Druh
    context_object_name = 'druh_list'
    template_name = 'index.html'


class ProduktView(ListView):
    model = Produkt
    context_object_name = 'produkt_list'
    template_name = 'produkty.html'

    def get_context_data(self, **kwargs):
        context = super(ProduktView, self).get_context_data(**kwargs)
        context['nadpis'] = "Všechny produkty"
        return context


class FilteredProduktView(ProduktView):

    def get_queryset(self):
        return Produkt.objects.filter(druh_id=self.kwargs['id'])

    def get_context_data(self, **kwargs):
        context = super(ProduktView, self).get_context_data(**kwargs)
        context['nadpis'] = Druh.objects.get(id=self.kwargs['id']).nazev
        return context


class ProduktDetailView(DetailView):
    model = Produkt
    context_object_name = 'produkt'
    template_name = 'detail.html'


