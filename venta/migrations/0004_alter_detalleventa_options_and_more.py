# Generated by Django 4.2.1 on 2023-06-29 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0003_rename_detalle_venta_detalleventa'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detalleventa',
            options={'verbose_name_plural': 'detalleventas'},
        ),
        migrations.RenameField(
            model_name='detalleventa',
            old_name='valor_total',
            new_name='valortotal',
        ),
    ]
