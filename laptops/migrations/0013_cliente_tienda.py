# Generated by Django 5.1 on 2024-08-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0012_remove_producto_cantidad_compra_detallecompra'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente_Tienda',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=100)),
                ('apellido_cliente', models.CharField(max_length=100)),
            ],
        ),
    ]
