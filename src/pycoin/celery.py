import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pycoin.settings')

app = Celery('pycoin')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.beat_schedule = {
    #Scheduler Name
    'fetch-price': {
        # Task Name (Name Specified in Decorator)
        'task': 'fetch-price',  
        # Schedule      
        'schedule': 3600.0,
    },
}