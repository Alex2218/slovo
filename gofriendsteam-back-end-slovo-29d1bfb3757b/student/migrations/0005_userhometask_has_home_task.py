# Generated by Django 3.0.3 on 2020-03-18 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_userhometask_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userhometask',
            name='has_home_task',
            field=models.BooleanField(default=False),
        ),
    ]