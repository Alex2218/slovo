from django.db import models


# Create your models here.


class Order(models.Model):
    student = models.ForeignKey('users.User',
                                on_delete=models.CASCADE,
                                blank=True, null=True, verbose_name='Студент')
    package = models.ForeignKey('course.Package',
                                on_delete=models.CASCADE,
                                verbose_name='Пакет курса',
                                blank=True, null=True)

    status = models.BooleanField(default=False,
                                 verbose_name='Статус заказа')  # TODO maybe create  status transaction (in future)

    def __str__(self):
        return '{}'.format(self.student)
