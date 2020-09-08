from django.core.management.base import BaseCommand, CommandError
from app.models import *
from app.views import recurence
import datetime
from django.utils import timezone


class Command(BaseCommand):
    help ='Daily profit multiplies'
    def handle(self, *args, **options):
        users = UserInfo.objects.all()
        perfectid = TransactionPerfectMoney.objects.all()
        for m in perfectid:
            ids = m.hashid
            if timezone.now() > m.closes:
                if m.sign == Unconfirmed:
                    if m.PAYMENT_AMOUNT > 2:
                        if m.Plan == 'After Plan':
                            perfect = TransactionPerfectMoney.objects.get(user=m.user, hashid=m.hashid)
                            bal = Investment.objects.get(user__username=perfect.user)
                            amounte = UserInfo.objects.get(user__username=perfect.user)
                            prie = Processors.objects.get(user__username=perfect.user)
                            mor = TransactionPerfectMoney.objects.filter(user=perfect.user, hashid=perfect.hashid).update(sign=Confirmed)
                            amounte.amount = amounte.amount - perfect.PAYMENT_AMOUNT
                            prie.perfectmoney = prie.perfectmoney + perfect.expectedIncome
                            bal.balance = bal.balance + perfect.expectedIncome
                            perfect.expectedIncome = perfect.expectedIncome * 0
                            perfect.PAYMENT_AMOUNT = perfect.PAYMENT_AMOUNT * 0
                            prie.save()
                            amounte.save()
                            perfect.save()
                            bal.save()

                        else:

                            perfect = TransactionPerfectMoney.objects.get(user=m.user, hashid=m.hashid)
                            bal = Investment.objects.get(user__username=perfect.user)
                            amounte = UserInfo.objects.get(user__username=perfect.user)
                            prie = Processors.objects.get(user__username=perfect.user)
                            mor = TransactionPerfectMoney.objects.filter(user=perfect.user, hashid=perfect.hashid).update(sign=Confirmed)
                            amounte.amount = amounte.amount - perfect.PAYMENT_AMOUNT
                            prie.perfectmoney = prie.perfectmoney + perfect.PAYMENT_AMOUNT
                            bal.balance = bal.balance + perfect.PAYMENT_AMOUNT
                            perfect.PAYMENT_AMOUNT = perfect.PAYMENT_AMOUNT * 0
                            amounte.save()
                            perfect.save()
                            prie.save()
                            bal.save()