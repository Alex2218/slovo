import logging
import re
import sys
import time
from datetime import datetime
import moviepy.editor as mp
import requests
from django.contrib.auth import get_user_model
from slovo_backend.celery import app
from django.conf import settings
import uuid

User = get_user_model()
from .models import Video

RESOLUTION = (360,)


@app.task
def resize_video(video_instance):
    id_video = video_instance.get('id')
    title_video = video_instance.get('title')
    # path_to_video = video_instance.get('video')
    # name_video = path_to_video.split('/')[-1].split('.')[0]

    video_object = Video.objects.get(pk=id_video)
    path_to_video = f'{settings.MEDIA_ROOT}/{video_object.video_1080.name}'
    video = mp.VideoFileClip(path_to_video)  # for example 1080
    name, ext = video_object.video_1080.name.split(".")
    print(name, ext)
    for resolution in RESOLUTION:
        video_resized = video.resize(height=resolution)
        path_to_new_video_file = f'{settings.MEDIA_ROOT}/lessons_video_{resolution}/{name.split("/")[-1]}-{str(uuid.uuid4())[:10]}resized_{resolution}.{ext}'
        print('path_to_new_video_file ', path_to_new_video_file)
        video_resized.write_videofile(path_to_new_video_file, audio=True)
        Video.objects.filter(pk=id_video).update(video_360=path_to_new_video_file)

    # print('id_video', id_video)
    # print('title_video', title_video)
    # print('path_to_video', path_to_video)
    # # print('name_video', name_video)
    # print('video', video)
