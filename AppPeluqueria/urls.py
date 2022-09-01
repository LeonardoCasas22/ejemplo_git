from xml.etree.ElementInclude import include
from django.urls import path
from AppPeluqueria import views


urlpatterns = [
    
    path('', views.inicio, name = 'inicio'),
    path('alisados/' , views.tratamientos, name = 'alisados'),
    path('unias/' , views.unias, name = 'unias'),
    path('cortes/' , views.cortes, name = 'cortes'),
    path('nosotros/' , views.nosotros, name = 'nosotros'),
    path('experiencias/' , views.leer_experiencia, name = 'experiencias'),
    path('contacto/' , views.contacto, name = 'contacto'), 
    path('experiencia_form/' , views.experiencia_formulario, name = 'experiencia_form'),
    path('Detail/', views.ver_tratamientos, name='Detail'),
    path('Nuevo/', views.tratamientos_form, name='nuevo'), 

    
    path('tratamientos/list/', views.TratamientosList.as_view(), name = 'List'),
    #path(r'^nuevo$', views.TratamientosCreacion.as_view(), name='Create'),
    path(r'^editar/(?P<pk>\d+)$', views.TratamientosUpdate.as_view(), name='Update'),
    path(r'^borrar/(?P<pk>\d+)$', views.TratamientosDelete.as_view(), name='Delete'), 


    #unias 

    path('unias_form/', views.unias_form, name='unias_form'),
    



]


