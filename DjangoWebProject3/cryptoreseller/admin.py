from django.contrib import admin
from .models import *




class CryptoAdmin(admin.ModelAdmin):
    list_display = ["username", "balance_amount", "exchanger", "Give", "Get", "Reserve", "Reviews"]

admin.site.register(Cryptoseller, CryptoAdmin)
