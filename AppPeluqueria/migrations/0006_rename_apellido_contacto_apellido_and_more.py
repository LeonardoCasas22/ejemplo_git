# Generated by Django 4.0.5 on 2022-07-17 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppPeluqueria', '0005_contacto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='Apellido',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='contacto',
            old_name='Consulta',
            new_name='consulta',
        ),
        migrations.RenameField(
            model_name='contacto',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contacto',
            old_name='Telefono',
            new_name='telefono',
        ),
    ]
