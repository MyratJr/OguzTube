from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class User(AbstractUser):
    avatar = models.ImageField(upload_to = "images", verbose_name = "avatar")


    def __str__(self):
        return str(f'{self.username}')


    def save(self, *args, **kwargs):
        if not self.id:
            self.set_password(self.password)
            super().save(*args, **kwargs)


    class Meta:
        verbose_name_plural = 'Users'


class Categories(models.Model):
    title = models.CharField(max_length = 50, blank = True)


    def __str__(self):
        return str(f'{self.title}')


class Video(models.Model):
    property = models.ForeignKey(User, on_delete = models.CASCADE, blank = True)
    title = models.CharField(max_length = 100, blank = True)
    category = models.ForeignKey(Categories, on_delete = models.CASCADE, default=None)
    video = models.FileField(upload_to = "videos",verbose_name = "Wideo")
    video_image = models.ImageField(upload_to = "video_images", verbose_name = "Image of video")
    view = models.IntegerField(default = 0)
    duration = models.DurationField(default = datetime.timedelta(seconds = 0))
    uploaded_time = models.DateField(auto_now=True)


    class Meta:
        verbose_name_plural = 'Videos of user'
        verbose_name = 'Video'


class Shorts(models.Model):
    property = models.ForeignKey(User, on_delete = models.CASCADE, blank = True)
    title = models.CharField(max_length = 100, blank = True)
    category = models.ForeignKey(Categories, on_delete = models.CASCADE, default=None)
    video = models.FileField(upload_to = "videos",verbose_name = "Wideo (1x2 size required)")
    video_image = models.ImageField(upload_to = "video_images", verbose_name = "Image of video")
    uploaded_time = models.DateField(auto_now=True)


    class Meta:
        verbose_name_plural = 'Short_videos of user'
        verbose_name = 'Short'