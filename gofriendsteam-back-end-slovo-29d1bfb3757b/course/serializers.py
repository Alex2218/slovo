from .models import Course, \
    Package, Speaker, Proffesion, \
    Lesson, Video, LessonFile, Module, \
    HomeTask, HomeTaskFile, Article
from rest_framework import serializers
from users.serializers import TagSerializer


class SpeakerSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Speaker
        fields = '__all__'

    def get_photo(self, obj):
        request = self.context['request']
        if obj.photo:
            photo_url = obj.photo.url
            print('small_image_url')
            return request.build_absolute_uri(photo_url)


class VideoSerializer(serializers.ModelSerializer):
    video_1080 = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ['id', 'title', 'video_1080', 'video_720', 'video_360']

    def get_video_1080(self, obj):
        try:

            request = self.context['request']
            if obj.video_1080:
                video_1080_url = obj.video_1080.url
                print('small_image_url')
                return request.build_absolute_uri(video_1080_url)
        except KeyError as e:
            return obj.video_1080.url
        # return None


class GetUserProgressModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('id', 'title')


class LessonFileSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    class Meta:
        model = LessonFile
        fields = ['id', 'file']

    def get_file(self , obj):
        request = self.context['request']
        if obj.file:
            full_file_url = obj.file.url
            return request.build_absolute_uri(full_file_url)


class HomeTaskFileSerializer(serializers.ModelSerializer):
    file  = serializers.SerializerMethodField()
    class Meta:
        fields = '__all__'
        model = HomeTaskFile

    def get_file(self, obj):
        request = self.context['request']
        if obj.file:
            full_file_url = obj.file.url
            return request.build_absolute_uri(full_file_url)

class HomeTaskSerializer(serializers.ModelSerializer):
    # files = HomeTaskFileSerializer(many=True, source='file')

    class Meta:
        fields = ['id', 'text']
        model = HomeTask


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            print('to_representation home task file!')
            all_files_for_task = instance.file.all()
            representation['files'] = [HomeTaskFileSerializer(f , context={
                'request': self.context['request']
            }).data  for f in all_files_for_task ]
            return representation
        except Exception as e:
            print(e , type(e))
        return representation

class LessonSerializer(serializers.ModelSerializer):
    # videos = serializers.RelatedField(source='lesson_video', queryset=Video.objects.all())

    class Meta:
        model = Lesson
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            all_files_for_lesson = LessonFile.objects.filter(lesson=instance)
            try:
                all_home_task = HomeTask.objects.get(lesson=instance)  # for user task
                representation['task'] = HomeTaskSerializer(all_home_task ,  context={'request': self.context['request']},).data
            except Exception as e:
                representation['task'] = {}
                print(type(e), e)
            all_videos = Video.objects.filter(lesson=instance)
            representation['files'] = LessonFileSerializer(all_files_for_lesson,
                context={'request': self.context['request']},
                many=True).data
            # representation['tasks'] = HomeTaskSerializer(all_home_task, many=True).data
            # print(self.re)
            print("self.context['request'] ", self.context['request'])
            representation['videos'] = VideoSerializer(all_videos, context={
                'request': self.context['request']
            }, many=True).data
        except Exception as e:
            print(type(e), e)
        print('instance ', instance)
        return representation


class ModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Module
        fields = '__all__'


class CourseSerializerByPackage(serializers.ModelSerializer):
    full_image = serializers.SerializerMethodField()
    small_image = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'speaker', 'proffesion', 'duration', 'full_image', 'small_image'
        ]

    # def get_video_1080(self, obj):
    #     request = self.context['request']
    #     if obj.video_1080:
    #         video_1080_url = obj.video_1080.url
    #         print('small_image_url')
    #         return request.build_absolute_uri(video_1080_url)
    def get_full_image(self, obj):
        request = self.context['request']
        if obj.full_image:
            full_image_url = obj.full_image.url
            return request.build_absolute_uri(full_image_url)

    def get_small_image(self, obj):
        request = self.context['request']
        if obj.small_image:
            small_image_url = obj.small_image.url
            return request.build_absolute_uri(small_image_url)
            # pass


class PackageSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True)

    class Meta:
        model = Package
        fields = [
            'id', 'title', 'description',
            'price', 'duration', 'is_sale',
            'new_price', 'modules'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.get_course:
            representation['course'] = CourseSerializerByPackage(instance.get_course, context={
                'request': self.context['request']
            }).data
        else:
            representation['course'] = None
        return representation


class ProffesionSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Proffesion
        fields = ['id', 'title', 'tags']


class CourseSerializer(serializers.ModelSerializer):
    speaker = SpeakerSerializer()
    proffesion = ProffesionSerializer()
    packages = PackageSerializer(many=True)
    tags = TagSerializer(many=True)
    small_image = serializers.SerializerMethodField()
    full_image = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description',
            'speaker', 'proffesion', 'packages',
            'duration', 'tags', 'small_image', 'full_image'
        ]

    def get_small_image(self, obj):
        request = self.context['request']
        if obj.small_image:
            small_image_url = obj.small_image.url
            print('small_image_url')
            return request.build_absolute_uri(small_image_url)

    def get_full_image(self, obj):
        request = self.context['request']
        if obj.full_image:
            full_image_url = obj.full_image.url
            print('full_image', full_image_url)
            return request.build_absolute_uri(full_image_url)

    # full_image

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            packages_min_price = min([package.price for package in instance.packages.all()])
            representation['from_min_price'] = packages_min_price
            return representation
        except Exception as e:
            representation['from_min_price'] = 0


#
# class ArticleListRelation(serializers.RelatedField):
#     pass


class ArticleSerializer1(serializers.ModelSerializer):
    id_ = serializers.IntegerField(source='id')
    desc_ = serializers.CharField(source='desc')
    lead_ = serializers.CharField(source='lead')
    image_ = serializers.SerializerMethodField()
    count_views_ = serializers.CharField(source='count_views')
    date_ = serializers.CharField(source='date')
    author = SpeakerSerializer()

    class Meta:
        model = Article
        fields = [
            'id_',
            'desc_',
            'lead_',
            'image_',
            'count_views_',
            'date_',
            'author',
        ]

    def get_image_(self, obj):
        request = self.context['request']
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)

class ArticleSerializers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    author = SpeakerSerializer()
    articles = ArticleSerializer1(many=True, read_only=True)

    class Meta:
        model = Article
        fields = [
            'id',
            'title',
            'desc',
            'image',
            'count_views',
            'date',
            'content' ,
            'lead' ,
            'articles' ,
            'author'
        ]
    def get_image(self, obj):
        request = self.context['request']
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)
