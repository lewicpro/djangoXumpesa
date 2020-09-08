from django.contrib import admin

from .models import timer


class timerAdmin(admin.ModelAdmin):
    list_display = ['user', 'bal']

admin.site.register(timer, timerAdmin)
