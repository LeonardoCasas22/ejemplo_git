# Generated by Django 4.0.5 on 2022-07-15 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppPeluqueria', '0002_corte_persona_atendida'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Alisados',
            new_name='Tratamientos',
        ),
    ]
