# Generated by Django 5.0 on 2023-12-25 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oguztube', '0006_shorts_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shorts',
            name='view',
        ),
    ]
