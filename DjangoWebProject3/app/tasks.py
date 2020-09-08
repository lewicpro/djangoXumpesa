from __future__ import absolute_import, unicode_literals
from celery import shared_task

from app.models import UserInfo
from celery import Celery
from celery.schedules import crontab
# from celery.registry import tasks
from django.conf import settings
from django.core.mail import send_mail
from celery.task import Task
# from celery.task import task
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from app.models import Investment
from datetime import timedelta
import datetime
import time
from celery.schedules import crontab
from .celery import app


@app.task
def add(y, b):
    result = y + b
    return result


app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'app.tasks.add',
        'schedule': datetime.timedelta(seconds=10),
        'args': (2, 3)
    },
}

app.conf.timezone = 'UTC'

@app.task
def Schedure(sender):
    pass





# class SignupTask(Task):
#     def run(self, user):
#         subject, from_email, to = 'Welcome', 'lewicpro@yahoo.com', user.userInfo
#
#         html_content = render_to_string('ProductsDetails.html', {'user': user})
#         text_content = strip_tags(html_content)
#         msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
#         msg.attach_alternative(html_content, "text/html")
#         msg.send()
# @app.task
# class confirmation(Task):
#     def run(self, user):
#         subject = 'thank you for sign up'
#         message = 'we weill be in touch soon'
#         from_email = settings.EMAIL_HOST_USER
#         to_list = [user.email, settings.EMAIL_HOST_USER]
#         send_mail(subject, message, from_email, to_list, fail_silently=True)



# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(10.0, test.s('hell'), name='add every 10')
#
#     sender.add_periodic_task(30.0, test.s('worl'), expires=10)
#
#     sender.add_periodic_task(
#         crontab(),
#         test.s('happy mondays!'),
#     )
#
#
# @app.task
# def test(arg):
#     print(arg)


@shared_task
def mul(x, y):
    time.sleep(20)
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)




# class signupTasks(Task):
#
#     def run(selfself, user):
#         subject, from_email, to = 'welcome', 'lewicpro@gmail.com', user.email
#         html_content = render_to_string('ProductsDetails.html', {'user': user.first_name})
#         text_content = strip_tags(html_content)

# def duration():
#     oneMinutes = datetime.timedelta(minutes=1)
#     start = datetime.datetime.now() + oneMinutes
#     while datetime.datetime.now() < start:
#         time.sleep(1)
#     Investment.balance = Investment.amount * 0.02 + Investment.amount
#     Investment.save()




