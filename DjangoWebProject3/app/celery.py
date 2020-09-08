from __future__ import absolute_import
import os
import datetime
from celery import Celery
from celery.schedules import crontab
import celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoWebProject3.settings')

app = Celery('DjangoWebProject3', backend='amqp', brocker='amqp://guest:guest@localhost:5672//')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('happy monday'),
    )


@app.task
def test(arg):
    print(arg)



#
# @app.task
# def add_days(days):
#     return datetime.datetime.now() + datetime.timedelta(days=days)
#
# @app.conf.update(
#     CELELYBEAT_SCHEDULE = {
#         'multiply-each-10-seconds':{
#             'task':'task.add_days',
#             'schedule':datetime.timedelta(seconds=10),
#             'args':(2, )
#
#         },
#     },
# )
