# Generated by Django 4.2 on 2023-04-17 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'verbose_name': 'Ish davomati', 'verbose_name_plural': 'Ish davomati'},
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='date',
        ),
    ]
