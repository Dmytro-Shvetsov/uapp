# Generated by Django 2.2.4 on 2019-08-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0030_auto_20190830_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marker',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]