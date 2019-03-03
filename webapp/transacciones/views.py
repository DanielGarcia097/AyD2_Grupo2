from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from inicio.models import Usuario, CuentaBancaria,Transaccion
from django.utils import timezone
from random import randint
# Create your views here.

def inicio_transacciones(request):
    if request.session.get('usuario'):
        email       = request.session['usuario']
        Logueado    = Usuario.objects.get(usuario=email)
        id_usuario  = Usuario.objects.get(usuario=email)
        CuentasBancarias    = CuentaBancaria.objects.all().filter(UsuarioPropietario=id_usuario)            
        template_name       = 'transacciones/home.html'
        return render(request, template_name,{'persona': Logueado, 'Cuentas': CuentasBancarias})   
    else:
        return  HttpResponseRedirect('/inicio')        

def RealizarTransacciones(request):
    if request.session.get('usuario'):
        email       = request.session['usuario']
        Logueado    = Usuario.objects.get(usuario=email)
        id_usuario  = Usuario.objects.get(usuario=email)
        CuentasBancarias = CuentaBancaria.objects.all().filter(UsuarioPropietario=id_usuario)            
        if request.method == 'POST':
            CuentaOrigen    = request.POST.get("CuentaOrigen")
            CuentaDestino   = request.POST.get("CuentaDestino")
            Descripcion     = request.POST.get("Descripcion")
            Password        = request.POST.get("password")
            Monto        = request.POST.get("MontoTransaccion")
            MontoTransaccion= request.POST.get("MontoTransaccion")

            ##Para realizar una transaccion se realiza en dos operaciones
            ## 1- Se saca de la Cuenta Origen   -> En DebitoCredito se pone 0
            ## 2- Se carga en cuenta destino    -> En DebitoCredito se pone 5
            ## Esto para facilitar las consultas
            CrearTransaccion(CuentaOrigen,CuentaDestino,0,Monto,Descripcion)
            CrearTransaccion(CuentaDestino,CuentaOrigen,5,Monto,Descripcion)
        return HttpResponseRedirect('/usuario/inicio_sesion/')
    else:
        return  HttpResponseRedirect('/inicio') 

def VerHistorialCuenta(request):
    if request.method == 'POST':
        cuenta        = request.POST.get("cuenta")
        if request.session.get('usuario'):
            username        = request.session['usuario']
            id_usuario      = Usuario.objects.get(usuario=username)
            Cuenta          = CuentaBancaria.objects.all().filter(NumeroCuentaBancaria=cuenta).last()
            Transacciones   = Transaccion.objects.all().filter(CuentaOrigen=Cuenta)
            template_name   = 'transacciones/HistorialTransacciones.html'
            return render(request, template_name,{'persona': id_usuario, 'Transacciones': Transacciones})   
        
        else:
            return  HttpResponseRedirect('/inicio')
    else:
        return  HttpResponseRedirect('/inicio')

def HistorialTransacciones(request):
    if request.session.get('usuario'):
        username        = request.session['usuario']
        id_usuario      = Usuario.objects.get(usuario=username)
        Cuenta          = CuentaBancaria.objects.all().filter(UsuarioPropietario=id_usuario).last()
        Transacciones   = Transaccion.objects.all().filter(CuentaOrigen=Cuenta)
        template_name   = 'transacciones/HistorialTransacciones.html'
        return render(request, template_name,{'persona': id_usuario, 'Transacciones': Transacciones})   
    
    else:
        return  HttpResponseRedirect('/inicio')
    

def CrearTransaccion(CuentaOrigen,CuentaDestino,DebitoCredito,Monto,Descripcion):
    trx = Transaccion()
    trx.id              = randint(1000000, 9000000)
    trx.CuentaOrigen    = CuentaBancaria.objects.get(NumeroCuentaBancaria=CuentaOrigen)
    trx.CuentaDestino   = CuentaBancaria.objects.get(NumeroCuentaBancaria=CuentaDestino)
    trx.DebitoCredito   = DebitoCredito
    trx.Monto           = Monto
    trx.Decripcion      = Descripcion
    trx.FechaTransaccion=timezone.now()
    trx.save()
    return trx


