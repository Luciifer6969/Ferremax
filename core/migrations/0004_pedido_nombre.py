# Generated by Django 5.0.3 on 2024-05-03 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_producto_imagen_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='nombre',
            field=models.CharField(default='nombrePrueba', max_length=70),
            preserve_default=False,
        ),
    ]
