# Generated by Django 4.0.3 on 2022-03-29 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inmueblesListApp', '0002_empresa_inmueble_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='empresa',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inmueblesListApp.empresa'),
            preserve_default=False,
        ),
    ]
