# Generated by Django 5.1 on 2024-08-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0016_remove_producto_tienda_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto_tienda',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
    ]
