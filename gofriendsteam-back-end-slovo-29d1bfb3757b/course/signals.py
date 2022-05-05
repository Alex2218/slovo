from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from .models import Video
from .tasks import resize_video
from .serializers import VideoSerializer
@receiver(post_save, sender=Video)
def post_save_video(sender, instance, created, **kwargs):
    # print('post_save_video')
    # print(sender, instance, created, kwargs)
    # json_video_format  =
    resize_video.delay(VideoSerializer(instance).data)