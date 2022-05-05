from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver
from course.models import HomeTask, Package
from student.models import UserPackage, UserHomeTask
from django.db import IntegrityError


@receiver(post_save, sender=Package)
def create_user_home_task(sender, instance, created, **kwargs):
    print('post_save package!', instance.status)
    if instance.user and instance.status:
        origin_package = instance.origin_package
        for module in origin_package.modules.all():
            for lesson in module.lessons.all():
                params = {
                    'student': instance.user,
                    'package': instance,
                    'module': module,
                    'lesson': lesson,
                    'course': origin_package.get_course,
                }
                try:
                    UserHomeTask.objects.get(**params)
                except Exception as e:
                    try:
                        # pass
                        HomeTask.objects.get(lesson=lesson)
                        params.update(has_home_task=True)
                    except Exception as e:
                        params.update(has_home_task=False)
                    UserHomeTask.objects.create(**params)
                    print()
                    print('have user!!!!')
