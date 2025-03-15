import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roozham.settings')

app = Celery('roozham')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'publish-posts-every-minute': {
        'task': 'blog.tasks.publish_scheduled_posts',
        'schedule': crontab(hour='*/8'),
    },
}

app.conf.timezone = 'Asia/Tehran'
