# Generated by Django 3.2.8 on 2021-11-08 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0013_auto_20211108_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personmodel',
            name='last_donated',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 20, 33, 19, 511159)),
        ),
        migrations.AlterField(
            model_name='personmodel',
            name='marital_status',
            field=models.JSONField(default={'Gender': 'None', 'MaritalStatus': 'Single'}),
        ),
    ]
