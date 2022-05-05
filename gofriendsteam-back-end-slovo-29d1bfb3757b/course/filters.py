from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters
from .models import Course, Speaker

User = get_user_model()


class CourseFilter(filters.FilterSet):
    speaker_id = filters.ModelChoiceFilter(field_name='speaker', queryset=Speaker.objects.all(), method='by_speaker')
    tag_id = filters.ModelChoiceFilter(field_name='tag')
    proffesion_id = filters.ModelChoiceFilter(field_name='tag')

    class Meta:
        model = Course
        fields = ['speaker_id', 'tag_id', 'proffesion_id']

    def by_speaker(self, queryset, name, value):
        print(queryset, name, value, 'by_speaker')
        return queryset
