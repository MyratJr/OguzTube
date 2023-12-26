from django.db.models import Q
from django.shortcuts import render
from .models import *
import socket 

ip_address = socket.gethostbyname(socket.gethostname())

def index(request):
    if request.method == "POST":
        form_data = request.POST
        name = form_data.get('gozle')
        videos = Video.objects.filter(title__icontains=name).select_related("property", "category")
    else:
        videos = Video.objects.all().select_related("property", "category")
    categories = Categories.objects.all()
    context = {
        'videos' : videos,
        'categories' : categories, 
        "ip" : ip_address  
    }
    return render(request, 'index.html', context)


def video(request, user_id, video_id):
    video = Video.objects.get(property=user_id, id=video_id)
    video.view=video.view+1
    video.save()
    categories = Categories.objects.all()
    user_videos = Video.objects.filter(~Q(id=video_id), property=user_id)[:5]
    others = Video.objects.filter(~Q(id=video_id))[:15]
    context = {
        "video" : video,
        "others" : others,
        "user_videos" : user_videos,
        'categories' : categories, 
        "ip" : ip_address 
    }
    return render(request, "each_video.html", context)

def short_videos(request):
    if request.method == "POST":
        form_data = request.POST
        name = form_data.get('gozle')
        videos = Shorts.objects.filter(title__icontains=name).select_related("property", "category")
    else:
        videos = Shorts.objects.all().select_related("property", "category")
    categories = Categories.objects.all()
    context = {
        'videos' : videos,
        'categories' : categories, 
        "ip" : ip_address  

    }
    return render(request, 'shorts.html', context)


def category(request,cat):
    if cat == "Ähli":
        videos = Video.objects.all().select_related("property", "category")
    else:
        cate = Categories.objects.get(title=cat)
        videos = Video.objects.filter(category=cate).select_related("property", "category")
    categories = Categories.objects.all()
    context={
        "videos":videos,
        "categories" : categories, 
        "cat" : cat, 
        "ip" : ip_address  

    }
    return render(request, 'index.html', context)


def short_part_def(request, short_part):
    if short_part == "Ähli":
        videos = Shorts.objects.all().select_related("property", "category")
    else:
        cate = Categories.objects.get(title=short_part)
        videos = Shorts.objects.filter(category=cate).select_related("property", "category")
    categories = Categories.objects.all()
    context={
        "videos":videos,
        "categories" : categories, 
        "cat" : short_part, 
        "ip" : ip_address  
    }
    return render(request, 'shorts.html', context)