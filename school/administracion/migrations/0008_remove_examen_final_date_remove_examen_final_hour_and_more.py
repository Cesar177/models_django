# Generated by Django 4.1.3 on 2022-11-30 06:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0007_alter_examen_final_table_alter_proyecto_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examen_final',
            name='date',
        ),
        migrations.RemoveField(
            model_name='examen_final',
            name='hour',
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='date',
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='hour',
        ),
        migrations.AddField(
            model_name='examen_final',
            name='hour_and_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 30, 6, 9, 42, 184397)),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='hour_and_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 30, 6, 9, 42, 184397)),
        ),
    ]
