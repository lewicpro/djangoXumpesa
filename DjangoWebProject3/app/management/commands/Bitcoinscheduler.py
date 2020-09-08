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
            if timezone.now() < m.closes:
                if m.sign == Unconfirmed:
                    if m.b_amount > 0:
                        if m.Plan == 'Daily Plan':
                            Bitcoin = BitcoinRedepositModels.objects.get(user=m.user, hashid=m.hashid)
                            bal = Investment.objects.get(user__username=Bitcoin.user)
                            amounte = UserInfo.objects.get(user__username=Bitcoin.user)
                            prie =Processors.objects.get(user__username=Bitcoin.user)

                            if Bitcoin.package == Silver:
                                bal.Bitcoin_balance = bal.Bitcoin_balance + Bitcoin.b_amount * 0.01
                                prie.bitcoin = prie.bitcoin + Bitcoin.b_amount * 0.01

                            elif Bitcoin.package == Tarnish:
                                bal.balance = bal.balance + Bitcoin.b_amount * 4 / 100
                                prie.bitcoin = prie.bitcoin + Bitcoin.b_amount * 4 / 100

                            elif Bitcoin.package == Charoite:
                                bal.Bitcoin_balance = bal.Bitcoin_balance + Bitcoin.b_amount * 6 / 100
                                prie.bitcoin = prie.bitcoin + Bitcoin.b_amount * 6 / 100

                            elif Bitcoin.package == TANZANITE:
                                bal.Bitcoin_balance = bal.Bitcoin_balance + Bitcoin.b_amount * 0.8 /100
                                prie.bitcoin = prie.bitcoin + Bitcoin.b_amount * 0.8 /100

                            elif Bitcoin.package == Karat:
                                bal.Bitcoin_balance = bal.Bitcoin_balance + Bitcoin.b_amount * 2.8/100
                                prie.bitcoin = prie.bitcoin + Bitcoin.b_amount * 2.8/100

                            elif Bitcoin.package == Corundum:
                                bal.Bitcoin_balance = bal.Bitcoin_balance + Bitcoin.b_amount * 3.2/100
                                prie.bitcoin = prie.bitcoin + Bitcoin.b_amount *  3.2/100

                            elif Bitcoin.package == TITANIUM:
                                bal.Bitcoin_balance = bal.Bitcoin_balance + Bitcoin.b_amount * 1.1/100
                                prie.bitcoin = prie.bitcoin + Bitcoin.b_amount * 1.1/100

                            elif Bitcoin.package == Niello:
                                bal.Bitcoin_balance = bal.Bitcoin_balance + Bitcoin.b_amount * 2.2/100
                                prie.bitcoin = prie.bitcoin + Bitcoin.b_amount * 2.2/100

                            elif Bitcoin.package == DIAMOND:
                                bal.Bitcoin_balance = bal.Bitcoin_balance + Bitcoin.b_amount * 3 /100
                                prie.bitcoin = prie.bitcoin + Bitcoin.b_amount * 3 /100

                            elif Bitcoin.package == Quartz:
                                bal.Bitcoin_balance = bal.Bitcoin_balance + Bitcoin.b_amount * 0.8/100
                                prie.bitcoin = prie.bitcoin + Bitcoin.b_amount * 0.8/100

                            elif Bitcoin.package == Carbon:
                                bal.Bitcoin_balance = bal.Bitcoin_balance + Bitcoin.b_amount * 2.8/100
                                prie.bitcoin = prie.bitcoin + Bitcoin.b_amount * 2.8/100

                            elif Bitcoin.package == Gold:
                                bal.Bitcoin_balance = bal.Bitcoin_balance + Bitcoin.b_amount * 1.4/100
                                prie.bitcoin = prie.bitcoin + Bitcoin.b_amount * 1.4/100

                            elif Bitcoin.package == Silver:
                                bal.Bitcoin_balance = bal.Bitcoin_balance + Bitcoin.b_amount * 0.01
                                prie.bitcoin = prie.bitcoin + Bitcoin.b_amount * 0.01

                            elif Bitcoin.package == Platnum:
                                bal.Bitcoin_balance = bal.Bitcoin_balance + Bitcoin.b_amount * 2.8/100
                                prie.bitcoin = prie.bitcoin + Bitcoin.b_amount * 2.8/100

                            elif Bitcoin.package == Pearl:
                                bal.Bitcoin_balance = bal.Bitcoin_balance + Bitcoin.b_amount * 3/100
                                prie.bitcoin = prie.bitcoin + Bitcoin.b_amount * 3/100

                            amounte.save()
                            Bitcoin.save()
                            prie.save()
                            bal.save()

