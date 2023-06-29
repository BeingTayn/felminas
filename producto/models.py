from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Producto(models.Model):
    nombre= models.CharField(max_length=45, verbose_name="Nombre")
    descripcion= models.CharField(max_length=60, verbose_name="Descripcion")
    marca= models.CharField(max_length=30, verbose_name="Marca")

    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
        CONDICIONADO='2',_("Condicionado")
    estado=models.CharField(max_length=2,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")

    
class Stock(models.Model):
    cantidad= models.CharField(max_length=40, verbose_name="cantidad")

    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")

    class Meta:
        verbose_name_plural = "stocks" 