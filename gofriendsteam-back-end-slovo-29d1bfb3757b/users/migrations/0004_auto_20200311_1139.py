# Generated by Django 3.0.3 on 2020-03-11 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200311_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.Tag'),
        ),
    ]
