# Generated by Django 2.0 on 2018-04-16 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='lastName',
            field=models.CharField(blank=True, max_length=256, verbose_name='lastName'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='userName',
            field=models.CharField(blank=True, max_length=256, verbose_name='userName'),
        ),
    ]
