# Generated by Django 3.1.6 on 2021-03-20 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
