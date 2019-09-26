# Generated by Django 2.2.5 on 2019-09-19 18:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='day_of_month',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(31)], verbose_name='день месяца'),
        ),
    ]