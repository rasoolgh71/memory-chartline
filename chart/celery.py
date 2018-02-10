import os
from celery import Celery
import os
from celery.schedules import crontab
from django.conf import settings
#from celery.decorators import periodic_task


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chart.settings')
app = Celery('chart')
app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
    'repeat_cheak': {
        'task': 'repeat_cheak',
        'schedule': crontab(minute='*/1'),
        'args': '',
    }
}

