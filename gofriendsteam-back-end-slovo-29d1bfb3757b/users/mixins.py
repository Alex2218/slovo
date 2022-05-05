from rest_framework import serializers
import django.contrib.auth.password_validation as validators
from django.core import exceptions

class UserSerializerMixin:
    def validate(self, data):
        password = data.get('password')
        if password:
            errors = dict()
            try:
                validators.validate_password(password=password)
            except exceptions.ValidationError as e:
                print('e.messages ' , e.messages)
                errors['password'] = list(e.messages)
            if errors:
                raise serializers.ValidationError(errors)
            if data.get('password') != data.get('confirm_password'):
                errors['password'] = "The two password fields didn't match."
                raise serializers.ValidationError(errors)
        return super().validate(data)
