# Generated by Django 3.0.3 on 2020-03-13 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200311_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='done_form',
            field=models.BooleanField(default=False, verbose_name='Анкета пройдена'),
        ),
    ]