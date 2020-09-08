from django import forms
from django.db.models import Count
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
User = get_user_model()
from .models import *
from django.contrib.auth.models import User


class RepresentativesForm(forms.ModelForm):
    names = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'names', 'style': 'width: 100%;'}))
    country = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'country', 'style': 'width: 100%'}))
    region = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'region', 'style': 'width: 100%'}))
    phone = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'phone', 'style': 'width: 100%'}))
    social_media = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'social media', 'style': 'width: 100%'}))

    class Meta:
        model = Representative
        fields = [
            'names',
            'country',
            'region',
            'phone',
            'social_media'
        ]


class SuggestForm(forms.ModelForm):
    suggestion = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '', 'style': 'width: 100%', 'class':'textinput text-center textInput form-control '}))
    subject = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))

    class Meta:
        model = Suggest
        fields = [
            'user',
            'subject',
            'suggestion'
        ]

