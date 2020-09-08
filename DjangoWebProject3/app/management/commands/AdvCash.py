from django.core.management.base import BaseCommand, CommandError
from app.models import *
from app.views import recurence
import datetime
from django.utils import timezone


class Command(BaseCommand):
    help ='Daily profit multiplies'
    def handle(self, *args, **options):
        users = UserInfo.objects.all()
        advcashid = AdvCashDeposit.objects.all()
        for m in advcashid:
            ids = m.hashid
            if timezone.now() > m.closes:
                if m.sign == Unconfirmed:
                    if m.a_amount > 2:
                        if m.Plan == 'After Plan':
                            advcash = AdvCashDeposit.objects.get(user=m.user, hashid=m.hashid)
                            bal = Investment.objects.get(user__username=advcash.user)
                            amounte = UserInfo.objects.get(user__username=advcash.user)
                            prie = Processors.objects.get(user__username=advcash.user)
                            mor = AdvCashDeposit.objects.filter(user=advcash.user, hashid=advcash.hashid).update(sign=Confirmed)
                            amounte.amount = amounte.amount - advcash.a_amount
                            prie.adcash = prie.adcash + advcash.expectedIncome
                            bal.balance = bal.balance + advcash.expectedIncome
                            advcash.expectedIncome = advcash.expectedIncome * 0
                            advcash.a_amount = advcash.a_amount * 0
                            amounte.save()
                            prie.save()
                            advcash.save()
                            bal.save()

                        else:
                            advcash = AdvCashDeposit.objects.get(user=m.user, hashid=m.hashid)
                            bal = Investment.objects.get(user__username=advcash.user)
                            amounte = UserInfo.objects.get(user__username=advcash.user)
                            prie = Processors.objects.get(user__username=advcash.user)
                            mor = AdvCashDeposit.objects.filter(user=advcash.user, hashid=advcash.hashid).update(sign=Confirmed)
                            amounte.amount = amounte.amount - advcash.a_amount
                            prie.adcash = prie.adcash + advcash.a_amount
                            bal.balance = bal.balance + advcash.a_amount
                            advcash.a_amount = advcash.a_amount * 0
                            amounte.save()
                            prie.save()
                            advcash.save()
                            bal.save()