# Generated by Django 2.2.7 on 2022-11-22 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_auto_20221121_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='join_new',
            field=models.DateTimeField(blank=True, null=True, verbose_name='وقت الانضمام'),
        ),
    ]
