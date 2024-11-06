# Generated by Django 5.0.3 on 2024-11-06 20:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoEntrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='EstadoPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('cantidad_producto', models.IntegerField(blank=True, null=True)),
                ('precio_producto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estadopedido')),
            ],
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id_entrega', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_entrega', models.DateTimeField()),
                ('estado_entrega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.estadoentrega')),
                ('pedido', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.pedido')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=3, max_digits=10)),
                ('cantidad_disponible', models.IntegerField()),
                ('imagen_url', models.URLField(default='https://img.freepik.com/premium-vector/default-image-icon-vector-missing-picture-page-website-design-mobile-app-no-photo-available_87543-11093.jpg')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.marca')),
                ('tipo_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipoproducto')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialPrecios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='precios', to='core.producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=100)),
                ('comentario', models.CharField(max_length=100)),
                ('respuesta', models.CharField(blank=True, max_length=100, null=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_transaccion', models.DateTimeField(auto_now_add=True)),
                ('metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.metodopago')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pedido')),
            ],
        ),
    ]
