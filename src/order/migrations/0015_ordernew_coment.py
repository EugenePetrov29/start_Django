# Generated by Django 3.1.6 on 2021-03-22 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20210322_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordernew',
            name='coment',
            field=models.TextField(default=None, null=True, verbose_name='Комментарии'),
        ),
    ]
