# Generated by Django 4.1.3 on 2023-01-06 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_appointment_hour_alter_appointment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarberHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.TimeField()),
            ],
        ),
    ]
