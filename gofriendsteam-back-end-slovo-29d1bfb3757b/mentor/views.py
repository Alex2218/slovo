from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from orders.models import Order
from course.models import Package, Module, Course
from course.serializers import PackageSerializer, \
    CourseSerializer, ModuleSerializer, GetUserProgressModuleSerializer, \
    LessonSerializer
from rest_framework import serializers
# from .models import UserPackage, UserHomeTask
from users.models import UserForm, Answer
from django_filters import rest_framework as filters
from rest_framework.parsers import FileUploadParser
# from .serializers import UserPackageSerializer, UserHomeTaskSerializer, UserAnswerHomeTaskSerializer
from pprint import pprint
from .serializers import MentorCourseSerializer
# Create your views here.
from course.models import HomeTask

from student.models import UserHomeTask

User = get_user_model()


# my courses (STUDENT)
class MyStudentView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    # queryset = UserPackage.objects.filter(status=True)
    http_method_names = ['get', ]

    serializer_class = MentorCourseSerializer

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return self.serializer_class
    #     return self.serializer_class

    def list(self, request, *args, **kwargs):
        user = self.request.user
        my_course = Course.objects.filter(mentor=user)
        for course in my_course:
            user_home_task_course = UserHomeTask.objects.filter(course=course)

            print("course ", user_home_task_course)
        serializer = self.serializer_class(my_course, many=True)
        print('user', user)
        print('user', serializer.data)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
