# Generated by Django 4.2.1 on 2023-06-29 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(max_length=40, verbose_name='cantidad')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
            options={
                'verbose_name_plural': 'stocks',
            },
        ),
    ]
