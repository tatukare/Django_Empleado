# Generated by Django 5.0.6 on 2024-05-15 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='cantidad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
