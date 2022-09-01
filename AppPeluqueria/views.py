from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppPeluqueria.models import Contacto, Experiencia, Tratamientos, Unias, Corte
from AppPeluqueria.forms import Experiencia_formulario, tratamientos_formulario, unias_formulario, corte_formulario, Contacto_formulario

from django.views.generic import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy 

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


def inicio(request):
    return render(request, 'AppPeluqueria/inicio.html')

def tratamientos(request):
    return render(request, 'AppPeluqueria/unias.html' )


def unias(request):
    return render(request, 'AppPeluqueria/unias.html' )

def cortes(request):
    return render(request, 'AppPeluqueria/cortes.html' )

def nosotros(request):
    return render(request, 'AppPeluqueria/nosotros.html' )


def leer_experiencia(request):

    experiencia = Experiencia.objects.all()
    
    contexto = {'expe': experiencia } 

    return render(request, 'AppPeluqueria/experiencias.html', contexto) 


def experiencia_formulario(request):

    if request.method == "POST": 

        elformulario = Experiencia_formulario(request.POST, request.FILES)

        if elformulario.is_valid(): 
        
            informacion = elformulario.cleaned_data

            contacto = Experiencia(nombre = informacion['nombre'], tratamiento = informacion['tratamiento'], fecha = informacion['fecha'], descripcion = informacion['descripcion' ],  imagen = informacion['imagen' ]) 

            contacto.save()
    
            return render(request, 'AppPeluqueria/inicio.html')    
    
    else:
         elformulario = Experiencia_formulario() 
    
    return render(request, 'AppPeluqueria/experiencias_formulario.html', {'form': elformulario}) 



def contacto(request):  
    
    if request.method == "POST": 

        elformulario = Contacto_formulario(request.POST)

        if elformulario.is_valid(): 
        
            informacion = elformulario.cleaned_data

            contacto = Contacto(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'], telefono = informacion['telefono'], consulta = informacion['consulta']) 

            contacto.save()
    
            return render(request, 'AppPeluqueria/gracias_contacto.html')    
    
    else:
         elformulario = Contacto_formulario() 
    
    return render(request, 'AppPeluqueria/contacto.html', {'form': elformulario}) 




def ver_tratamientos(request):

    tratamientos = Tratamientos.objects.filter() 
    
    contexto = {'tratamientos': tratamientos }

    return render(request, 'AppPeluqueria/tratamientos_detalle.html', contexto) 

class TratamientosList(ListView):

    model = Tratamientos
    template_name = 'AppPeluqueria/tratamientos_list.html' 

#class TratamientosDetalle(DetailView):

    #model = Tratamientos
    #template_name = 'AppPeluqueria/tratamientos_detalle.html' 


class TratamientosCreacion(CreateView):

    model = Tratamientos
    success_url = '/AppPeluqueria/tratamientos/list'
    fields = ['producto', 'duracion','fecha','descripcion','imagen'] 

class TratamientosUpdate(UpdateView):

    model = Tratamientos
    success_url = '/AppPeluqueria/tratamientos/list'
    fields = ['producto', 'duracion','fecha','descripcion', 'imagen']

class TratamientosDelete(DeleteView):
    
    model = Tratamientos
    success_url = '/AppPeluqueria/tratamientos/list'


def tratamientos_form(request):

    if request.method == "POST": 

        elformulario = tratamientos_formulario(request.POST, request.FILES)

        if elformulario.is_valid(): 
        
            informacion = elformulario.cleaned_data

            contacto = Tratamientos(producto = informacion['producto'], duracion = informacion['duracion'], fecha = informacion['fecha'], descripcion = informacion['descripcion' ],  imagen = informacion['imagen' ]) 

            contacto.save()
    
            return render(request, 'AppPeluqueria/inicio.html')    
    
    else:
         elformulario = tratamientos_formulario() 
    
    return render(request, 'AppPeluqueria/tratamientos_form.html', {'form': elformulario})


#Unias----

def unias_form(request):

    if request.method == "POST": 

        elformulario = unias_formulario(request.POST, request.FILES)

        if elformulario.is_valid(): 
        
            informacion = elformulario.cleaned_data

            contacto = Unias(producto = informacion['producto'], duracion = informacion['duracion'], fecha = informacion['fecha'], descripcion = informacion['descripcion' ])

            contacto.save()
    
            return render(request, 'AppPeluqueria/unias.html')    
    
    else:
         elformulario = unias_formulario() 
    
    return render(request, 'AppPeluqueria/unias_form.html', {'form': elformulario}) 

