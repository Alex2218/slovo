# Generated by Django 3.0.3 on 2020-03-20 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_user_done_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='MentorUser',
            fields=[
            ],
            options={
                'verbose_name': 'Ментор',
                'verbose_name_plural': 'Менторы',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
        ),
        migrations.CreateModel(
            name='StudentUser',
            fields=[
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
        ),
    ]