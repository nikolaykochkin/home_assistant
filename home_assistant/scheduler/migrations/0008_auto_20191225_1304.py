# Generated by Django 3.0.1 on 2019-12-25 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0007_auto_20191225_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='friday',
            field=models.BooleanField(verbose_name='пт'),
        ),
        migrations.AlterField(
            model_name='task',
            name='monday',
            field=models.BooleanField(verbose_name='пн'),
        ),
        migrations.AlterField(
            model_name='task',
            name='saturday',
            field=models.BooleanField(verbose_name='сб'),
        ),
        migrations.AlterField(
            model_name='task',
            name='sunday',
            field=models.BooleanField(verbose_name='вс'),
        ),
        migrations.AlterField(
            model_name='task',
            name='thursday',
            field=models.BooleanField(verbose_name='чт'),
        ),
        migrations.AlterField(
            model_name='task',
            name='tuesday',
            field=models.BooleanField(verbose_name='вт'),
        ),
        migrations.AlterField(
            model_name='task',
            name='wednesday',
            field=models.BooleanField(verbose_name='ср'),
        ),
    ]
