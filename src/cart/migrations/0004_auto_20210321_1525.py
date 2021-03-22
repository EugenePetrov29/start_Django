# Generated by Django 3.1.6 on 2021-03-21 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0015_auto_20210321_1525'),
        ('cart', '0003_auto_20210321_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookincart',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='groups.book', verbose_name='Book in the cart'),
        ),
    ]
