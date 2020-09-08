from .forms import *
from PIL import Image, ImageFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, render_to_response
from .models import *
from rest_framework.views import APIView
import schedule
from rest_framework import status
from django.core.paginator import Paginator
from braces.views import FormMessagesMixin
from django.utils.translation import ugettext_lazy as _
import datetime
from django.views.generic.edit import FormMixin
from django.http import HttpResponseForbidden
import operator
from django.http import HttpResponse
from functools import reduce
from rest_framework.response import Response
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.contrib import messages
from django.contrib import messages
from django.views.generic.edit import CreateView, DeleteView, FormMixin, UpdateView, ModelFormMixin
from django.views.generic import DetailView
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from rest_framework.views import APIView
from .models import *



class cryptohome(generic.ListView):
    model = Cryptoseller
    form_class = CrytpoForm
    template_name = "cryptohome.html"

    def get_queryset(self):
        return Cryptoseller.objects.all()


class CryptoSell(generic.CreateView):
    form_class = CrytpoForm
    template_name = "cryptoresell.html"
