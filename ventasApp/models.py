from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.db import transaction
from django.db.models import F

# Create your models here.
class Categoria(models.Model):
    descripcion=models.CharField(max_length=30)
    estado=models.BooleanField()
    
    def __str__(self):
        return self.descripcion

class Unidad(models.Model):
    descripcion=models.CharField(max_length=30)
    estado=models.BooleanField()
    def __str__(self):
        return self.descripcion

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    documento = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    direccion = models.TextField()

    def clean(self):
        super().clean()
        if len(self.documento) != 8 or not self.documento.isdigit():
            raise ValidationError("El documento debe contener exactamente 8 dígitos.")

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
    class Meta:
        ordering = ['apellidos', 'nombre']
        
class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.descripcion
        
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='ventas')
    fecha_venta = models.DateField()
    documento = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])

    @property
    def igv(self):
        return self.total * Decimal('0.18')

    @property
    def subtotal(self):
        return self.total - self.igv

    def __str__(self):
        return f'Venta {self.id} - {self.fecha_venta}'

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        with transaction.atomic():
            producto_actual = Producto.objects.select_for_update().get(pk=self.producto.pk)
            if producto_actual.stock < self.cantidad:
                raise ValueError(f"No hay suficiente stock para {producto_actual.descripcion}. Stock disponible: {producto_actual.stock}, solicitado: {self.cantidad}")
            producto_actual.stock = F('stock') - self.cantidad
            producto_actual.save(update_fields=['stock'])
            super().save(*args, **kwargs)

    def __str__(self):
        return f'Detalle Venta {self.id} - {self.producto.descripcion}'

    def __str__(self):
        return f'Detalle Venta {self.id} - {self.producto.descripcion}'
