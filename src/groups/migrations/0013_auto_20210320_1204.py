# Generated by Django 3.1.6 on 2021-03-20 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0012_auto_20210319_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]