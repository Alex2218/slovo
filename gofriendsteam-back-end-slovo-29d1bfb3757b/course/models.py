from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from sortedm2m.fields import SortedManyToManyField


# Create your models here.
class Speaker(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя спикера')
    description = RichTextField()
    position = models.CharField(max_length=255, verbose_name='Чем занимается', blank=True, null=True)
    photo = models.ImageField(upload_to='speakers/', blank=True, null=True)
    is_lead = models.BooleanField(default=False, verbose_name='Лид спикер')

    def __str__(self):
        return "{} | {}".format(self.name, 'Лид' if self.is_lead else '')

    class Meta:
        verbose_name = 'Спикер'
        verbose_name_plural = 'Спикеры'


class Proffesion(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название проффесии')
    tags = models.ManyToManyField('users.Tag', verbose_name='Навыки', related_name='tags')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проффесия'
        verbose_name_plural = 'Проффесии'


class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название урока')
    description = RichTextField()

    # task = models.ForeignKey(HomeTask, on_delete=models.SET_NULL, default='', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_files(self):
        return LessonFile.objects.filter(lesson=self)

    def get_videos(self):
        return Video.objects.filter(lesson=self)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class HomeTaskFile(models.Model):
    file = models.FileField(upload_to='home_task/', blank=True, null=True, default='')


class HomeTask(models.Model):
    STATUS_CHOICES = (
        ('done', 'Сдано'),
        ('not_done', 'Не сдано'),
        ('wait', 'На проверке'),
    )
    file = models.ManyToManyField(HomeTaskFile, related_name='files')
    text = RichTextField(blank=True, null=True, default='')
    lesson = models.OneToOneField(Lesson, on_delete=models.CASCADE, blank=False, null=False, default='')

    def __str__(self):
        return 'Домашнее задание - {}'.format(self.text)

    # def get_file_by_user(self):
    #     return 'Есть файл' if self.file_answer else 'Нет файла'


class Video(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название видео', blank=True, null=True, default='')
    video_1080 = models.FileField(upload_to='lessons_video_1080/', blank=True, null=True)
    video_720 = models.FileField(upload_to='lessons_video_720/', blank=True, null=True)
    video_360 = models.FileField(upload_to='lessons_video_360/', blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='lesson_video', blank=True, null=True)

    def __str__(self):
        return 'Video {}'.format(self.lesson)


class LessonFile(models.Model):
    file = models.FileField(upload_to='lessons_files/', blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, default='', related_name='lesson_file',
                               blank=True, null=True)

    def __str__(self):
        return 'File {}'.format(self.lesson)


class Module(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название модуля')
    description = RichTextField(verbose_name='Описание модуля')
    lessons = SortedManyToManyField(Lesson, blank=True, null=True, default='')

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'


class Package(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название пакета')
    description = RichTextField()
    price = models.IntegerField(verbose_name='Цена')
    modules = SortedManyToManyField(Module, related_name='modules', null=True, blank=True)
    duration = models.CharField(max_length=255, blank=True, null=True,
                                default='', verbose_name='длительность')
    feature = models.CharField(max_length=500, verbose_name='Фича')
    is_sale = models.BooleanField(default=False, verbose_name='По акции')
    new_price = models.IntegerField(verbose_name='Новая цена ', blank=True, null=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True, null=True, default='')
    origin_package = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return "{} {} $ Кол-во модулей - {}".format(self.title, self.price, len(self.modules.all()))

    class Meta:
        verbose_name = 'Пакет'
        verbose_name_plural = 'Пакеты'

    @property
    def get_course(self):
        qs = Course.objects.filter(packages__in=[self]).first()
        return qs if qs else None


class Course(models.Model):
    title = models.CharField(verbose_name='Название курса', max_length=255)
    description = RichTextField()
    small_image = models.ImageField(upload_to='small_image_course/', blank=True, null=True, default='')
    full_image = models.ImageField(upload_to='full_image_course/', blank=True, null=True, default='')
    speaker = models.ForeignKey(Speaker, on_delete=models.SET_NULL,
                                null=True, verbose_name='Спикер')
    tags = models.ManyToManyField('users.Tag')
    proffesion = models.ForeignKey(Proffesion, on_delete=models.SET_NULL,
                                   null=True, blank=True, verbose_name='Проффесия')
    duration = models.CharField(max_length=255, blank=True, null=True,
                                default='', verbose_name='длительность')
    packages = SortedManyToManyField(Package, verbose_name='Пакеты', blank=True, null=True)
    mentor = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_packages(self):
        return ' , '.join([package.title for package in self.packages.all()])

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

# from .serializers import ArticleSerializers
class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок статьи')
    desc = models.TextField(max_length=500, verbose_name="Краткое описание статьи")
    lead  = models.TextField(max_length=500 , verbose_name='Ключевые моменты статьи (Лид)' , default='')
    content = RichTextUploadingField(verbose_name="Контент")
    status = models.BooleanField(default=True, verbose_name='В публикацию')
    image = models.ImageField(upload_to='articles/', blank=True, null=True, default='')
    count_views = models.IntegerField(default=0)
    date = models.DateField(auto_now=True)
    author  = models.ForeignKey(Speaker , on_delete=models.CASCADE , blank=True, null=True, default='')
    articles = SortedManyToManyField('self', verbose_name='Читайте также', blank=True, null=True)
