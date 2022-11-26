# Generated by Django 2.2.7 on 2022-11-12 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20221110_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default=1, max_length=50, verbose_name='المحافظة'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='address_detail',
            field=models.CharField(default=1, max_length=50, verbose_name='العنوان بالتفصيل'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='doctor',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='دكتور؟'),
        ),
        migrations.AddField(
            model_name='profile',
            name='number_phone',
            field=models.CharField(default=1, max_length=50, verbose_name='رقم الهاتف'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='specialist_doctor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='متخصص في'),
        ),
        migrations.AddField(
            model_name='profile',
            name='subtitle',
            field=models.CharField(default=1, max_length=50, verbose_name='نبذة عنك'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='waiting_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='مدة الانتظار'),
        ),
        migrations.AddField(
            model_name='profile',
            name='working_hours',
            field=models.CharField(default=1, max_length=50, verbose_name='عدد ساعات العمل'),
            preserve_default=False,
        ),
    ]
