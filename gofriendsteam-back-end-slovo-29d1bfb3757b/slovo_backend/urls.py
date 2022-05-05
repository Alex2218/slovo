"""chat_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema
from django.conf.urls.static import static
from django.conf import settings


class CategorizedAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys):
        if len(operation_keys) >= 1:
            operation_keys = operation_keys[1:]
        return super().get_tags(operation_keys)


schema_view = get_schema_view(
    openapi.Info(
        title="Slovo api",
        default_version='v1',
        description="Test description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui(), name='docs'),
    path('api/<version>/user/', include('users.urls', namespace='users')),
    path('api/<version>/course/', include('course.urls', namespace='course')),
    path('api/<version>/course/params/', include('course.params_urls', namespace='params_urls')),
    path('api/<version>/orders/', include('orders.urls', namespace='orders')),
    path('api/<version>/student/', include('student.urls', namespace='student')),
    path('api/<version>/mentor/', include('mentor.urls', namespace='mentor')),
    path('api/<version>/library/', include('library.urls', namespace='library')),
    # path('api/<version>/params/', include('student.params_urls', namespace='student'))
    # re_path(r'^$', schema_view)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
