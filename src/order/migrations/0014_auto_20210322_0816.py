# Generated by Django 3.1.6 on 2021-03-22 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0013_auto_20210322_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordernew',
            name='address',
            field=models.CharField(max_length=200, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='ordernew',
            name='phone',
            field=models.IntegerField(default=375, null=True, verbose_name='Номер телефона'),
        ),
    ]
