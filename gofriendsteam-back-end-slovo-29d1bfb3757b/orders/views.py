from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView, get_object_or_404, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework import permissions, status, generics
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import OrderCreatePackage
from course.models import Package
from .models import Order

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

User = get_user_model()


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderCreatePackage
    http_method_names = ['post']
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        package_id = request.data.pop('package_id')
        # print(request.data, 'request.data')
        user = self.request.user
        try:
            check_package_in_student = Order.objects.filter(student_id=user.id, package_id=package_id)
            if check_package_in_student:
                return Response(status=status.HTTP_208_ALREADY_REPORTED, data={
                    'msg': 'Вы уже делали заявку на этот курс!'
                })
            Order.objects.create(
                student_id=user.id,
                package_id=package_id
            )
        except Exception as e:
            print(type(e), e)
        print('package_id', package_id)
        print(request.data)
        print(args)
        print(kwargs)
        print('user', self.request.user)
        return Response(status=status.HTTP_201_CREATED, data={
            'msg': 'Ваша заявка в обработке!'
        })
