# Generated by Django 4.2 on 2023-04-17 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_attendance_options_remove_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='action_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]