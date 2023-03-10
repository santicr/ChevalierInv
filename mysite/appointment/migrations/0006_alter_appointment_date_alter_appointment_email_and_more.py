# Generated by Django 4.1.3 on 2023-01-08 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_delete_barberhour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='hour',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='lastname1',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='lastname2',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
