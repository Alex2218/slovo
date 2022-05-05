from django.contrib import admin
from django import forms
from .models import User, Question, Tag, Answer, UserForm , CallBack
from student.utils_admin_side import StudentQuestionFilter


# Register your models here.



class StudentUser(User):
    class Meta:
        proxy = True
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class MentorUser(User):
    class Meta:
        proxy = True
        verbose_name = 'Ментор'
        verbose_name_plural = 'Менторы'





class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['user_permissions', 'groups']


@admin.register(StudentUser)
class StudentUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'is_active', 'done_form', 'referral_code', 'referred']
    form = StudentForm

    def get_queryset(self, request):
        return User.objects.filter(role='student')

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields if
                field.name in ['referral_code', 'referred', 'password', 'email']]


@admin.register(MentorUser)
class MentorUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'is_active', 'done_form']

    def get_queryset(self, request):
        return User.objects.filter(role='mentor')


@admin.register(UserForm)
class UserFormAdmin(admin.ModelAdmin):
    list_display = ['user', 'question', 'get_answers', 'get_tags']
    list_filter = [StudentQuestionFilter, "question"]

    def get_answers(self, obj):
        return " , ".join([p.answer for p in obj.answers.all()])

    def get_tags(self, obj):
        tags = [tag.tag for answer in obj.answers.all() for tag in answer.tags.all()]
        return ', '.join(tags)

    get_answers.short_description = 'Ответы'
    get_tags.short_description = 'Теги'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class AnswerAdminInline(admin.TabularInline):
    model = Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        AnswerAdminInline,
    ]

@admin.register(CallBack)
class CallBackAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'phone' , 'date' , 'status']
    list_filter = ['status']
    list_editable = ['status']
    pass