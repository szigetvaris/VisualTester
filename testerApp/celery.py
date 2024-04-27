import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testerApp.settings')
app = Celery("testerApp")
app.config_from_object('django.conf:settings', namespace='CELERY')

@app.task
def random():
    return 'have a nice day, and go home!'

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)