# Generated by Django 3.1.6 on 2021-03-19 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0008_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='picture',
            field=models.ImageField(blank=True, height_field='250', null=True, upload_to='images', width_field='200'),
        ),
    ]
