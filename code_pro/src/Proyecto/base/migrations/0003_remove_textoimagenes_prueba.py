# Generated by Django 4.2.5 on 2023-11-02 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_textoimagenes_prueba'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='textoimagenes',
            name='prueba',
        ),
    ]