from django.contrib import admin
from . import models
from admin_ordering.admin import OrderableAdmin
from django.shortcuts import resolve_url
from django.contrib.admin.templatetags.admin_urls import admin_urlname
from django.template.defaultfilters import escape
from django.utils.html import format_html
from django.contrib.admin.views.main import ChangeList
from .forms import CourseChangeListForm, RequiredInlineFormSet
from django.contrib.auth import get_user_model

User = get_user_model()


# Register your models here.

@admin.register(models.HomeTaskFile)
class HomeTaskFileAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Speaker)
class SpeakerAdmin(admin.ModelAdmin):
    # ordering_field = "name"
    list_display = ['id', "is_lead", 'name', 'position']
    list_editable = ['is_lead', "name", 'position']
    pass


@admin.register(models.Proffesion)
class ProffesionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    pass


class LessonFileAdmin(admin.TabularInline):
    model = models.LessonFile
    extra = 1


class HomeTaskAdmin(admin.TabularInline):
    model = models.HomeTask
    fields = ['file', 'text']
    extra = 1
    max_num = 1
    min_num = 1
    formset = RequiredInlineFormSet

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj=None, **kwargs)
        formset.validate_min = True
        return formset


class VideoLessonAdmin(admin.TabularInline):
    model = models.Video
    extra = 2


#
# @admin.register(models.LessonFile)
# class LessonFileAdmin

@admin.register(models.HomeTask)
class HomeTaskAdminMain(admin.ModelAdmin):
    pass


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = [LessonFileAdmin, VideoLessonAdmin, HomeTaskAdmin]
    list_display = ['title', 'get_video']
    change_form_template = 'admin/preview_template.html'

    def get_video(self, obj):
        result_str = ''
        for video in models.Video.objects.filter(lesson=obj):
            link = '<a href="%s">%s</a> | '
            url = resolve_url(admin_urlname(models.Video._meta, 'change'), video.id)
            result_str += link % (url, video.title)
        return format_html(result_str)

    get_video.allow_tags = True
    get_video.short_description = 'Прикрепленные видео'


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.LessonFile)
class LessonFileAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Module)
class ModuleAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Package)
class PackageAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        return models.Package.objects.filter(user__isnull=True)


class CourseChangeList(ChangeList):
    def __init__(self, request, model, list_display, list_display_links,
                 list_filter, date_hierarchy, search_fields, list_select_related,
                 list_per_page, list_max_show_all, list_editable, model_admin, sortable_by):
        list_select_related = True
        super(CourseChangeList, self).__init__(request, model, list_display, list_display_links,
                                               list_filter, date_hierarchy, search_fields, list_select_related,
                                               list_per_page, list_max_show_all, list_editable, model_admin,
                                               sortable_by)
        self.list_display = ['id', 'title', 'get_packages', 'speaker']
        self.list_display_links = ['id']
        # self.list_editable = ['packages']
        # self.list_select_related = True


from django import forms


class CourseAdminForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CourseAdminForm, self).__init__(*args, **kwargs)
        self.fields['packages'].queryset = models.Package.objects.filter(user__isnull=True)
        self.fields['mentor'].queryset = User.objects.filter(role='mentor')


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    pass
    list_display = ['speaker']
    form = CourseAdminForm

    #
    def get_changelist(self, request, **kwargs):
        return CourseChangeList

    def get_changelist_form(self, request, **kwargs):
        return CourseChangeListForm


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status', 'count_views']
    list_editable = ['status', 'count_views']
