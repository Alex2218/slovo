from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from drf_yasg.utils import swagger_auto_schema
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers, status
from .serializers import TokenObtainPairCustomSerializer

app_name = 'users'
router = DefaultRouter()
router.register(r'get_form', views.StartFormView, basename='get_form')
urlpatterns = [

]
urlpatterns += router.urls

decorated_login_view = \
    swagger_auto_schema(
        method='post',
        responses={status.HTTP_200_OK: TokenObtainPairCustomSerializer}
    )(views.TokenObtainPairCustomView.as_view())

auth_urls = [
    path('callback/' , views.CallBackView.as_view()),
    path('register/', views.CreateUserView.as_view()),
    path('login/', decorated_login_view),
    path('social-login/', views.GoogleView.as_view()),
    path('password_reset/', views.PasswordResetView.as_view()),
    # path('get_form/', views.StartFormView.as_view()),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='activate'),
]

urlpatterns += auth_urls
