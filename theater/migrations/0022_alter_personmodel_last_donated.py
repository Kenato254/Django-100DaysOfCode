# Generated by Django 3.2.8 on 2021-12-28 22:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0021_alter_personmodel_last_donated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personmodel',
            name='last_donated',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 24, 1, 17, 49, 764339)),
        ),
    ]
