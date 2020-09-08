
from .forms import *

from django.shortcuts import render, redirect, render_to_response
from .models import *
from app.models import *


class PaginationMixin(object):
    fields = ['status']
    # def forms(self):
    #


class Messages(object):
    def mor(self):
        detor = UserInfo.objects.get(user=self.request.user.pk)
        gol = detor.user
        Accep = AcceptedApp.objects.filter(applier=gol)
        return Accep