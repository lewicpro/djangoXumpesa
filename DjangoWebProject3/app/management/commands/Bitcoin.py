from django.core.management.base import BaseCommand, CommandError
from app.models import *
from app.views import recurence
import datetime
from django.utils import timezone


class Command(BaseCommand):
    help ='Daily profit multiplies'
    def handle(self, *args, **options):
        users = UserInfo.objects.all()
        Bitcoinid = BitcoinRedepositModels.objects.all()
        for m in Bitcoinid:
            ids = m.hashid
            if timezone.now() > m.closes:
                if m.sign == Unconfirmed:
                    if m.b_amount > 0:
                        if m.Plan == 'After Plan':
                            Bitcoin = BitcoinRedepositModels.objects.get(user=m.user, hashid=m.hashid)
                            bal = Investment.objects.get(user__username=Bitcoin.user)
                            amounte = UserInfo.objects.get(user__username=Bitcoin.user)
                            prie = Processors.objects.get(user__username=Bitcoin.user)
                            mor = BitcoinRedepositModels.objects.filter(user=Bitcoin.user, hashid=Bitcoin.hashid).update(sign=Confirmed)
                            amounte.bitcoin_amount = amounte.bitcoin_amount - Bitcoin.b_amount
                            prie.bitcoin = prie.bitcoin + Bitcoin.expectedIncome
                            bal.Bitcoin_balance = bal.Bitcoin_balance + Bitcoin.expectedIncome
                            Bitcoin.expectedIncome = Bitcoin.expectedIncome * 0
                            Bitcoin.b_amount = Bitcoin.b_amount * 0
                            amounte.save()
                            prie.save()
                            Bitcoin.save()
                            bal.save()

                        else:

                            Bitcoin = BitcoinRedepositModels.objects.get(user=m.user, hashid=m.hashid)
                            bal = Investment.objects.get(user__username=Bitcoin.user)
                            amounte = UserInfo.objects.get(user__username=Bitcoin.user)
                            prie = Processors.objects.get(user__username=Bitcoin.user)
                            mor = BitcoinRedepositModels.objects.filter(user=Bitcoin.user, hashid=Bitcoin.hashid).update(sign=Confirmed)
                            amounte.bitcoin_amount = amounte.bitcoin_amount - Bitcoin.b_amount
                            prie.bitcoin = prie.bitcoin + Bitcoin.b_amount
                            bal.Bitcoin_balance = bal.Bitcoin_balance + Bitcoin.b_amount
                            Bitcoin.b_amount = Bitcoin.b_amount * 0
                            amounte.save()
                            Bitcoin.save()
                            prie.save()
                            bal.save()