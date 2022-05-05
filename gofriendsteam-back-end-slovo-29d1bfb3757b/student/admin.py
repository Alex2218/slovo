from django.contrib import admin
from course.models import HomeTask, Package
from django.contrib.admin import SimpleListFilter
from .models import UserPackage, UserHomeTask, UserAnswer
from .utils_admin_side import StudentFilterHomeTask, StudentFilterPackage
from django import forms


# Register your models here.


class UserAnswerAdmin(admin.TabularInline):
    model = UserAnswer


@admin.register(UserHomeTask)
class UserHomeTaskAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'package', 'module', 'lesson', 'status',
                    'count_answer']
    list_filter = ['course', 'package', StudentFilterHomeTask]
    inlines = [UserAnswerAdmin, ]

    def count_answer(self, instance):
        return len(UserAnswer.objects.filter(task=instance))

    count_answer.short_description = 'Кол-во ответов'


@admin.register(UserPackage)
class UserPackageAdmin(admin.ModelAdmin):
    list_display = ['student', 'status']
    list_filter = [StudentFilterPackage]
    pass


class HomeTaskStudent(HomeTask):
    class Meta:
        proxy = True
        verbose_name = 'Домашка студентa'
        verbose_name_plural = 'Домашки студентов'


class StudentPackage(Package):
    class Meta:
        proxy = True
        verbose_name = 'пакет студента'
        verbose_name_plural = 'пакеты студентов'


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        exclude = ['modules']


@admin.register(StudentPackage)
class StudentPackageAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'status']
    list_filter = ['user',]
    form = PackageForm

    def get_queryset(self, request):
        return Package.objects.filter(user__isnull=False)

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields if field.name != 'status']
