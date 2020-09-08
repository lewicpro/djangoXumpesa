from django.test import TestCase

# Create your tests here.
from django.db import models

class UserInfo(models.Model):
    full_name = models.CharField(max_length=120, blank=True, null=True)
    email = models.EmailField()
    phone_no = models.CharField(max_length=14)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, default=0)

    def __str__(self):
        return self.email
