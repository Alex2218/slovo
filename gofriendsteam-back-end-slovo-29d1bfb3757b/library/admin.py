from django.contrib import admin
from .models import SingleVideo, VideoOrder
from django import forms
from .utils_admin_side import VideoOrderFilterUser


# Register your models here.

class SingleVideoForm(forms.ModelForm):
    class Meta:
        model = SingleVideo
        # fields = '__all__'
        exclude = ['student', 'origin_video']


@admin.register(SingleVideo)
class SingleVideoAdmin(admin.ModelAdmin):
    form = SingleVideoForm
    list_display = ['id',
                    'title',
                    'price',
                    'speaker']

    list_filter = ['price', 'speaker']

    def get_queryset(self, request):
        return SingleVideo.objects.filter(student__isnull=True)


@admin.register(VideoOrder)
class VideoOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'student', 'video']
    list_filter = ['status', VideoOrderFilterUser]


class SingleVideoStudent(SingleVideo):
    class Meta:
        proxy = True
        verbose_name = 'Видео студента'
        verbose_name_plural = 'Видео студентов'


class SingleVideoStudentForm(forms.ModelForm):
    pass


@admin.register(SingleVideoStudent)
class SingleVideoStudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'student']
    list_filter = ['status', VideoOrderFilterUser]

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields if field.name not in ['status', 'origin_video']]

    def get_queryset(self, request):
        return SingleVideo.objects.filter(student__isnull=False)
