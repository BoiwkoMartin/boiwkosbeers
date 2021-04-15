from django.contrib import admin
from cerveceria.models import Cerveza, Marca
# Register your models here.

class MarcaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'telefono', 'direccion', 'email')
	search_fields = ('nombre')

class CervezaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'tipo', 'precio', 'cantidad')
	


admin.site.register(Cerveza)
admin.site.register(Marca)