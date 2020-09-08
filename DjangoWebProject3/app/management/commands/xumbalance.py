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
            if timezone.now() > m.closes:
                if m.sign == Unconfirmed:
                    if m.amount_transfered > 2:
                        if m.Plan == 'After Plan':
                            xum = BalanceRedeposit.objects.get(user=m.user, hashid=m.hashid)
                            bal = Investment.objects.get(user__username=xum.user)
                            amounte = UserInfo.objects.get(user__username=xum.user)
                            mor = BalanceRedeposit.objects.filter(user=xum.user, hashid=xum.hashid).update(sign=Confirmed)
                            amounte.amount = amounte.amount - xum.amount_transfered
                            bal.balance = bal.balance + xum.amount_transfered
                            bal.balance = bal.balance + xum.expectedIncome
                            xum.expectedIncome = xum.expectedIncome * 0
                            xum.amount_transfered = xum.amount_transfered * 0
                            amounte.save()
                            xum.save()
                            bal.save()

                        else:
                            xum = BalanceRedeposit.objects.get(user=m.user, hashid=m.hashid)
                            bal = Investment.objects.get(user__username=xum.user)
                            amounte = UserInfo.objects.get(user__username=xum.user)
                            mor = BalanceRedeposit.objects.filter(user=xum.user, hashid=xum.hashid).update(sign=Confirmed)
                            amounte.amount = amounte.amount - xum.amount_transfered
                            bal.balance = bal.balance + xum.amount_transfered
                            xum.amount_transfered = xum.amount_transfered * 0
                            amounte.save()
                            xum.save()
                            bal.save()