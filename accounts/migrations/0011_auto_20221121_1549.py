# Generated by Django 2.2.7 on 2022-11-21 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20221121_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='join_new',
            field=models.DateTimeField(default=True, verbose_name='وقت الانضمام'),
        ),
    ]