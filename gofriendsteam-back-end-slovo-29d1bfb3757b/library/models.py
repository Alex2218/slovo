from django.db import models
from ckeditor.fields import RichTextField
from users.models import Tag
from course.models import Speaker
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.


class SingleVideo(models.Model):
    title = models.CharField(verbose_name='Название видео', max_length=255)
    preview = models.ImageField(upload_to='preview_video/', blank=True, null=True)
    price = models.IntegerField(verbose_name='Цена')
    sale = models.BooleanField(default=False)
    new_price = models.IntegerField(verbose_name='Новая цена', blank=True, null=True)
    description = RichTextField()
    tags = models.ManyToManyField(Tag)
    speaker = models.ForeignKey(Speaker, on_delete=models.SET_NULL, blank=True, null=True)
    video = models.FileField(upload_to='single_video/')
    origin_video = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.BooleanField(default=False, verbose_name='Открыть видео')

    def __str__(self):
        return f'{self.title} - {self.price} - {self.speaker}'


class VideoOrder(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(SingleVideo, on_delete=models.CASCADE)
    status = models.BooleanField(default=False, verbose_name='Потвердить заказ')

    def __str__(self):
        return f'{self.student} - {self.status}'
