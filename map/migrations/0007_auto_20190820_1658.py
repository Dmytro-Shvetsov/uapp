# Generated by Django 2.2.4 on 2019-08-20 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_auto_20190820_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='marker',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True),
        ),
    ]
