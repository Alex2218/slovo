from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from drf_yasg.utils import swagger_auto_schema
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers, status

app_name = 'course'
router = DefaultRouter()
router.register(r'all_courses', views.AllCoursesView, basename='all_courses')
router.register(r'package_info', views.PackageView, basename='package_info')
router.register(r'articles', views.ArticleView, basename='articles')
urlpatterns = [

]
urlpatterns += router.urls
auth_urls = [
    path('speakers/', views.SpeakerView.as_view()),
    # path('login/', decorated_login_view),
    # path('social-login/', decorated_login_view),
    # path('password_reset/', views.PasswordResetView.as_view()),
    # # path('get_form/', views.StartFormView.as_view()),
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #         views.activate, name='activate'),
]

urlpatterns += auth_urls
