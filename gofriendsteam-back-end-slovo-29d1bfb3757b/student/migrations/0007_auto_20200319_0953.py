# Generated by Django 3.0.3 on 2020-03-19 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_auto_20200319_0905'),
        ('student', '0006_studentpackage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhometask',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.Package'),
        ),
    ]