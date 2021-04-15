from django.db import models

# Create your models here.
class Marca(models.Model):
	nombre = models.CharField(max_length = 50, default="Boiwko's")
	telefono = models.CharField(max_length = 15)
	direccion = models.CharField(max_length=60)
	email = models.EmailField(blank=True, verbose_name='correo electrónico')

	class Meta:
		verbose_name_plural = 'Marcas'

	def __str__(self):
		return self.nombre


class Cerveza(models.Model):
	nombre = models.CharField(max_length = 50, default="Boiwko's")
	tipo = models.CharField(max_length=600)
	marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
	cantidad = models.IntegerField()
	precio = models.FloatField()
	imagen = models.ImageField(upload_to='capturas')
	descripcion = models.CharField(max_length=400, blank=True)

	class Meta:
		ordering = ["marca", "tipo"]
		verbose_name_plural = 'Cervezas'
	def __str__(self):
		return self.nombre