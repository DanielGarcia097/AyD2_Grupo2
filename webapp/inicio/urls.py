from django.conf.urls import url
from . import views


urlpatterns = [
    
    #URL Login

    url('inicio_sesion/$', views.inicio_sesion),
    url('carga_datos/$', views.carga_datos),    
    url('inicio/$', views.inicio),    
]
