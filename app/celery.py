import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'matches.settings')

app = Celery('app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'matches-collect': {
        'task': 'app.tasks.update_matches',
        'schedule': crontab(minute="*/2"),
    },
    'alert-today': {
        'task': 'app.tasks.alert_matches_today',
        'schedule': crontab(hour="*/4"),
    },
    'alert-week': {
        'task': 'app.tasks.alert_matches_week',
        'schedule': crontab(hour="*/4", day_of_week="mon"),
    },
    'alert-predict': {
        'task': 'app.tasks.alert_matches_predict',
        'schedule': crontab(hour="*/4"),
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
