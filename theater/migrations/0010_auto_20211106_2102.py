# Generated by Django 3.2.8 on 2021-11-06 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0009_auto_20211106_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personmodel',
            name='can_donate_on',
        ),
        migrations.AlterField(
            model_name='personmodel',
            name='last_donated',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 1, 21, 2, 55, 582086)),
        ),
    ]
