# Generated by Django 2.2.7 on 2022-11-10 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='profile', verbose_name='الصورة الشخصية'),
        ),
    ]
