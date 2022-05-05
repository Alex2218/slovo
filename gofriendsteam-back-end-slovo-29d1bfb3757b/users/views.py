from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.template.loader import render_to_string
from rest_framework import status, viewsets
from rest_framework.generics import CreateAPIView, get_object_or_404, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework import permissions, status, generics
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer, PasswordResetSerializer, QuestionSerializer, UserAnswerSerializer, UserQuestionAnwersSer, TokenObtainPairCustomSerializer, GoogleTokenSerializer, CallBackSerializer
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import Question, Answer, UserForm, CallBack
# start import for google auth
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager
import requests
import json

# end import for google auth
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

User = get_user_model()


class TokenObtainPairCustomView(TokenObtainPairView):
    """
    Takes a set of user credentials and returns an access and refresh JSON web
    token pair to prove the authentication of those credentials.
    """
    serializer_class = TokenObtainPairCustomSerializer


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # if serializer.is_valid():
        #     print('valid form!!!!')
        # else:
        #     print('invalid form')
        #     return Response(data={
        #         'msg': 'Ваш аккаунт уже отправлен на активацию',
        #         'errors': serializer.errors
        #     }, status=status.HTTP_400_BAD_REQUEST)
        # print('ser', serializer)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(data={
            'send_email': True,
            'user': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)


class CallBackView(CreateAPIView):
    model = CallBack
    permission_classes = (permissions.AllowAny,)
    serializer_class = CallBackSerializer

    def post(self , request , *args , **kwargs):
        serializer  = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED , data={
                'msg': 'Спасибо что Вы с нами. Мы свяжемся с Вами!'
            })


class GoogleView(generics.CreateAPIView):
    serializer_class = GoogleTokenSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        print('GoogleView!!!!!')
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.data.get('token')

        payload = {'access_token': token}  # validate the token
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)
        print('data social login', data)
        if 'error' in data:
            print('Error!')
            print(data)
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)

        # create user if not exist
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            user = User()
            user.username = data['email']
            # provider random default password
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data['email']
            user.role = 'student'
            user.save()

        token = RefreshToken.for_user(user)  # generate token without username & password
        response = {}
        response['user'] = {}
        response['user']['email'] = user.email
        response['user']['role'] = user.role or 'student'
        response['user']['done_form'] = user.done_form
        # response['username'] = user.username
        response['token'] = str(token.access_token)
        # response['refresh_token'] = str(token)
        return Response(response)


class LoginView(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        print('LoginView LoginView LoginView')
        # by default attempts username / passsword combination
        response = super(LoginView, self).post(request, *args, **kwargs)
        # token = response.data['token']  # don't use this to prevent errors
        # below will return null, but not an error, if not found :)
        res = response.data
        token = res.get('token')

        # token ok, get user
        if token:
            user = jwt_decode_handler(token)  # aleady json - don't serialize
            print(' if token:')
        else:  # if none, try auth by email
            req = request.data  # try and find email in request
            email = req.get('email')
            password = req.get('password')
            username = req.get('username')
            print(' else: ')
            if email is None or password is None:
                return Response({'success': False,
                                 'message': 'Missing or incorrect credentials',
                                 'data': req},
                                status=status.HTTP_400_BAD_REQUEST)

            # email exists in request, try to find user
            try:
                user = User.objects.get(email=email)
                print('  try:')
            except Exception as e:
                print('except', e)
                return Response({'success': False,
                                 'message': 'User not found',
                                 'data': req},
                                status=status.HTTP_404_NOT_FOUND)

            if not user.check_password(password):
                return Response({'success': False,
                                 'message': 'Incorrect password',
                                 'data': req},
                                status=status.HTTP_403_FORBIDDEN)

            # make token from user found by email
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            print(user)

        try:
            if not user.is_active:
                return Response(data={
                    'message': 'This account is not active.'
                }, status=status.HTTP_403_FORBIDDEN)
            # user_obj = User.objects.get(pk=user['user_id'])
        except Exception as e:
            print('error login view ', e)
            user_obj = User.objects.get(pk=user['user_id'])
            return Response({'success': True,
                             'token': token,
                             'user': {
                                 'email': user_obj.email,
                                 'role': user_obj.role,
                                 'done_form': user_obj.done_form,
                             }
                             },
                            status=status.HTTP_200_OK)


class SocialLoginView(ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super(SocialLoginView, self).post(request, *args, **kwargs)
        # token = response.data['token']  # don't use this to prevent errors
        # below will return null, but not an error, if not found :)
        res = response.data
        token = res.get('token')
        email = request.data.get('email')
        print(request.data, request.data.get('email'))
        # firstname , lastname  , full_name
        if email:
            user, created = User.objects.get_or_create(email=email)
            print(user, created, user.is_active)
            if created:
                user.role = 'student'
                user.save()
            if user.is_active:
                print("user.is_active ", user.is_active)
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                return Response({'success': True,
                                 'token': token,
                                 'user': {
                                     'email': user.email,
                                     'role': user.role,
                                     'done_form': user.done_form
                                 }
                                 },
                                status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)


class PasswordResetView(generics.UpdateAPIView):
    model = User
    permission_classes = (permissions.AllowAny,)
    serializer_class = PasswordResetSerializer

    def update(self, request, *args, **kwargs):
        # serializer_class = PasswordResetSerializer
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        serializer.save()

        if serializer.is_valid():
            print(serializer.validated_data)
            return Response(data={
                'send_email': True,
                'email': serializer.validated_data['email']
            }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StartFormView(viewsets.ModelViewSet):
    # permission_classes = (permissions.AllowAny,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Question.objects.all().order_by('id')

    def get_serializer_class(self):
        if self.action == 'list':
            return QuestionSerializer
        elif self.action == 'create':
            return UserQuestionAnwersSer

        return QuestionSerializer

    def list(self, request, *args, **kwargs):
        print(request.user.is_authenticated)
        all_questions = Question.objects.all().order_by('id')
        serializer = QuestionSerializer(all_questions, many=True)
        return Response(data=serializer.data)

    def create(self, request, *args, **kwargs):
        all_questions = request.data.pop('questions')
        user = self.request.user
        print(user)
        res = request.data
        # token = res.get('token')
        # email = request.data.get('email')
        print(res)
        for question in all_questions:
            current_question_id = question.get('question_id')
            new_user_form = UserForm()
            new_user_form.user = user
            new_user_form.question_id = current_question_id
            new_user_form.save()
            all_answers_ids = question.get('answer_id')
            for answer_id in all_answers_ids:
                new_user_form.answers.add(answer_id)
            new_user_form.save()
            print(question)
        user.done_form = True
        user.save()
        print(request.data)
        return Response(status=status.HTTP_201_CREATED)


def activate(request, uidb64, token, *args, **kwargs):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        template = render_to_string('static_template/after_ver_email.html', {})
        return HttpResponse(template)
    else:
        return HttpResponse('Activation link is invalid!')
