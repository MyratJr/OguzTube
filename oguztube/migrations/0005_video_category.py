# Generated by Django 5.0 on 2023-12-22 21:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oguztube', '0004_categories_alter_shorts_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='oguztube.categories'),
        ),
    ]