from django.contrib import admin
from .models import *

models = [Druh, Produkt, Vyrobce]
admin.site.register(models)

