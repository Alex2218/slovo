from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'slovo_backend.settings')

app = Celery('slovo_backend')
# app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()

app.conf.CELERYBEAT_SCHEDULE = {

}
