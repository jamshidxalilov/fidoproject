# Generated by Django 4.2 on 2023-04-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_attendance_hours'),
    ]

    operations = [
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.SmallIntegerField(choices=[(1, 'Yanvar'), (2, 'Fevral'), (3, 'Mart'), (4, 'Aprel'), (5, 'May'), (6, 'Iyun'), (7, 'Iyul'), (8, 'Avgust'), (9, 'Sentyabr'), (10, 'Oktyabr'), (11, 'Noyabr'), (12, 'Dekabr')], default=100)),
            ],
        ),
    ]