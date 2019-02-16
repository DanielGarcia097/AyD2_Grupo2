from django.db import models

# Create your models here.
class Cuenta(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    saldo = models.IntegerField()
    def __str__(self):
        return self.usuario