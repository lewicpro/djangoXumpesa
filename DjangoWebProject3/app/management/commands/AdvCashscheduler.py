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
            if timezone.now() < m.closes:
                if m.sign == Unconfirmed:
                    if m.a_amount > 2:
                        if m.Plan == 'Daily Plan':
                            advcash = AdvCashDeposit.objects.get(user=m.user, hashid=m.hashid)
                            bal = Investment.objects.get(user__username=advcash.user)
                            amounte = UserInfo.objects.get(user__username=advcash.user)
                            prie = Processors.objects.get(user__username=advcash.user)

                            if advcash.package == Silver:
                                bal.balance = bal.balance + advcash.a_amount * 0.01
                                prie.adcash = prie.adcash + advcash.a_amount * 0.01

                            elif advcash.package == Tarnish:
                                bal.balance = bal.balance + advcash.a_amount * 4 / 100
                                prie.adcash = prie.adcash + advcash.a_amount *  4 / 100

                            elif advcash.package == Charoite:
                                bal.balance = bal.balance + advcash.a_amount * 6 / 100
                                prie.adcash = prie.adcash + advcash.a_amount * 6 / 100

                            elif advcash.package == TANZANITE:
                                bal.balance = bal.balance + advcash.a_amount * 0.8 /100
                                prie.adcash = prie.adcash + advcash.a_amount * 0.8 /100

                            elif advcash.package == Karat:
                                bal.balance = bal.balance + advcash.a_amount * 2.8/100
                                prie.adcash = prie.adcash + advcash.a_amount * 2.8/100

                            elif advcash.package == Corundum:
                                bal.balance = bal.balance + advcash.a_amount * 3.2/100
                                prie.adcash = prie.adcash + advcash.a_amount * 3.2/100

                            elif advcash.package == TITANIUM:
                                bal.balance = bal.balance + advcash.a_amount * 1.1/100
                                prie.adcash = prie.adcash + advcash.a_amount * 1.1/100

                            elif advcash.package == Niello:
                                bal.balance = bal.balance + advcash.a_amount * 2.2/100
                                prie.adcash = prie.adcash + advcash.a_amount * 2.2/100

                            elif advcash.package == DIAMOND:
                                bal.balance = bal.balance + advcash.a_amount * 3 /100
                                prie.adcash = prie.adcash + advcash.a_amount * 3 /100

                            elif advcash.package == Quartz:
                                bal.balance = bal.balance + advcash.a_amount * 0.8/100
                                prie.adcash = prie.adcash + advcash.a_amount * 0.8/100

                            elif advcash.package == Carbon:
                                bal.balance = bal.balance + advcash.a_amount * 2.8/100
                                prie.adcash = prie.adcash + advcash.a_amount * 2.8/100

                            elif advcash.package == Gold:
                                bal.balance = bal.balance + advcash.a_amount * 1.4/100
                                prie.adcash = prie.adcash + advcash.a_amount * 1.4/100

                            elif advcash.package == Silver:
                                bal.balance = bal.balance + advcash.a_amount * 0.01
                                prie.adcash = prie.adcash + advcash.a_amount * 0.01

                            elif advcash.package == Platnum:
                                bal.balance = bal.balance + advcash.a_amount * 2.8/100
                                prie.adcash = prie.adcash + advcash.a_amount * 2.8/100

                            elif advcash.package == Pearl:
                                bal.balance = bal.balance + advcash.a_amount * 3/100
                                prie.adcash = prie.adcash + advcash.a_amount * 3/100
                            amounte.save()
                            advcash.save()
                            prie.save()
                            bal.save()

