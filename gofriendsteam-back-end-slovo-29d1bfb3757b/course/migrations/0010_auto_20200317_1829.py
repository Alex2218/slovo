# Generated by Django 3.0.3 on 2020-03-17 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_auto_20200317_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hometask',
            name='lesson',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='course.Lesson'),
        ),
    ]
