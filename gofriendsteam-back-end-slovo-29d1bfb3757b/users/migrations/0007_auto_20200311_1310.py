# Generated by Django 3.0.3 on 2020-03-11 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20200311_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='anwer',
            new_name='answer',
        ),
    ]
