from celery import Celery
from celery.schedules import crontab

app = Celery()


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


@app.task
def add(x, y):
    return x + y