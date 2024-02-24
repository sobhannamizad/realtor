import celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','A.settings')
app = celery.Celery('A')
app.autodiscover_tasks()
app.conf.broker_url ='redis://127.0.0.1:6379/0'
app.conf.result_backend ='redis://127.0.0.1:6379/0'
app.conf.broker_connection_retry_on_startup =True