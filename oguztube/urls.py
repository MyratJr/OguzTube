from django.urls import path
from .views import *


urlpatterns = [
    path('',index, name="index"),
    path('video/<int:user_id>/<int:video_id>', video, name="video"),
    path('short',short_videos, name="short"),
    path('category/<str:cat>',category, name="category"),
    path('short_part/<str:short_part>',short_part_def, name="short_part"),
]
