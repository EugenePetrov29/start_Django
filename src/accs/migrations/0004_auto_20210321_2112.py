# Generated by Django 3.1.6 on 2021-03-21 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accs', '0003_auto_20210320_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
