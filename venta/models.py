from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class venta(models.Model):
    fecha= models.DateField(verbose_name="Fecha", help_text="MM/DD/AAAA")
    
    class Estado(models.TextChoices):
        ACTIVA='1',_("Activa")
        INACTIVA='0',_("Inactiva")
            
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVA,verbose_name="Estado")
            
    class Meta:
        verbose_name_plural= "ventas"
        
class Detalleventa(models.Model):
    valortotal= models.CharField(max_length=45, verbose_name="valor total")

    class Estado(models.TextChoices):
        ACTIVO='1',_("Activo")
        INACTIVO='0',_("Inactivo")
    estado=models.CharField(max_length=1,choices=Estado.choices,default=Estado.ACTIVO,verbose_name="Estado")

    class Meta:
        verbose_name_plural = "detalleventas" 