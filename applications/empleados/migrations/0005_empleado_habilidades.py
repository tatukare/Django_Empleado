# Generated by Django 5.0.6 on 2024-05-16 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0004_habilidades_alter_empleado_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='empleados.habilidades'),
        ),
    ]