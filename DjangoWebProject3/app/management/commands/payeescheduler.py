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
            if timezone.now() < m.closes:
                if m.sign == Unconfirmed:
                    if m.m_amount > 2:
                        if m.Plan == 'Daily Plan':
                            payee = TransactionPayeer.objects.get(user=m.user, hashid=m.hashid)
                            bal = Investment.objects.get(user__username=payee.user)
                            amounte = UserInfo.objects.get(user__username=payee.user)
                            prie = Processors.objects.get(user__username=payee.user)

                            if payee.package == Silver:
                                bal.balance = bal.balance + payee.m_amount * 0.01
                                prie.payeer =prie.payeer + payee.m_amount * 0.01

                            elif payee.package == Tarnish:
                                bal.balance = bal.balance + payee.m_amount * 4 / 100
                                prie.payeer = prie.payeer + payee.m_amount * 4/ 100

                            elif payee.package == Charoite:
                                bal.balance = bal.balance + payee.m_amount * 6 / 100
                                prie.payeer = prie.payeer + payee.m_amount * 6/100

                            elif payee.package == TANZANITE:
                                bal.balance = bal.balance + payee.m_amount * 0.8 /100
                                prie.payeer = prie.payeer + payee.m_amount * 0.8/100

                            elif payee.package == Karat:
                                bal.balance = bal.balance + payee.m_amount * 2.8/100
                                prie.payeer = prie.payeer + payee.m_amount * 2.8/100

                            elif payee.package == Corundum:
                                bal.balance = bal.balance + payee.m_amount * 3.2/100
                                prie.payeer = prie.payeer + payee.m_amount * 3.2/100

                            elif payee.package == TITANIUM:
                                bal.balance = bal.balance + payee.m_amount * 1.1/100
                                prie.payeer = prie.payeer + payee.m_amount * 1.1 / 100

                            elif payee.package == Niello:
                                bal.balance = bal.balance + payee.m_amount * 2.2/100
                                prie.payeer = prie.payeer + payee.m_amount * 2.2/100

                            elif payee.package == DIAMOND:
                                bal.balance = bal.balance + payee.m_amount * 3 /100
                                prie.payeer = prie.payeer + payee.m_amount * 3 /100

                            elif payee.package == Quartz:
                                bal.balance = bal.balance + payee.m_amount * 2.8/100
                                prie.payeer = prie.payeer + payee.m_amount * 2.8/ 100

                            elif payee.package == Carbon:
                                bal.balance = bal.balance + payee.m_amount * 2.8/100
                                prie.payeer = prie.payeer + payee.m_amount * 2.8/ 100

                            elif payee.package == Gold:
                                bal.balance = bal.balance + payee.m_amount * 1.4/100
                                prie.payeer = prie.payeer + payee.m_amount * 1.4/ 100

                            elif payee.package == Silver:
                                bal.balance = bal.balance + payee.m_amount * 0.01
                                prie.payeer = prie.payeer + payee.m_amount * 1 / 100

                            elif payee.package == Platnum:
                                bal.balance = bal.balance + payee.m_amount * 2.8/100
                                prie.payeer = prie.payeer + payee.m_amount * 2.8/ 100

                            elif payee.package == Pearl:
                                bal.balance = bal.balance + payee.m_amount * 3/100
                                prie.payeer = prie.payeer + payee.m_amount * 3 / 100

                            amounte.save()
                            payee.save()
                            bal.save()




