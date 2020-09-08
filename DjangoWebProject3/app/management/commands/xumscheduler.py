from django.core.management.base import BaseCommand, CommandError
from app.models import *
from app.views import recurence
import datetime
from django.utils import timezone


class Command(BaseCommand):
    help ='Daily profit multiplies'
    def handle(self, *args, **options):
        users = UserInfo.objects.all()
        xumid = BalanceRedeposit.objects.all()
        for m in xumid:
            ids = m.hashid
            if timezone.now() < m.closes:
                if m.sign == Unconfirmed:
                    if m.amount_transfered > 2:
                        if m.Plan == 'Daily Plan':
                            xum = BalanceRedeposit.objects.get(user=m.user, hashid=m.hashid)
                            bal = Investment.objects.get(user__username=xum.user)
                            amounte = UserInfo.objects.get(user__username=xum.user)
                            if xum.package == Silver:
                                bal.balance = bal.balance + xum.amount_transfered * 0.01

                            elif xum.package == Tarnish:
                                bal.balance = bal.balance + xum.amount_transfered * 4 / 100

                            elif xum.package == Charoite:
                                bal.balance = bal.balance + xum.amount_transfered * 6 / 100

                            elif xum.package == TANZANITE:
                                bal.balance = bal.balance + xum.amount_transfered * 0.8 / 100

                            elif xum.package == Karat:
                                bal.balance = bal.balance + xum.amount_transfered * 2.8 / 100

                            elif xum.package == Corundum:
                                bal.balance = bal.balance + xum.amount_transfered * 3.2 / 100

                            elif xum.package == TITANIUM:
                                bal.balance = bal.balance + xum.amount_transfered * 1.1 / 100

                            elif xum.package == Niello:
                                bal.balance = bal.balance + xum.amount_transfered * 2.2 / 100

                            elif xum.package == DIAMOND:
                                bal.balance = bal.balance + xum.amount_transfered * 3 / 100

                            elif xum.package == Quartz:
                                bal.balance = bal.balance + xum.amount_transfered * 0.8 / 100

                            elif xum.package == Carbon:
                                bal.balance = bal.balance + xum.amount_transfered * 2.8 / 100

                            elif xum.package == Gold:
                                bal.balance = bal.balance + xum.amount_transfered * 1.4 / 100

                            elif xum.package == Silver:
                                bal.balance = bal.balance + xum.amount_transfered * 0.01

                            elif xum.package == Platnum:
                                bal.balance = bal.balance + xum.amount_transfered * 2.8 / 100

                            elif xum.package == Pearl:
                                bal.balance = bal.balance + xum.amount_transfered * 3 / 100
                            amounte.save()
                            xum.save()
                            bal.save()