from django.db import models
from producto.models import Stock

from django.utils.translation import gettext_lazy as _
# Create your models here.
class Compra(models.Model):
    fecha= models.DateField(verbose_name="Fecha", help_text="MM/DD/AAAA")

    class Estado(models.TextChoices):
        ACTIVA='1',_("Activa")
        INACTIVA='0',_("Inactiva")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVA,verbose_name="Estado")
  
class Meta:
    verbose_name_plural="compras"

class Detallecompra(models.Model):
    precio= models.CharField(max_length=45, verbose_name="precio")
    cantidad= models.CharField(max_length=45, verbose_name="cantidad")
    valortotal= models.CharField(max_length=45, verbose_name="valor total")

    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")

    class Meta:
        verbose_name_plural = "detallecompras" 


