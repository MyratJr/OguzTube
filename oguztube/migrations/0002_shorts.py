# Generated by Django 5.0 on 2023-12-22 11:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oguztube', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shorts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100)),
                ('video', models.FileField(upload_to='videos', verbose_name='Wideo')),
                ('video_image', models.ImageField(upload_to='video_images', verbose_name='Image of video')),
                ('view', models.IntegerField(default=0)),
                ('uploaded_time', models.DateField(auto_now=True)),
                ('property', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Short',
                'verbose_name_plural': 'Short_videos of user',
            },
        ),
    ]