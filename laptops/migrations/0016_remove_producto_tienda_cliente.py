# Generated by Django 5.1 on 2024-08-17 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0015_producto_tienda'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto_tienda',
            name='cliente',
        ),
    ]
