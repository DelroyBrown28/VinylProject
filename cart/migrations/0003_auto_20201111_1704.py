# Generated by Django 3.1.2 on 2020-11-11 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20201111_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='seconday_category',
            new_name='secondary_category',
        ),
    ]
