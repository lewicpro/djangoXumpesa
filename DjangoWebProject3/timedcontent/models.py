from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class timer(models.Model):
    user = models.OneToOneField(User, null=True)
    bal = models.PositiveIntegerField(blank=False, default=0.00)


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs['created']:
        user_profile = timer(user=user)
        user_profile.save()

post_save.connect(create_profile, sender=User)
