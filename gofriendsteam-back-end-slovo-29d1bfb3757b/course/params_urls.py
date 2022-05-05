from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'params_urls'
router = DefaultRouter()
urlpatterns = [
    path('', views.ParamsView.as_view())

]
urlpatterns += router.urls
