from django.contrib.admin import SimpleListFilter
from .models import UserHomeTask
from users.models import UserForm


class BaseStudentFilter(SimpleListFilter):
    title = 'student'
    parameter_name = 'student'

    def lookups(self, request, model_admin):
        students = set(
            [user.student for user in model_admin.model.objects.filter(
                student__isnull=False, student__role='student')
             ]
        )
        return [(student.id, student.email) for student in students]


class StudentFilterHomeTask(BaseStudentFilter):
    def queryset(self, request, queryset):
        return UserHomeTask.objects.filter(student__isnull=False, student_id=self.value()) if self.value() else queryset


class StudentFilterPackage(BaseStudentFilter):
    def queryset(self, request, queryset):
        return queryset


class StudentQuestionFilter(SimpleListFilter):
    title = 'Student'
    parameter_name = 'user'

    def lookups(self, request, model_admin):
        students = set(
            [user.user for user in model_admin.model.objects.filter(
                user__role='student')
             ]
        )
        return [(student.id, student.email) for student in students]

    def queryset(self, request, queryset):
        return UserForm.objects.filter(user__role='student', user_id=self.value()) if self.value() else queryset
