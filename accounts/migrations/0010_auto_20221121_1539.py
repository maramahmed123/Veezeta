# Generated by Django 2.2.7 on 2022-11-21 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_profile_join_us'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='join_us',
            new_name='join_new',
        ),
    ]