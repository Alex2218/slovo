from django.core.exceptions import ObjectDoesNotExist

from .models import SingleVideo
from rest_framework import serializers
from users.serializers import TagSerializer
from course.serializers import SpeakerSerializer
from .models import VideoOrder


class SingleVideoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    # speaker = SpeakerSerializer()

    class Meta:
        model = SingleVideo
        exclude = ('student',)

    def to_representation(self, instance):
        representation  = super().to_representation(instance)
        print(self.context)
        representation['speaker'] = SpeakerSerializer(instance.speaker , context={
            'request': self.context['request']}).data
        return representation

class OrderExistsException(Exception):
    def __init__(self):
        self.msg = 'Вы уже оставили заявку на это видео. Обратитесь к менеджеру'


class LibraryOrderSerializer(serializers.Serializer):
    video_id = serializers.IntegerField()

    def create(self, validated_data):
        user = self.context['request'].user
        video_id = validated_data['video_id']
        order_params = {
            'student': user,
            'video_id': video_id,
        }
        try:
            VideoOrder.objects.get(**order_params)
            raise OrderExistsException
        except ObjectDoesNotExist as err:
            new_order = VideoOrder.objects.create(**order_params)
        return new_order
