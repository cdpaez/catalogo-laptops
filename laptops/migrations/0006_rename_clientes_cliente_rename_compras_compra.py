# Generated by Django 5.1 on 2024-08-13 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0005_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clientes',
            new_name='Cliente',
        ),
        migrations.RenameModel(
            old_name='Compras',
            new_name='Compra',
        ),
    ]
