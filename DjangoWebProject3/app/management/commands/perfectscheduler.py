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
            if timezone.now() < m.closes:
                if m.sign == Unconfirmed:
                    if m.PAYMENT_AMOUNT > 2:
                        if m.Plan == 'Daily Plan':
                            perfect = TransactionPerfectMoney.objects.get(user=m.user, hashid=m.hashid)
                            bal = Investment.objects.get(user__username=perfect.user)
                            amounte = UserInfo.objects.get(user__username=perfect.user)
                            prie = Processors.objects.get(user__username=perfect.user)
                            if perfect.package == Silver:
                                bal.balance = bal.balance + perfect.PAYMENT_AMOUNT * 0.01
                                prie.perfectmoney = prie.perfectmoney + perfect.PAYMENT_AMOUNT * 0.1

                            elif perfect.package == Tarnish:
                                bal.balance = bal.balance + perfect.PAYMENT_AMOUNT * 4 / 100
                                prie.perfectmoney = prie.perfectmoney + perfect.PAYMENT_AMOUNT * 4 / 100

                            elif perfect.package == Charoite:
                                bal.balance = bal.balance + perfect.PAYMENT_AMOUNT * 6 / 100
                                prie.perfectmoney = prie.perfectmoney + perfect.PAYMENT_AMOUNT * 6 / 100

                            elif perfect.package == TANZANITE:
                                bal.balance = bal.balance + perfect.PAYMENT_AMOUNT * 0.8 / 100
                                prie.perfectmoney = prie.perfectmoney + perfect.PAYMENT_AMOUNT * 0.8 / 100

                            elif perfect.package == Karat:
                                bal.balance = bal.balance + perfect.PAYMENT_AMOUNT * 2.8 / 100
                                prie.perfectmoney = prie.perfectmoney + perfect.PAYMENT_AMOUNT *  2.8 / 100

                            elif perfect.package == Corundum:
                                bal.balance = bal.balance + perfect.PAYMENT_AMOUNT * 3.2 / 100
                                prie.perfectmoney = prie.perfectmoney + perfect.PAYMENT_AMOUNT * 3.2 / 100

                            elif perfect.package == TITANIUM:
                                bal.balance = bal.balance + perfect.PAYMENT_AMOUNT * 1.1 / 100
                                prie.perfectmoney = prie.perfectmoney + perfect.PAYMENT_AMOUNT * 1.1 / 100

                            elif perfect.package == Niello:
                                bal.balance = bal.balance + perfect.PAYMENT_AMOUNT * 2.2 / 100
                                prie.perfectmoney = prie.perfectmoney + perfect.PAYMENT_AMOUNT * 2.2 / 100

                            elif perfect.package == DIAMOND:
                                bal.balance = bal.balance + perfect.PAYMENT_AMOUNT * 3 / 100
                                prie.perfectmoney = prie.perfectmoney + perfect.PAYMENT_AMOUNT *  3 / 100

                            elif perfect.package == Quartz:
                                bal.balance = bal.balance + perfect.PAYMENT_AMOUNT * 2.8 / 100
                                prie.perfectmoney = prie.perfectmoney + perfect.PAYMENT_AMOUNT * 2.8 / 100

                            elif perfect.package == Carbon:
                                bal.balance = bal.balance + perfect.PAYMENT_AMOUNT * 2.8 / 100
                                prie.perfectmoney = prie.perfectmoney + perfect.PAYMENT_AMOUNT * 2.8 / 100

                            elif perfect.package == Gold:
                                bal.balance = bal.balance + perfect.PAYMENT_AMOUNT * 1.4 / 100
                                prie.perfectmoney = prie.perfectmoney + perfect.PAYMENT_AMOUNT * 1.4 / 100

                            elif perfect.package == Silver:
                                bal.balance = bal.balance + perfect.PAYMENT_AMOUNT * 0.01
                                prie.perfectmoney = prie.perfectmoney + perfect.PAYMENT_AMOUNT * 0.01

                            elif perfect.package == Platnum:
                                bal.balance = bal.balance + perfect.PAYMENT_AMOUNT * 2.8 / 100
                                prie.perfectmoney = prie.perfectmoney + perfect.PAYMENT_AMOUNT * 2.8 / 100

                            elif perfect.package == Pearl:
                                bal.balance = bal.balance + perfect.PAYMENT_AMOUNT * 3 / 100
                                prie.perfectmoney = prie.perfectmoney + perfect.PAYMENT_AMOUNT * 2.8 / 100

                            amounte.save()
                            prie.save()
                            perfect.save()
                            bal.save()