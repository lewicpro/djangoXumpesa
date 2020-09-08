from django.core.management.base import BaseCommand, CommandError
from app.models import *
from app.views import recurence
import datetime
from django.utils import timezone


class Command(BaseCommand):
    help ='Daily profit multiplies'
    def handle(self, *args, **options):
        users = UserInfo.objects.all()
        okpayid = OKpayDeoisitModel.objects.all()
        for m in okpayid:
            ids = m.hashid
            if timezone.now() > m.closes:
                if m.sign == Unconfirmed:
                    if m.o_amount > 2:
                        if m.Plan == 'After Plan':
                            okpay = OKpayDeoisitModel.objects.get(user=m.user, hashid=m.hashid)
                            bal = Investment.objects.get(user__username=okpay.user)
                            amounte = UserInfo.objects.get(user__username=okpay.user)
                            prie = Processors.objects.get(user__username=okpay.user)
                            mor = OKpayDeoisitModel.objects.filter(user=okpay.user, hashid=okpay.hashid).update(sign=Confirmed)
                            amounte.amount = amounte.amount - okpay.o_amount
                            prie.okpay = prie.okpay + okpay.expectedIncome
                            bal.balance = bal.balance + okpay.expectedIncome
                            okpay.expectedIncome = okpay.expectedIncome * 0
                            okpay.o_amount = okpay.o_amount * 0
                            amounte.save()
                            okpay.save()
                            prie.save()
                            bal.save()

                        else:

                            okpay = OKpayDeoisitModel.objects.get(user=m.user, hashid=m.hashid)
                            bal = Investment.objects.get(user__username=okpay.user)
                            amounte = UserInfo.objects.get(user__username=okpay.user)
                            prie = Processors.objects.get(user__username=okpay.user)
                            mor = OKpayDeoisitModel.objects.filter(user=okpay.user, hashid=okpay.hashid).update(sign=Confirmed)
                            amounte.amount = amounte.amount - okpay.o_amount
                            prie.okpay = prie.okpay + okpay.o_amount
                            bal.balance = bal.balance + okpay.o_amount
                            okpay.o_amount = okpay.o_amount * 0
                            amounte.save()
                            okpay.save()
                            prie.save()
                            bal.save()