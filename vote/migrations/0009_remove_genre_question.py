# Generated by Django 4.0.3 on 2022-03-21 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0008_alter_serie_description_serie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='question',
        ),
    ]