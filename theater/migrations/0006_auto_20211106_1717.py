# Generated by Django 3.2.8 on 2021-11-06 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0005_personmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='personmodel',
            name='age',
            field=models.IntegerField(default=25),
        ),
        migrations.AddField(
            model_name='personmodel',
            name='country',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='theater.countrymodel'),
        ),
        migrations.AddField(
            model_name='personmodel',
            name='job',
            field=models.CharField(default='', max_length=100),
        ),
    ]
