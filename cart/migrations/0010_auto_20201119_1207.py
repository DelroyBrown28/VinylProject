# Generated by Django 3.1.2 on 2020-11-19 12:07

import cart.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_auto_20201116_1039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='secondary_category',
        ),
        migrations.AddField(
            model_name='product',
            name='secondary_category',
            field=models.CharField(blank=True, max_length=15, verbose_name=cart.models.Category),
        ),
    ]
