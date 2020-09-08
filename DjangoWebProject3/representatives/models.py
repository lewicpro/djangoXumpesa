from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save


class Representative(models.Model):
    Accepted = 'Accepted'
    Not_requested = 'Not requested'
    Rejected = 'Rejected'
    Account_types = (
        (Accepted, 'Accepted'),
        (Not_requested, 'Not requested'),
        (Rejected, 'Rejected'),
    )
    user = models.OneToOneField(User, null=False)
    names = models.CharField(max_length=120, blank=False, null=False)
    country = models.CharField(max_length=120, blank=False, null=False)
    status = models.CharField(max_length=120, choices=Account_types, blank=False, default=Rejected)
    region = models.CharField(max_length=12, blank=False, null=False)
    phone = models.CharField(max_length=12, blank=False, null=False)
    social_media = models.CharField(max_length=12, blank=False)
    last_online = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name_plural = "Our representatives"

    def __str__(self):
        return self.user.username


class Suggest(models.Model):
    user = models.CharField(max_length=120, blank=False, null=True)
    subject = models.CharField(max_length=40, blank=False, null=False)
    suggestion = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name_plural = "Representative suggestions"

    def __str__(self):
        return self.user







def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs['created']:
        user_profile = Representative(user=user)
        user_profile.save()
        Already=Suggest(user=user)
        Already.save()

post_save.connect(create_profile, sender=User)
