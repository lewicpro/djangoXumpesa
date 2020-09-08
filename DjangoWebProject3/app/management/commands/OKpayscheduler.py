from django.core.management.base import BaseCommand, CommandError
from app.models import *
from app.views import recurence
import datetime
from django.utils import timezone


class Command(BaseCommand):
    help ='Daily profit multiplies'
    def handle(self, *args, **options):
        users = UserInfo.objects.all()
        OKpayid = OKpayDeoisitModel.objects.all()
        for m in OKpayid:
            ids = m.hashid
            if timezone.now() < m.closes:
                if m.sign == Unconfirmed:
                    if m.o_amount > 2:
                        if m.Plan == 'Daily Plan':
                            okpay = OKpayDeoisitModel.objects.get(user=m.user, hashid=m.hashid)
                            bal = Investment.objects.get(user__username=okpay.user)
                            amounte = UserInfo.objects.get(user__username=okpay.user)
                            prie = Processors.objects.get(user__username=okpay.user)

                            if okpay.package == Silver:
                                bal.balance = bal.balance + okpay.o_amount * 0.01
                                prie.payeer =prie.payeer + okpay.o_amount * 0.01

                            elif okpay.package == Tarnish:
                                bal.balance = bal.balance + okpay.o_amount * 4 / 100
                                prie.payeer = prie.payeer + okpay.o_amount * 4 / 100

                            elif okpay.package == Charoite:
                                bal.balance = bal.balance + okpay.o_amount * 6 / 100
                                prie.payeer = prie.payeer + okpay.o_amount * 6 / 100

                            elif okpay.package == TANZANITE:
                                bal.balance = bal.balance + okpay.o_amount * 0.8 /100
                                prie.payeer = prie.payeer + okpay.o_amount * 0.8 /100

                            elif okpay.package == Karat:
                                bal.balance = bal.balance + okpay.o_amount * 2.8/100
                                prie.payeer = prie.payeer + okpay.o_amount * 2.8/100

                            elif okpay.package == Corundum:
                                bal.balance = bal.balance + okpay.o_amount * 3.2/100
                                prie.payeer = prie.payeer + okpay.o_amount * 3.2/100

                            elif okpay.package == TITANIUM:
                                bal.balance = bal.balance + okpay.o_amount * 1.1/100
                                prie.payeer = prie.payeer + okpay.o_amount * 1.1/100

                            elif okpay.package == Niello:
                                bal.balance = bal.balance + payee.o_amount * 2.2/100
                                prie.payeer = prie.payeer + okpay.o_amount *  2.2/100

                            elif okpay.package == DIAMOND:
                                bal.balance = bal.balance + okpay.o_amount * 3 /100
                                prie.payeer = prie.payeer + okpay.o_amount * 3 /100

                            elif okpay.package == Quartz:
                                bal.balance = bal.balance + okpay.o_amount * 2.8/100
                                prie.payeer = prie.payeer + okpay.o_amount * 2.8/100

                            elif okpay.package == Carbon:
                                bal.balance = bal.balance + okpay.o_amount * 2.8/100
                                prie.payeer = prie.payeer + okpay.o_amount * 2.8/100

                            elif okpay.package == Gold:
                                bal.balance = bal.balance + okpay.o_amount * 1.4/100
                                prie.payeer = prie.payeer + okpay.o_amount * 1.4/100


                            elif okpay.package == Platnum:
                                bal.balance = bal.balance + okpay.o_amount * 2.8/100
                                prie.payeer = prie.payeer + okpay.o_amount * 2.8/100

                            elif okpay.package == Pearl:
                                bal.balance = bal.balance + okpay.o_amount * 3/100
                                prie.payeer = prie.payeer + okpay.o_amount * 3/100

                            amounte.save()
                            okpay.save()
                            prie.save()
                            bal.save()

