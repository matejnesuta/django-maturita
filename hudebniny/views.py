from django.shortcuts import render
from .models import *
from django.views.generic import ListView


class IndexView(ListView):
    model = Druh
    context_object_name = 'druh_list'
    template_name = 'index.html'


class ProduktView(ListView):
    model = Produkt
    context_object_name = 'produkt_list'
    template_name = 'produkty.html'
    context = {
        'nadpis': 'Produkty',
    }


class FilteredProduktView(ProduktView):

    def get_queryset(self):
        return Produkt.objects.filter(druh_id=self.kwargs['id'])
