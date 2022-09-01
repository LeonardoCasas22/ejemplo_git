from django.contrib import admin

from AppPeluqueria.models import Contacto, Corte, Experiencia, Tratamientos, Unias

# Register your models here.

admin.site.register(Tratamientos)
admin.site.register(Unias)
admin.site.register(Corte)
admin.site.register(Contacto)
admin.site.register(Experiencia)


