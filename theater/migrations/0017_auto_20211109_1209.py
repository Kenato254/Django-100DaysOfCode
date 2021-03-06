# Generated by Django 3.2.8 on 2021-11-09 09:09

import datetime
from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0016_auto_20211108_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='DogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('data', models.JSONField(default=django.db.models.expressions.Value('null'))),
            ],
        ),
        migrations.AddField(
            model_name='countrymodel',
            name='independent',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='personmodel',
            name='last_donated',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 4, 12, 9, 0, 812234)),
        ),
    ]
