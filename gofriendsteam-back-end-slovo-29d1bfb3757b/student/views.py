from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from orders.models import Order
from course.models import Package, Module, Course
from course.serializers import PackageSerializer, \
    CourseSerializer, ModuleSerializer, GetUserProgressModuleSerializer, \
    LessonSerializer
from rest_framework import serializers
from .models import UserPackage, UserHomeTask
from users.models import UserForm, Answer
from django_filters import rest_framework as filters
from rest_framework.parsers import FileUploadParser
from .serializers import UserPackageSerializer, UserHomeTaskSerializer, UserAnswerHomeTaskSerializer
from pprint import pprint

# Create your views here.
from course.models import HomeTask

User = get_user_model()


# my courses (STUDENT)
class MyCoursesView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = UserPackage.objects.filter(status=True)
    http_method_names = ['get', ]
    serializer_class = UserPackageSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return self.serializer_class
        return self.serializer_class

    def list(self, request, *args, **kwargs):
        user = self.request.user
        user_packages = Package.objects.filter(user=user, status=True)
        all_course = []
        for order in user_packages:
            serializer_data = PackageSerializer(order).data
            obj_course = {
                'id': serializer_data['id'],
                'course': PackageSerializer(order.origin_package, context={
                    'request': self.request
                }).data['course']
            }
            all_course.append(obj_course)
        return Response(status=status.HTTP_200_OK, data=all_course)

    def retrieve(self, request, *args, **kwargs):
        print('retrieve retrieve retrieve')
        id_user_package = kwargs.pop('pk')
        user_package = Package.objects.get(pk=id_user_package)
        data_origin = PackageSerializer(user_package.origin_package, context={
            'request': self.request
        }).data
        response_data = []
        count_home_task_in_package = 0
        done_home_task = 0
        waiting_task = 0
        for module in data_origin['modules']:
            # module_clean = module.pop('lessons')
            # print('module ', module)
            new_obj = {
                'module': {
                    'id': module['id'],
                    'title': module['title'],
                },
            }
            module_id = module['id']
            lessons = []
            for lesson in module['lessons']:
                lesson_id = lesson['id']
                error = None
                try:
                    HomeTask.objects.get(lesson_id=lesson_id)
                    count_home_task_in_package += 1
                except Exception as e:
                    print(type(e), e, 'HomeTask')
                    error = True
                # print('lesson ', lesson)
                # print('lesson_id ', lesson_id)
                # # continue
                # print('*****' * 10, '{user} , {course_id} , {package_id} , {module_id} , {lesson_id}'.format(
                #     user=self.request.user, course_id=data_origin['course']['id'],
                #     package_id=id_user_package, module_id=module_id, lesson_id=lesson_id
                # ))
                # continue
                try:
                    home_task = UserHomeTask.objects.get(
                        student=self.request.user,
                        course_id=data_origin['course']['id'],
                        package_id=id_user_package,
                        module_id=module_id,
                        lesson_id=lesson_id,
                    )
                    dict_lesson = dict(lesson)
                    if home_task.status == 'done':
                        done_home_task += 1
                    if home_task.status == 'wait':
                        waiting_task += 1
                    dict_lesson.update(status_task=home_task.status if home_task else 'empty')

                except Exception as e:
                    print(type(e), e, 'странная проблема с назначениям дз')
                dict_lesson = dict(lesson)
                lessons.append(dict_lesson)
                new_obj['lessons'] = lessons or []
            response_data.append(new_obj)
        progress_done = round(done_home_task / count_home_task_in_package, 2) * 100
        activity_progress = round((done_home_task + waiting_task) / count_home_task_in_package, 2) * 100
        # on_wait = round(waiting_task / count_home_task_in_package, 2) * 100

        print('progress_done ', progress_done)
        print('activity_progress ', activity_progress)

        # print('total count_home_task_in_package ', count_home_task_in_package)
        # print('total done_home_task ', done_home_task)
        # print('total activity_home_task ', activity_home_task)
        # print(response_data)
        # print(dict(lesson).update(status=home_task.status))
        # print(lesson)
        # print('module {} lesson {}'.format(module, lesson))
        # print("module ", module['lessons'])
        # print('data_origin ', data_origin)
        # user_home_task_info = UserHomeTask.objects.filter(package=user_package, student=self.request.user).values(
        #     'id', 'module', 'lesson', 'status')
        #   = {}
        #
        # print('user_home_task_info ', user_home_task_info)
        #
        # for task_info in user_home_task_info:
        #     module_id = task_info['module']
        #     if module_id in total_dict:
        #         current_list = total_dict[module_id]
        #         current_list.append({
        #             'lesson': task_info['lesson'],
        #             'status': task_info['status'],
        #         })
        #         total_dict[module_id] = current_list
        #     else:
        #         total_dict[module_id] = [{
        #             'lesson': task_info['lesson'],
        #             'status': task_info['status'],
        #         }]
        # list_result = []
        # for module_id in total_dict:
        #     module = Module.objects.get(pk=module_id)
        #     module_obj = {
        #         'module': GetUserProgressModuleSerializer(module).data,
        #         'lessons': []
        #     }
        #     lessons = total_dict[module_id]
        #     for lesson in module.lessons.all():
        #         list_lesson = module_obj['lessons']
        #         lesson_task = LessonSerializer(lesson).data
        #         for l in lessons:
        #             if l['lesson'] == lesson.id:
        #                 lesson_task.update(status=l['status'])
        #         list_lesson.append(lesson_task)
        #         module_obj['lessons'] = list_lesson
        #     list_result.append(module_obj)
        return Response(status=status.HTTP_200_OK, data={
            'course': data_origin['course'],
            'modules': response_data,
            'progress_done': progress_done,
            'activity_progress': activity_progress,
            'waiting_task': waiting_task,
            'package_id': id_user_package,
            'total_count': count_home_task_in_package
        })


class RecommendedCoursesView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    http_method_names = ['get', ]

    def list(self, *args, **kwargs):
        user = self.request.user
        if user.done_form:
            user_form = [Answer.objects.get(id=i).tags.all() for i in
                         UserForm.objects.filter(user=user).values_list('answers', flat=True)]
            all_tags = list(set([value for tag in user_form for value in tag]))
            reccomended_course = list(set(Course.objects.filter(tags__in=all_tags)))
            data = CourseSerializer(reccomended_course, many=True).data
        else:
            data = CourseSerializer(Course.objects.all(), many=True).data
        return Response(status=status.HTTP_200_OK, data=data)


class UploadHomeTaskView(generics.CreateAPIView):
    serializer_class = UserAnswerHomeTaskSerializer
    parser_class = (FileUploadParser,)
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        _mutable_data = request.data
        _mutable_data._mutable = True
        list_of_keys = len([key for key in _mutable_data if key.startswith('text_answer_')])
        text_answers = [_mutable_data.pop('text_answer_{}'.format(index))[0] for index in range(list_of_keys)]
        files_answer = [_mutable_data.pop('file_answer_{}'.format(index))[0] for index in range(list_of_keys)]
        tuples_answer = list(zip(text_answers, files_answer))
        serializer = UserAnswerHomeTaskSerializer(data=_mutable_data, context={
            'request': request,
            'tuples_answer': tuples_answer
        })
        serializer.is_valid(raise_exception=True)
        saved_data = serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=UserAnswerHomeTaskSerializer(saved_data, many=True).data)


class GetVideo(generics.RetrieveAPIView):
    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = LessonSerializer

    def get(self, request, *args, **kwargs):
        user = self.request.user
        package_id = kwargs.pop('package_id')
        module_id = kwargs.pop('module_id')
        lesson_id = kwargs.pop('lesson_id')
        try:
            current_lesson = Package.objects.get(user=user, id=package_id) \
                .origin_package.modules \
                .get(id=module_id). \
                lessons.get(id=lesson_id)
            user_home_task = UserHomeTask.objects.get(student=user,
                                                      package_id=package_id,
                                                      module_id=module_id,
                                                      lesson_id=lesson_id)  # TODO: user home task
            data_to_response = LessonSerializer(current_lesson, context={
                'request': self.request
            }).data
            print('self.request ', self.request)
            # print('get !!', data_to_response)
            # print('user_home_task !!', repr(user_home_task))
        except Exception as e:
            print(type(e), e, 'get current lesson')
            return Response(status=status.HTTP_404_NOT_FOUND)
        print(args, kwargs)
        print(self.request.user)
        return Response(status=status.HTTP_200_OK, data=data_to_response)
