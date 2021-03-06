# Generated by Django 2.2.5 on 2019-09-19 19:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_auto_20190919_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='day_of_month',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(31)], verbose_name='день месяца'),
        ),
        migrations.AlterField(
            model_name='task',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата окончания'),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_time',
            field=models.TimeField(blank=True, null=True, verbose_name='время начала'),
        ),
    ]
