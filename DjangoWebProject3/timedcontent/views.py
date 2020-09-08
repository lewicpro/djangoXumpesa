from django.shortcuts import render
from .models import *
from .forms import *
from app.models import *
import time
import datetime


def account_time(request):
    if request.user.is_authenticated():
        acco = Investment.objects.get(user=request.user.pk)
        instance = timer.objects.get(user=request.user.pk)
        form = timerForm(request.POST or None, instance=instance)
        if form.is_valid():
            #user = form.save(commit=False)
            #user.save()
            instance = form.save(commit=False)
            oneMinutes = datetime.timedelta(seconds=10)
            start = datetime.datetime.now() + oneMinutes
            while datetime.datetime.now() < start:
                time.sleep(1)
            acco.balance = instance.bal * 0.02 + instance.bal
            acco.save()
            instance.save()
