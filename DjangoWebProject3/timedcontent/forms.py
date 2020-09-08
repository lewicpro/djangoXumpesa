from django import forms
from .models import timer


class timerForm(forms.ModelForm):

    class Mete:
        models = timer
        fields = [
            'bal',
        ]