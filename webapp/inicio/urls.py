from django.conf.urls import url
from . import views


urlpatterns = [
    
    #URL Login
    url('carga_datos/$', views.carga_datos),    
    url('inicio/$', views.inicio),    
]
