# Generated by Django 3.2 on 2021-05-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hudebniny', '0003_auto_20210502_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='druh',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='druh/', verbose_name='Ilustrační foto'),
        ),
    ]
