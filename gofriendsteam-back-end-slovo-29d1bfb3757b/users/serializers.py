from django.template.loader import render_to_string
from rest_framework import serializers
from .mixins import UserSerializerMixin
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model
from .tokens import account_activation_token, password_reset_token
from .constants import ROLE_USER
from .tasks import send_email_task
from django.utils.encoding import force_bytes, force_text
import string
import random
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Question, Answer, Tag, CallBack
from django.contrib.auth import authenticate

User = get_user_model()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag']


class TokenObtainPairCustomSerializer(TokenObtainPairSerializer):
    password = serializers.CharField(required=False)

    def validate(self, attrs):
        print('validate validate validate')
        print(attrs)
        self.user = authenticate(**{
            self.username_field: attrs[self.username_field],
            'password': attrs['password'],
        })
        is_not_activated = User.objects.filter(
            email=attrs[self.username_field],
            is_active=False
        ).exists()
        data = {}

        if is_not_activated:
            raise serializers.ValidationError(
                'Аккаунт не активирован.'
            )

        if self.user is None:
            raise serializers.ValidationError(
                'Неправильный логин или пароль.',
            )

        refresh = self.get_token(self.user)

        # data['refresh'] = str(refresh)
        # data['role'] = self.user.role
        data['token'] = str(refresh.access_token)
        data['user'] = {}
        data['user']['email'] = self.user.email
        data['user']['role'] = self.user.role
        data['user']['done_form'] = self.user.done_form
        print(self.user.role)
        return data



class UserSerializer(UserSerializerMixin, serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    password = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    confirm_password = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    referral_code = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    role = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'confirm_password', 'first_name', 'last_name', 'role', 'referral_code')
        extra_kwargs = {'phone': {'required': True}}
        error_messages = {"password": {"required": "123123213"}}

    def create(self, validated_data):
        referral_code = validated_data.get('referral_code')
        referred = None
        if referral_code:
            referred = User.objects.get(referral_code=referral_code)
            print('referred ', referred)
        email = validated_data['email']
        try:
            first_name = validated_data['first_name']
            last_name = validated_data['last_name']
        except KeyError as e:
            print('KeyError in register !', e)
            first_name = ''
            last_name = ''
        user = User.objects.create(
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_active=False,
            role=validated_data['role'],
            referred=referred
        )
        print("validated_data ", validated_data)
        user.set_password(validated_data['password'])
        user.save()
        mail_subject = 'Активация аккаунта.'
        message = render_to_string('mail/account_activation_email.html', {
            # 'domain': settings.HOST_NAME,
            'request': self.context['request'].META['HTTP_HOST'],
            'domain': 'api.slovo.expert',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        data = {
            'to_emails': [email, ],
            'mail_subject': mail_subject,
            'html_content': message
        }
        # # send_email_task.delay(**data)
        send_email_task.delay(**data)
        return user

    # def __init__(self, *args, **kwargs):
    #     super(UserSerializer, self).__init__(*args, **kwargs)
    #     self.fields['password'].error_messages['required'] = 'Укажите пароль'
    #     self.fields['password'].error_messages['null'] = 'Пароль не может быть пустым'
    #     self.fields['password'].error_messages['invalid'] = 'В пароле не валидные символы'
    #     print("self.fields['password']. erorrs" , )


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('email',)

    def save(self, *args):
        print('save!!!!!!')
        email = self.validated_data['email']
        user = User.objects.filter(email=email).first()
        if user:
            password = self.generate_password(35)
            user.set_password(password)
            user.save()
            print('if! user')
            mail_subject = 'Reset your password.'
            message = render_to_string('mail/password_reset_email.html', {
                'user': user,
                'password': password
            })
            data = {
                'to_emails': [email, ],
                'mail_subject': mail_subject,
                'html_content': message
            }
            send_email_task.delay(**data)
            return password
        else:
            errors = dict()
            errors['email'] = "Пользователя с таким e-mail не найдено"
            raise serializers.ValidationError(errors)

    @staticmethod
    def generate_password(string_length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(string_length))


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'question', 'answers']


class UserAnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    answer_id = serializers.ListField()

    class Meta:
        fields = [
            'question_id',
            'answer_id',
        ]


class UserQuestionAnwersSer(serializers.Serializer):
    questions = UserAnswerSerializer(many=True)

    class Meta:
        fields = ('questions',)


class GoogleTokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=500)


class CallBackSerializer(serializers.ModelSerializer):
    class Meta:
        model  = CallBack
        fields  = [
            'name',
            'phone'
        ]