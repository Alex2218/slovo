from django.db import models
import uuid
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from .constants import ROLE_USER

from .managers import CustomUserManager


def validate_message_content(content):
    if content is None or content == "" or content.isspace():
        raise ValidationError(
            'Content is empty or invalid',
            code='invalid',
            params={
                'content': content
            }
        )


# google client_id 972869637602-absn6th5vggmp7cu59r0b68smhrnhnc3.apps.googleusercontent.com
# google client_secret zhNg-IjxocC8eFk40Rn8hrf5
import uuid


class User(AbstractUser):
    username = None
    online = models.BooleanField(null=False, blank=False, default=False)
    last_read_date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    email = models.EmailField(unique=True, null=True, verbose_name='Емейл')
    role = models.CharField(choices=ROLE_USER, max_length=25, verbose_name='Роль пользователя', default=ROLE_USER[0][0])
    done_form = models.BooleanField(default=False, verbose_name='Анкета пройдена')
    referred = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL , verbose_name='Кто пригласил')
    referral_code = models.UUIDField(
        default=uuid.uuid4,
        editable=False)
    referral_bonus = models.BooleanField(default=False)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.id} {self.email}' or 'empty email'

    def read(self):
        self.last_read_date = timezone.now()
        self.save()


class Question(models.Model):
    question = models.CharField(max_length=255, verbose_name='Вопрос', default='')

    def __str__(self):
        return "Вопрос - " + self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Tag(models.Model):
    tag = models.CharField(max_length=255, verbose_name='Интерес', default='', blank=True, null=True)

    def __str__(self):
        return self.tag


class Answer(models.Model):
    answer = models.CharField(verbose_name='Ответ', max_length=255, default='')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', default='')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class UserForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default='')
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, blank=True, null=True, default='')
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return self.user.__str__()

    class Meta:
        verbose_name = 'Ответ студента'
        verbose_name_plural = 'Ответы студентов'



class CallBack(models.Model):
    name = models.CharField(max_length=255 , verbose_name='Имя')
    phone = models.CharField(max_length=150 , verbose_name='Номер телефона')
    status = models.BooleanField(default=False , verbose_name='Обработана заявка')
    date = models.DateTimeField(auto_now_add=True)
    __str__ = lambda self : f'{self.name} {self.phone}'