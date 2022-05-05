from django.shortcuts import render
# from djangorestframework_camel_case.parser import CamelCaseJSONParser

from .models import Course, Package, Proffesion, Speaker, Article
from users.models import Tag
from users.serializers import TagSerializer
# Create your views here.
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from .serializers import CourseSerializer, PackageSerializer, \
    ProffesionSerializer, SpeakerSerializer, ArticleSerializers

# class PackageView(generics.APIVIE)
from .filters import CourseFilter
from django_filters import rest_framework as filters


# from rest_framework.parsers import MultiPartParser

class AllCoursesView(viewsets.ModelViewSet):
    # pass
    # parser_classes = (MultiPartParser, CamelCaseJSONParser,)
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get']
    # filter_backends = (filters.DjangoFilterBackend,)
    queryset = Course.objects.all()

    # filterset_class = CourseFilter

    # fil

    # def get_pa .

    def get_serializer_class(self):
        return CourseSerializer

    def get_queryset(self):
        # pk =
        print('get_queryset')
        return self.queryset

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.pop('pk')
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course, context={
            'request': self.request
        })
        print(request, args, kwargs)
        print(request, args, serializer)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def list(self, request, *args, **kwargs):
        print('list')
        # return
        speaker_id = self.request.query_params.get('speaker_id')
        tag_id = self.request.query_params.get('tag_id')
        proffesion_id = self.request.query_params.get('proffesion_id')
        print('speaker_id ', speaker_id)
        print('tag_id ', tag_id)
        print('proffesion_id ', proffesion_id)
        qs_speaker = None
        qs_tag = None
        qs_prof = None
        if speaker_id:
            qs_speaker = self.queryset.filter(speaker_id=speaker_id)
        if tag_id:
            qs_tag = self.queryset.filter(tags__in=[tag_id])
        if proffesion_id:
            qs_prof = self.queryset.filter(proffesion_id=proffesion_id)
        print('qs_speaker', qs_speaker)
        print('qs_tag', qs_tag)
        print('qs_prof', qs_prof)
        all_courses = self.queryset.order_by('-id')
        serializer = CourseSerializer(all_courses, context={'request': self.request},
                                      many=True)
        print(all_courses, len(all_courses))
        return Response(data=serializer.data)
        # return Response(data={
        #     'sta': 1
        # })


class PackageView(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    http_method_names = ['get']
    serializer_class = PackageSerializer
    permission_classes = (permissions.AllowAny,)


from rest_framework.views import APIView


class ParamsView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, *args, **kwargs):
        all_proffesions = ProffesionSerializer(
            Proffesion.objects.all(), many=True).data
        all_tags = TagSerializer(Tag.objects.all(), many=True).data
        all_speaker = SpeakerSerializer(Speaker.objects.all(), many=True).data
        return Response(status=status.HTTP_200_OK, data={
            'tags': all_tags,
            'proffesions': all_proffesions,
            'speakers': all_speaker
        })


class SpeakerView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, *args, **kwargs):
        return Response(status=status.HTTP_200_OK,
                        data=SpeakerSerializer(Speaker.objects.filter(is_lead=True), context={
                            'request': self.request
                        }, many=True).data)


class ArticleView(viewsets.ModelViewSet):
    serializer_class = ArticleSerializers
    permission_classes = (permissions.AllowAny,)
    queryset = Article.objects.filter(status=True).order_by('-id')

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK, data=self.serializer_class(self.queryset, context={
            'request': self.request
        }, many=True).data)
