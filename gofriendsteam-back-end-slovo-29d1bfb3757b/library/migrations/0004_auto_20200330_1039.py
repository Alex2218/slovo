# Generated by Django 3.0.3 on 2020-03-30 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_singlevideo_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleVideoStudent',
            fields=[
            ],
            options={
                'verbose_name': 'Видео студента',
                'verbose_name_plural': 'Видео студентов',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('library.singlevideo',),
        ),
        migrations.AddField(
            model_name='singlevideo',
            name='origin_video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.SingleVideo'),
        ),
        migrations.AlterField(
            model_name='videoorder',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Потвердить заказ'),
        ),
    ]
