from django.core.management.base import BaseCommand, CommandError
from app.models import *
from app.views import recurence
import datetime
from django.utils import timezone


class Command(BaseCommand):
    help ='Daily profit multiplies'
    def handle(self, *args, **options):
        users = UserInfo.objects.all()
        payeeid = TransactionPayeer.objects.all()
        for m in payeeid:
            ids = m.hashid
            if timezone.now() > m.closes:
                if m.sign == Unconfirmed:
                    if m.m_amount > 2:
                        if m.Plan == 'After Plan':
                            payee = TransactionPayeer.objects.get(user=m.user, hashid=m.hashid)
                            bal = Investment.objects.get(user__username=payee.user)
                            amounte = UserInfo.objects.get(user__username=payee.user)
                            prie = Processors.objects.get(user__username=payee.user)
                            print(payee.user)
                            mor = TransactionPayeer.objects.filter(user=payee.user, hashid=payee.hashid).update(sign=Confirmed)
                            amounte.amount = amounte.amount - payee.m_amount
                            bal.balance = bal.balance + payee.expectedIncome
                            prie.payeer = prie.payeer + payee.expectedIncome
                            payee.m_amount = payee.m_amount * 0
                            payee.expectedIncome = payee.expectedIncome * 0
                            amounte.save()
                            payee.save()
                            prie.save()
                            bal.save()
                        else:
                            payee = TransactionPayeer.objects.get(user=m.user, hashid=m.hashid)
                            bal = Investment.objects.get(user__username=payee.user)
                            amounte = UserInfo.objects.get(user__username=payee.user)
                            prie = Processors.objects.get(user__username=payee.user)
                            print(payee.user)
                            mor = TransactionPayeer.objects.filter(user=payee.user, hashid=payee.hashid).update(sign=Confirmed)
                            amounte.amount = amounte.amount - payee.m_amount
                            prie.payeer = prie.payeer + payee.m_amount
                            bal.balance = bal.balance + payee.m_amount
                            payee.m_amount = payee.m_amount * 0
                            amounte.save()
                            payee.save()
                            prie.save()
                            bal.save()




