# Generated by Django 4.0.1 on 2022-07-29 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmueblesListApp', '0008_alter_edificacion_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificacion',
            name='avg_calificacion',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='edificacion',
            name='number_Calificacion',
            field=models.FloatField(default=0),
        ),
    ]
