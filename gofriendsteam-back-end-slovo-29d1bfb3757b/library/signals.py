from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from .models import SingleVideo, VideoOrder
from django.core.exceptions import ObjectDoesNotExist


@receiver(post_save, sender=VideoOrder)
def order_saved(sender, instance, created, **kwargs):
    print('post save!!!!! sender=VideoOrder')
    try:
        single_video = SingleVideo.objects.get(origin_video_id=instance.video.id, student=instance.student)
        single_video.status = instance.status
        single_video.save()
    except ObjectDoesNotExist as err:
        video = SingleVideo.objects.get(id=instance.video.id)
        video.id = None
        video.origin_video_id = instance.video.id
        video.student = instance.student
        video.status = instance.status
        video.save()
