# Generated by Django 3.0.3 on 2020-03-11 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200311_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='question',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='users.Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(default='', max_length=255, verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(default='', max_length=255, verbose_name='Интерес'),
        ),
        migrations.DeleteModel(
            name='UserForm',
        ),
    ]
