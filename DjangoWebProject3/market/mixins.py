
from .forms import *

from django.shortcuts import render, redirect, render_to_response
from .models import *



class PaginationMixin(object):
    fields = ['status']
    # def forms(self):
    #
