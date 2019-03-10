from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
from .models import Cuenta
import datetime
from django.http import HttpResponseRedirect
from .models import Cuenta,Usuario,CuentaBancaria,ServiciosBancarios,Transaccion
from django.utils import timezone
from random import randint
from django.template import RequestContext

# Create your views here.

#Codigo destinado a la carga de datos iniciales de la aplicación.
def carga_datos(request):

    Cuenta.objects.all().delete()
    Usuario.objects.all().delete()    
    CuentaBancaria.objects.all().delete()
    ServiciosBancarios.objects.all().delete()
    Transaccion.objects.all().delete()    
    


    CrearUsuarios('ggamboac','admin','Gustavo Adolfo','Gamboa Cruz','USAC',59377035)
    CrearUsuarios('jarango','admin','Julio Alberto','Arango Godinez','USAC',59377035)
    CrearUsuarios('jsierra','admin','Julia Argentina','Sierra Herrera','USAC',59377035)   
    CrearUsuarios('achinchilla','admin','Alba Janeth','Chinchilla','USAC',59377035)
    CrearUsuarios('dgarcia','admin','Daniel','Garcia','USAC',59377035)
 




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


    DatosCargados = CuentaBancaria.objects.count()
    return  HttpResponse("Carga de Datos: " + str(DatosCargados))  


#LOGIN.
#--
#Vista de login de la aplicación.
@csrf_exempt
def inicio(request):
    if request.session.get('usuario'):
        del request.session['usuario']
    template_name = 'inicio/page-login.html'
    return render(request, template_name)

#Vista de validación de login de la aplicación.
@csrf_exempt
def inicio_sesion(request):     
    if request.session.get('usuario') and request.session.get('password'):
        email       = request.session['usuario']
        password    = request.session['password']
        Logueado    = Usuario.objects.get(usuario=email,password=password)
        id_usuario  = Usuario.objects.get(usuario=email,password=password)
        request.session['usuario'] = email
        request.session['password'] = password
        CuentasBancarias    = CuentaBancaria.objects.all().filter(UsuarioPropietario=id_usuario)       
        #validacion si es usuario administrador
        if email == 'ggamboac':
            return  HttpResponseRedirect('/VerServiciosBancarios')       
        template_name       = 'usuario/home.html'
        return render(request, template_name,{'persona': Logueado, 'Cuentas': CuentasBancarias})        

    if request.method == 'POST':
        email       = request.POST.get("email")
        password    = request.POST.get("password")
        if email is "" or password is  "":
            return HttpResponseRedirect('/inicio')
        existe = Usuario.objects.filter(usuario=email,password=password).exists()
        if existe == True:
            Logueado        = Usuario.objects.get(usuario=email,password=password)
            id_usuario      = Usuario.objects.get(usuario=email,password=password)
            request.session['usuario']  = email
            request.session['password'] = password
            CuentasBancarias    = CuentaBancaria.objects.all().filter(UsuarioPropietario=id_usuario)            
            #Validacion usuario administrador
            if email == 'ggamboac':
                return  HttpResponseRedirect('/VerServiciosBancarios')
            template_name       = 'usuario/home.html'
            return render(request, template_name,{'persona': Logueado, 'Cuentas': CuentasBancarias})
        else:
            return HttpResponseRedirect('/inicio')
    else:
        return HttpResponseRedirect('/inicio')

def CrearUsuarios( usuario, password, nombre, apellido, direccion,telefono):
    usr8            = Usuario()
    usr8.id         = randint(1000000, 9000000)  
    usr8.usuario    = usuario
    usr8.password   = password
    usr8.Nombre     = nombre
    usr8.Apellido   = apellido
    usr8.direccion  = direccion
    usr8.telefono   = telefono
    usr8.Fecha_Creacion = timezone.now()    
    usr8.save()

    ct1 = CuentaBancaria()
    ct1.NumeroCuentaBancaria = randint(1000000, 9000000) 
    ct1.UsuarioPropietario = usr8
    ct1.saldo = 50
    ct1.FechaInicio = timezone.now()
    ct1.save()

    ct2 = CuentaBancaria()
    ct2.NumeroCuentaBancaria = randint(1000000, 9000000) 
    ct2.UsuarioPropietario = usr8
    ct2.saldo = 835
    ct2.FechaInicio = timezone.now()
    ct2.save()    

    return ct1

def CrearServicios():    
    srv1 = ServiciosBancarios()
    srv1.id = randint(1000000, 9000000)
    srv1.NumeroCuentaBancaria = CrearUsuarios('calusac','admin','Calusac','Centro Estudios','USAC',59377035)
    srv1.NombreServicio = 'Centro Estudio Lenguas'
    srv1.FechaInicio = timezone.now()
    srv1.save()


def CrearTransaccion(CuentaOrigen, CuentaDestino,DebitoCredito,Monto,Descripcion):

    existeOrigen = CuentaBancaria.objects.filter(NumeroCuentaBancaria=CuentaOrigen).exists()
    existeDestino = CuentaBancaria.objects.filter(NumeroCuentaBancaria=CuentaDestino).exists()

    if existeOrigen == True and existeDestino == True:
        trx = Transaccion()
        trx.id = randint(1000000, 9000000) 
        trx.CuentaOrigen = CuentaBancaria.objects.get(NumeroCuentaBancaria=CuentaOrigen)
        trx.CuentaDestino = CuentaBancaria.objects.get(NumeroCuentaBancaria=CuentaDestino)
        trx.Monto = Monto
        trx.FechaTransaccion = timezone.now()
        trx.DescripcionTransaccion = Descripcion
        trx.save()


#--

