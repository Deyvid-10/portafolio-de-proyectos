# Generated by Django 4.2.5 on 2023-11-02 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_textoimagenes_prueba'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textoimagenes',
            name='imagenes',
        ),
    ]
