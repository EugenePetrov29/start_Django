# Generated by Django 3.1.6 on 2021-03-19 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0010_auto_20210319_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_img',
            field=models.ImageField(blank=True, null=True, upload_to='groups/images'),
        ),
    ]