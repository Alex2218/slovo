from django.contrib.admin import SimpleListFilter
from .models import VideoOrder
from django.contrib.auth import get_user_model

User = get_user_model()


class VideoOrderFilterUser(SimpleListFilter):
    title = 'student'
    parameter_name = 'student'

    def lookups(self, request, model_admin):
        try:
            students = set(
                [user.student for user in model_admin.model.objects.all()]
            )
            return [(student.id, student.email) for student in students]
        except AttributeError as e:
            return [(student.id, student.email) for student in User.objects.filter(role='student')]

    def queryset(self, request, queryset):
        return VideoOrder.objects.filter(student__isnull=False, student_id=self.value()) if self.value() else queryset
