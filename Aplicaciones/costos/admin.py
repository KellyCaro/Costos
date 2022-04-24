from django.contrib import admin

from Aplicaciones.costos.models import *



# Register your models here.



class RecetaIngredienteInline(admin.TabularInline):
    model = IngredientesReceta
    extra = 1
    autocomplete_fields = ['ingredientes']


class IngredientesAdmin(admin.ModelAdmin):
    inlines = (RecetaIngredienteInline,)
    search_fields = ('producto'),
    ordering = ['producto']
class RecetaAdmin(admin.ModelAdmin):
    inlines = [RecetaIngredienteInline,]
    list_display = (
        'nombre_receta',
        'cantidad_gramos',
        'costo',
        
        
    )
    #
    search_fields = ('nombre_receta',)
    list_filter = ('cantidad_gramos', 'ingredientes',)
    #
    filter_horizontal = ['ingredientes',]


admin.site.register(Ingredientes, IngredientesAdmin)
admin.site.register(Receta, RecetaAdmin)