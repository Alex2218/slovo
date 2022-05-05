from .models import Order
from rest_framework import serializers


class OrderCreatePackage(serializers.Serializer):
    package_id = serializers.IntegerField()
