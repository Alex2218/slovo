# Generated by Django 3.0.3 on 2020-03-19 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20200319_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhometask',
            name='status',
            field=models.CharField(choices=[('done', 'Сдано'), ('not_done', 'Не сдано'), ('wait', 'На проверке'), ('empty', 'Нет дз')], default='not_done', max_length=20),
        ),
    ]
