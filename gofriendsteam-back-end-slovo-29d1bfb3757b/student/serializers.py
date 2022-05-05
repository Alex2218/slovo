from django.db import transaction
from rest_framework import serializers
from .models import UserPackage, UserHomeTask, UserAnswer
from course.serializers import PackageSerializer, \
    CourseSerializer, ModuleSerializer, GetUserProgressModuleSerializer, \
    LessonSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAnswerHomeTaskSerializer(serializers.ModelSerializer):
    # file = serializers.FileField(required=True)
    package = serializers.IntegerField(required=False)
    module = serializers.IntegerField(required=False)
    lesson = serializers.IntegerField(required=False)
    text_answer = serializers.CharField(required=False)

    class Meta:
        model = UserAnswer
        fields = '__all__'

    def create(self, validated_data):
        package_id = validated_data.pop('package')
        module_id = validated_data.pop('module')
        lesson_id = validated_data.pop('lesson')
        tuples_answer = self.context['tuples_answer']
        with transaction.atomic():
            student = self.context['request'].user
            print("user in UserAnswerHomeTaskSerializer create", student)

            task = UserHomeTask.objects.get(student_id=student,  # its hardcode! TODO : must bu student instance!
                                            package_id=package_id,
                                            module_id=module_id,
                                            lesson_id=lesson_id)
            new_user_answer = [UserAnswer(task=task,
                                          file_answer=file if file else None,
                                          text_answer=text if text else ''
                                          ) for text, file in tuples_answer if text or file]
            for user_answer in new_user_answer:
                user_answer.save()
        return new_user_answer


class UserPackageSerializer(serializers.ModelSerializer):
    package = PackageSerializer()

    class Meta:
        model = UserPackage
        fields = ('id', 'package')


class UserHomeTaskSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = UserHomeTask
        fields = ['id', 'course']
