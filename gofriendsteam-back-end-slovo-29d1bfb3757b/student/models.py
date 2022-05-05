from django.db import models


# class HomeTaskUser(models.Model):


class UserPackage(models.Model):
    student = models.ForeignKey('users.User', on_delete=models.CASCADE,
                                blank=True, null=True)
    package = models.ForeignKey('course.Package', on_delete=models.CASCADE,
                                blank=True, null=True)
    status = models.BooleanField(default=False, verbose_name='Открыть')

    def __str__(self):
        return self.package.title


class UserHomeTask(models.Model):
    STATUS_CHOICES = (
        ('done', 'Сдано'),
        ('not_done', 'Не сдано'),
        ('wait', 'На проверке'),
        # ('empty', 'Нет дз'),
    )
    student = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, blank=True, null=True)
    package = models.ForeignKey('course.Package', on_delete=models.CASCADE, blank=True, null=True)
    module = models.ForeignKey('course.Module', on_delete=models.CASCADE, blank=True, null=True)
    lesson = models.ForeignKey('course.Lesson', on_delete=models.CASCADE, blank=True, null=True)
    has_home_task = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[1][0])

    def __repr__(self):
        return 'UserHomeTask(student - {student}' \
               ' , course={course} , ' \
               'package- {package},' \
               'module-{module} , lesson - {lesson} , ' \
               'status  - {status})'.format(
            student=self.student,
            course=self.course.id,
            package=self.package.id,
            module=self.module.id,
            lesson=self.lesson.id,
            status=self.status,
        )

    class Meta:
        unique_together = ('student', 'course', 'package', 'module', 'lesson')


class UserAnswer(models.Model):
    task = models.ForeignKey(UserHomeTask, on_delete=models.CASCADE, blank=True, null=True)
    file_answer = models.FileField(upload_to='file_answer/', blank=True, null=True)
    text_answer = models.TextField(max_length=5000, verbose_name='Текст ответа')
