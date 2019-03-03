from django.conf.urls import url
from inicio.views import carga_datos
from inicio.views import inicio
from transacciones.views import inicio_transacciones,RealizarTransacciones,HistorialTransacciones,VerHistorialCuenta
#from transacciones import views



urlpatterns = [    
    #URL Login
    url('carga_datos/$', carga_datos),
    url('inicio/$', inicio),
    url('transacciones/$', inicio_transacciones),
    url('RealizarTransaccion/$', RealizarTransacciones),
    url('HistorialTransacciones/$', HistorialTransacciones),
    url('VerHistorialCuenta/$', VerHistorialCuenta),  
  
]
