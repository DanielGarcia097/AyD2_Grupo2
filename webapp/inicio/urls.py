from django.conf.urls import url
from . import views


urlpatterns = [
    
    #URL Login

    url('inicio/$', views.manual),
    url('inicio/login$', views.inicio_sesion),    

]
