from django.db import models

# Create your models here.
class Cuenta(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    saldo = models.IntegerField()
    def __str__(self):
        return self.usuario


class Usuario(models.Model):
    usuario = models.CharField(primary_key=True,max_length=30)    
    ##id = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)        
    password = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.IntegerField()        
    Fecha_Creacion = models.DateField()
    def __str__(self):
        return self.usuario

class CuentaBancaria(models.Model):
    NumeroCuentaBancaria = models.IntegerField(primary_key=True)
    UsuarioPropietario = models.ForeignKey(Usuario,related_name='CuentaBancariaUsuario', on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=8, decimal_places=4)
    def __str__(self):
        return self.UsuarioPropietario

class ServiciosBancarios(models.Model):
    NumeroCuentaBancaria = models.ForeignKey(CuentaBancaria, on_delete=models.CASCADE)
    NombreServicio = models.CharField(max_length=30)
    def __str__(self):
        return self.NombreServicio


class Transaccion(models.Model):
    CuentaOrigen = models.ForeignKey(CuentaBancaria,related_name='OrigenCuenta', on_delete=models.CASCADE)
    CuentaDestino = models.ForeignKey(CuentaBancaria,related_name='DestinoCuenta', on_delete=models.CASCADE)
    DebitoCredito = models.IntegerField() ##  0 = Debito (Se agrega a cuenta) | 1 = Credito (Se quita a cuenta)
    Monto = models.DecimalField(max_digits=8, decimal_places=4)
    FechaTransaccion = models.DateField()
    def __str__(self):
        return self.id