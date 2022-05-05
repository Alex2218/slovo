# Generated by Django 3.0.3 on 2020-03-18 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_userhometask'),
    ]

    operations = [
        migrations.AddField(
            model_name='userhometask',
            name='status',
            field=models.CharField(choices=[('done', 'Сдано'), ('not_done', 'Не сдано'), ('wait', 'На проверке')], default='not_done', max_length=20),
        ),
    ]