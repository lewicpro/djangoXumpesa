from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery import Celery
import datetime

app = Celery('market', backend='amqp')
@app.task
def add(days):
    return datetime.datetime.now() + datetime.timedelta(days=days)
app.conf.update(
    CELERYBEAT_SCHEDULE={
        'add-every-30-seconds': {
            'task': 'tasks.add',
            'schedule': datetime.timedelta(seconds=10),
            'args': (2, )
        },
    },
)
# @shared_task
# def add(x, y):
#     return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)