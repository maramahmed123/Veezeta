# Generated by Django 2.2.7 on 2022-11-22 23:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_auto_20221123_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fieldName',
        ),
        migrations.AddField(
            model_name='profile',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 23, 1, 10, 37, 651045)),
        ),
    ]
