from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from drf_yasg.utils import swagger_auto_schema
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers, status

app_name = 'orders'
router = DefaultRouter()
router.register(r'create', views.OrderViewSet, basename='get_form')
urlpatterns = [

]
urlpatterns += router.urls