# Generated by Django 2.2.7 on 2022-11-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20221110_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='سعر الكشف'),
        ),
    ]
