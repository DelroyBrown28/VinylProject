# Generated by Django 3.1.2 on 2020-11-14 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_category_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='icon',
        ),
    ]
