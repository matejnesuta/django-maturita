from django.core.validators import MinValueValidator
from django.db import models
import os
from django.dispatch import receiver


class Produkt(models.Model):
    nazev = models.CharField(blank=False, max_length=100, null=False, unique=True, verbose_name="Název")
    cena = models.DecimalField(blank=False, decimal_places=2, default=999.99, max_digits=12, null=False,
                               validators=[MinValueValidator(0.0)], verbose_name="Cena")
    vyrobce = models.ForeignKey('Vyrobce', null=False, on_delete=models.RESTRICT)
    popis = models.TextField
    foto = models.ImageField(upload_to='produkt/%Y/%m/%d/', blank=True, null=True, verbose_name="Fotka produktu")
    druh = models.ForeignKey('Druh', null=False, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"
        ordering = ["-cena", "nazev"]

    def __str__(self):
        return f"{self.druh}: {self.nazev}, {self.cena} KČ"


class Vyrobce(models.Model):
    nazev = models.CharField(blank=False, max_length=100, null=False, unique=True, verbose_name="Název")

    class Meta:
        verbose_name = "Výrobce"
        verbose_name_plural = "Výrobci"
        ordering = ["nazev"]

    def __str__(self):
        return self.nazev


class Druh(models.Model):
    nazev = models.CharField(blank=False, max_length=100, null=False, unique=True, verbose_name="Název")

    class Meta:
        verbose_name = "Druh zboží"
        verbose_name_plural = "Druhy zboží"
        ordering = ["nazev"]

    def __str__(self):
        return self.nazev


@receiver(models.signals.post_delete, sender=Produkt)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.foto:
        if os.path.isfile(instance.foto.path):
            os.remove(instance.foto.path)


@receiver(models.signals.pre_save, sender=Produkt)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = Produkt.objects.get(pk=instance.pk).foto
    except Produkt.DoesNotExist:
        return False

    new_file = instance.foto
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
