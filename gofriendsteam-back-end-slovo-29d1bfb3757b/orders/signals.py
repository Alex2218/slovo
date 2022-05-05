from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from course.models import HomeTask, Package
from .models import Order
from student.models import UserPackage, UserHomeTask
from django.db import IntegrityError


@receiver(post_save, sender=Order)
def check_order_isTrue(sender, instance, created, **kwargs):
    # print(instance.status, 'instance!!!!')

    if instance.status:
        try:
            package = Package.objects.get(origin_package_id=instance.package.id,
                                          user=instance.student)

        except Exception  as e:
            package = Package.objects.get(id=instance.package.id)
            package.id = None
            package.origin_package_id = instance.package.id
            package.user = instance.student
            package.status = instance.status
            package.save()
            # print(type(e), e)
    # try:
    #     user_package, created_package = UserPackage.objects.get_or_create(student=instance.student,
    #                                                                       package=instance.package)
    #
    #     print('created_package ', created_package)
    #     user_package.status = instance.status
    #     user_package.save()
    #     # if not created_package:
    #
    #     #
    #     #
    #     if instance.status:
    #         course = user_package.package.get_course
    #         modules = user_package.package.modules.all()
    #         for module in modules:
    #             for lesson in module.lessons.all():
    #                 params = {
    #                     "student": instance.student,
    #                     "course": course,
    #                     "package": user_package,
    #                     "module": module,
    #                     "lesson": lesson,
    #                 }
    #                 try:
    #                     HomeTask.objects.get(lesson=lesson)
    #                     params.update(has_home_task=True)
    #                     # if HomeTask.objects.get(lesson=lesson):
    #                     #     UserHomeTask.objects.get_or_create(student=instance.student,
    #                     #                                        course=course,
    #                     #                                        package=user_package,
    #                     #                                        module=module,
    #                     #                                        lesson=lesson)
    #                 except Exception as e:
    #                     params.update(has_home_task=False)
    #                     print(type(e), e)
    #                 UserHomeTask.objects.create(**params)
    #                 print('module {}  , lesson - {}'.format(module, lesson))
    #     print("signals ", user_package)
    # except Exception as e:
    #     print("Error in signals ", type(e), e)
    #     # UserPackage.objects.create(student=instance.student, package=instance.package, status=instance.status)
