# Generated by Django 3.2.8 on 2021-11-04 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0002_citymodel_countrymodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citymodel',
            old_name='city',
            new_name='country',
        ),
    ]
