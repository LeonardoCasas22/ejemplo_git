from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class tratamientos_formulario(forms.Form):

    producto = forms.CharField(max_length= 40)
    duracion =  forms.CharField(max_length=40)
    fecha =   forms.DateField()
    descripcion = forms.CharField(max_length= 4000)
    imagen = forms.ImageField()
    
    

class unias_formulario(forms.Form):

    producto = forms.CharField(max_length= 40)
    duracion =  forms.CharField(max_length=40)
    fecha =   forms.DateField()
    descripcion = forms.CharField(max_length= 40)

class corte_formulario(forms.Form):

    persona_atendida = forms.CharField(max_length= 40)
    fecha =   forms.DateField()
    descripcion = forms.CharField(max_length= 40)

class Contacto_formulario(forms.Form):

    nombre = forms.CharField(max_length= 40)
    apellido = forms.CharField(max_length= 40)
    email = forms.EmailField()
    telefono = forms.IntegerField()
    consulta = forms.CharField(max_length= 40000)


class Experiencia_formulario(forms.Form):

    nombre = forms.CharField(max_length= 40)
    tratamiento = forms.CharField(max_length= 40)
    fecha =   forms.DateField()
    descripcion = forms.CharField(max_length= 4000)
    imagen = forms.ImageField()



