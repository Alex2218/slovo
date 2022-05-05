from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, get_object_or_404, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework import permissions, status, generics
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from django.http import HttpResponse
from rest_framework.views import APIView
from course.models import Package
from .serializers import SingleVideoSerializer, LibraryOrderSerializer, OrderExistsException
from .models import SingleVideo, VideoOrder

User = get_user_model()


class VideoViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'post']
    serializer_class = SingleVideoSerializer
    queryset = SingleVideo.objects.filter(student__isnull=True)

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset, context={
            'request': self.request
        }, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @action(methods=['POST'], detail=False,
            serializer_class=LibraryOrderSerializer,
            permission_classes=(permissions.IsAuthenticated,))
    def create_order(self, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=self.request.data, context={
                'request': self.request
            })
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data={
                'msg': 'Спасибо за заявку , мы свяжемся с Вами!'
            })
        except OrderExistsException as err:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={
                'msg': err.msg
            })

    @action(methods=['GET'], detail=False, permission_classes=(permissions.IsAuthenticated,))
    def my_videos(self, *agrs, **kwargs):
        student_videos = SingleVideo.objects.filter(student=self.request.user, status=True).order_by('id')
        videos = [self.serializer_class(video.origin_video , context={
            'request': self.request
        }).data for video in student_videos]  # get origin video
        return Response(status=status.HTTP_200_OK, data=videos)

    def retrieve(self, request, *args, **kwargs):
        pk_video = kwargs.pop('pk')
        video = SingleVideo.objects.get(student=self.request.user, origin_video_id=pk_video, status=True)
        return Response(status=status.HTTP_200_OK, data=self.serializer_class(video , context={
            'request': self.request
        }).data)
