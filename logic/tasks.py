import os
import time

from celery import Celery
from celery.schedules import crontab

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")
#  Раскомментируйте эти линии, чтобы принтовать хеллоу каждые 5 секунд
celery.conf.beat_schedule = {
        'periodic_task-every-minute': {
            'task': 'custom_task',
            'schedule': 5
        }
    }
celery.conf.timezone = 'UTC'


@celery.task(name='custom_task')
def custom_task():
    print('hello')
