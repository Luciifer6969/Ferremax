from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.IntegerField()

class EstadoPedido(models.Model):
    estado = models.CharField(max_length=20)

class Pedido(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True) 
    estado = models.ForeignKey(EstadoPedido, on_delete=models.CASCADE)  

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

class MetodoPago(models.Model):
    metodo = models.CharField(max_length=100)    

class Venta(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_transaccion = models.DateTimeField(auto_now_add=True)    

class EstadoEntrega(models.Model):
    estado = models.CharField(max_length=30)

class Entrega(models.Model):
    id_entrega = models.AutoField(primary_key=True)
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE)
    fecha_entrega = models.DateTimeField()
    estado_entrega = models.ForeignKey(EstadoEntrega, on_delete=models.CASCADE)