from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from drf_yasg.utils import swagger_auto_schema
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers, status

app_name = 'mentor'
router = DefaultRouter()
router.register(r'my_students', views.MyStudentView, basename='my_students')
# router.register(r'recommended_course', views.RecommendedCoursesView, basename='recommended_course')
urlpatterns = [
    # path('get_video/package_id-<package_id>/module_id-<module_id>/lesson_id-<lesson_id>/', views.GetVideo.as_view(),
    #      name='get_video'),
    # path('upload_home_task' , views.UploadHomeTaskView.as_view() , name='upload_home_task')
]
urlpatterns += router.urls
