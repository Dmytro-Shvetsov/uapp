# Generated by Django 2.2.4 on 2019-08-26 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0010_auto_20190822_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='long_description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='marker',
            name='short_description',
            field=models.TextField(max_length=200),
        ),
    ]
