# Generated by Django 3.2.12 on 2022-03-21 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0006_alter_serie_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='question',
            field=models.ManyToManyField(blank=True, to='vote.Question'),
        ),
        migrations.AddField(
            model_name='serie',
            name='acteur',
            field=models.ManyToManyField(blank=True, to='vote.Acteur'),
        ),
        migrations.AddField(
            model_name='serie',
            name='genre',
            field=models.ManyToManyField(blank=True, to='vote.Genre'),
        ),
        migrations.AddField(
            model_name='serie',
            name='plateform',
            field=models.ManyToManyField(blank=True, to='vote.Plateform'),
        ),
    ]