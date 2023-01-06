# Generated by Django 4.1.3 on 2023-01-03 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_appointment_barber_appointment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='hour',
            field=models.TimeField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(),
        ),
    ]