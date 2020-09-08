from django import forms
from .models import *
from app.models import *
from io import StringIO
from PIL import Image
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime

class CrytpoForm(forms.ModelForm):
    class Meta:
        model = Cryptoseller
        fields = [
            'username',
            'balance_amount',
            'exchanger',
            'currency',
            'Reserve',
            'Get',
            'Give'
        ]