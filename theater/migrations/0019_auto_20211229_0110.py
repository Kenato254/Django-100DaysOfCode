# Generated by Django 3.2.8 on 2021-12-28 22:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0018_auto_20211109_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personmodel',
            name='last_donated',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 24, 1, 10, 43, 887670)),
        ),
        migrations.AlterField(
            model_name='personmodel',
            name='marital_status',
            field=models.JSONField(verbose_name='{"MaritalStatus": "Single"}'),
        ),
    ]