# Generated by Django 3.0.3 on 2020-04-02 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0028_course_mentor'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='position',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Чем занимается'),
        ),
    ]
