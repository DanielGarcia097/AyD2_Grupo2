from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
from .models import Cuenta
import datetime
from django.http import HttpResponseRedirect


# Create your views here.


def carga_datos(request):
    n = Cuenta()
    n.id = 1
    n.usuario = 'gamgustavo'
    n.password = 'password'
    n.saldo = 512
    n.save()

    n2 = Cuenta()
    n2.id = 2
    n2.usuario = 'danielgarcia'
    n2.password = 'password'
    n2.saldo = 850
    n2.save()    

    n3 = Cuenta()
    n3.id = 3
    n3.usuario = 'albachinchilla'
    n3.password = 'password'
    n3.saldo = 796
    n3.save()    


    n4 = Cuenta()
    n4.id = 4
    n4.usuario = 'julioarango'
    n4.password = 'password'
    n4.saldo = 7896
    n4.save()    

    n5 = Cuenta()
    n5.id = 5
    n5.usuario = 'juliaargentina'
    n5.password = 'password'
    n5.saldo = 1256
    n5.save()

    DatosCargados = Cuenta.objects.count()
    return  HttpResponse("Carga de Datos: " + str(DatosCargados))  

@csrf_exempt
def inicio(request):
    template_name = 'inicio/page-login.html'
    return render(request, template_name)



@csrf_exempt
def inicio_sesion(request):
    if request.method == 'POST':
        email  = request.POST.get("email")
        password  = request.POST.get("password")
        if email is "" or password is  "":
            return HttpResponseRedirect('/inicio')
        existe = Cuenta.objects.filter(usuario=email,password=password).exists()
        if existe == True:
            Logueado = Cuenta.objects.get(usuario=email,password=password)
            template_name = 'inicio/estado_cuenta.html'
            return render(request, template_name,{'persona': Logueado})
        else:
            return HttpResponseRedirect('/inicio')

    else:
        return HttpResponseRedirect('/inicio')


