# Generated by Django 3.1.6 on 2021-03-22 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0016_auto_20210322_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='book_img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
