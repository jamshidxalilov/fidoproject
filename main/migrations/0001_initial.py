# Generated by Django 4.2 on 2023-04-17 18:37

from django.db import migrations, models
import django.db.models.deletion
import fido.helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': "Bo'lim",
                'verbose_name_plural': "Bo'limlar",
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Ish turi',
                'verbose_name_plural': 'Ish turlari',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='staffs', verbose_name=fido.helpers.UploadTo)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('hour_salary', models.DecimalField(decimal_places=2, max_digits=19)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.department')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.job')),
            ],
            options={
                'verbose_name': 'Xodim',
                'verbose_name_plural': 'Xodimlar',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.SmallIntegerField(choices=[(1, 'Enter'), (0, 'Leave')])),
                ('date', models.DateField()),
                ('action_at', models.DateTimeField()),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='main.staff')),
            ],
        ),
    ]