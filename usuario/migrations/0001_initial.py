# Generated by Django 4.1.7 on 2023-04-19 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_nombre', models.CharField(max_length=30, verbose_name='Primer Nombre')),
                ('segundo_nombre', models.CharField(max_length=30, verbose_name='Segundo Nombre')),
                ('primer_apellido', models.CharField(max_length=30, verbose_name='Primer Apellido')),
                ('segundo_apellido', models.CharField(max_length=30, verbose_name='Segundo Apellido')),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cedula'), ('TI', 'Tarjeta de Idetidad'), ('CE', 'Cédula de Extranjería')], max_length=2, verbose_name='Tipo de Documento')),
                ('documento', models.CharField(max_length=20, verbose_name='Documento')),
                ('telefono_contacto', models.CharField(max_length=10, verbose_name='Telefono de contacto')),
                ('telefono_personal', models.CharField(max_length=10, verbose_name='telefono personal')),
                ('rol', models.CharField(choices=[('E', 'Empleado'), ('P', 'Proveedor'), ('C', 'Cliente')], max_length=1, verbose_name='Rol')),
                ('correo', models.CharField(max_length=40, verbose_name='Correo')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo'), ('2', 'Condicionado')], default='1', max_length=1, verbose_name='Estado')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]
