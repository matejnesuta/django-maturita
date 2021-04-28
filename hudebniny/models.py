from django.db import models


# Create your models here.
class Produkt(models.Model):
    nazev = models.CharField(verbose_name="Název", null=False, max_length=100)

    class Meta:
        verbose_name_plural = "Produkty"
