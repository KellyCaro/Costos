from django.db import models
from sqlalchemy import null

# Create your models here.
class Ingredientes(models.Model):
    producto=models.CharField(max_length=50,primary_key=True)
    costo=models.IntegerField()
    valor=models.IntegerField()
    fecha_de_registro=models.DateField()
    proveedor=models.CharField(max_length=50)

    def __str__(self):
        txt='{0}'
        return txt.format(self.producto)


class Receta(models.Model):
    nombre_receta=models.CharField(max_length=50,primary_key=True)
    cantidad_gramos=models.IntegerField()
    costo=models.IntegerField()
    ingredientes = models.ManyToManyField(
        Ingredientes,
        through='IngredientesReceta',
        blank=True,
    )
    def __str__(self):
        txt='{0}'
        return txt.format(self.nombre_receta)
    def nombre(self):
        txt='{0}'
        return txt.format(self.nombre_receta)

class IngredientesReceta(models.Model):
    ingredientes=models.ForeignKey(
        Ingredientes,
        on_delete=models.CASCADE,
        blank=True, null=True
        )
    
    receta=models.ForeignKey(
        Receta,
        on_delete=models.CASCADE,
        blank=True, null=True
        )
    
    cantidad=models.IntegerField(default=0)
    valor=models.IntegerField(blank=False,default=None)

    class  meta:
        db_table='ingrediente_receta_cantidades'
        verbose_name= 'Ingrediente Receta'
        verbose_name_plural='Ingredientes Recetas'
    
    def __str__(self):
        return str(self.id) +'-'+self.receta.nombre()
