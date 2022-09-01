from pickle import TRUE
from django.db import models
from django.forms import EmailField


class Tratamientos(models.Model):

    producto = models.CharField(max_length= 40)
    duracion =  models.CharField(max_length=40)
    fecha =   models.DateField()
    descripcion = models.CharField(max_length= 4000)  
    imagen = models.ImageField(upload_to='tratamientos', null=True, blank=True) 
 

    def __str__(self) -> str:
        return f'{self.producto} - {self.descripcion}'


class Unias(models.Model):

    producto = models.CharField(max_length= 40)
    duracion =  models.CharField(max_length=40)
    fecha =   models.DateField()
    descripcion = models.CharField(max_length= 4000)

    def __str__(self) -> str:
        return f'{self.producto} - {self.descripcion}'

class Corte(models.Model):

    persona_atendida = models.CharField(max_length= 40)
    fecha =   models.DateField()
    descripcion = models.CharField(max_length= 40)

    def __str__(self) -> str:
        return f'{self.persona}'

class Contacto(models.Model):

    nombre = models.CharField(max_length= 40)
    apellido = models.CharField(max_length= 40)
    email = models.EmailField()
    telefono = models.IntegerField()
    consulta = models.CharField(max_length= 40000)

    def __str__(self) -> str:
        return f'{self.consulta}'

 

class Experiencia(models.Model):

    nombre = models.CharField(max_length= 40)
    tratamiento = models.CharField(max_length= 40)
    fecha =   models.DateField()
    descripcion = models.CharField(max_length= 4000)
    imagen = models.ImageField(upload_to='experiencias', null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.nombre} - {self.tratamiento} - {self.fecha} -  {self.descripcion}'





