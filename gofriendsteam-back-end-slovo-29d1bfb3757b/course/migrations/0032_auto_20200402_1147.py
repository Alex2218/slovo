# Generated by Django 3.0.3 on 2020-04-02 11:47

from django.db import migrations
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0031_auto_20200402_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='packages',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, null=True, to='course.Package', verbose_name='Пакеты'),
        ),
    ]
