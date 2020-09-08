from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
import time, subprocess
import datetime
from rest_framework.views import APIView
import schedule
from rest_framework import status
from django.contrib.auth import logout as django_logout
from .serializers import AppSerializers
from django.shortcuts import render, redirect, get_object_or_404
from timedcontent.models import timer
from django.contrib import messages
from django.http import Http404
from rest_framework.response import Response
from django.utils import timezone
timezone.now().date()
from django.views.generic.edit import CreateView, DeleteView, FormMixin, UpdateView, ModelFormMixin
from django.views.generic import DetailView
from django.views import generic
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.http import Http404
from django.contrib.auth import update_session_auth_hash
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from .models import *
import binascii
import hashlib
import base64
from .conversion import *


# def activate_user_view(request, code=None, *args, **kwargs):
#     if code:
#         qs = UserInfo.objects.filter(shortcode=code)
#         if qs.exists() and qs.count() == 1:
#             profile = qs.first()
#             if not profile.activated:
#                 user_ = profile.user
#                 user_.is_active = True
#                 user_.save()
#                 profile.activated = True
#                 profile.shortcode=None
#                 profile.save()
#                 return redirect(reverse('app:login'))
#     return redirect(reverse('app:login'))


def index(request):
    num = random.randint(1000, 100000)


    some_list = [str(random.randint(10, 100)) + str('000')]
    gold = [str(random.randint(100, 500)) + str('000')]
    platnum = [str(random.randint(500, 1000)) + str('000')]
    context = {
        "bool_item": True,
        "num": num,
        "some_list": some_list,
        "gold": gold,
        "platnum": platnum
    }
    return render(request, 'index.html', context)


@login_required(login_url='/login/')
def withdraw(request, pk=1):
    title = "WITHDRAWAL REQUEST",
    button = "Request"
    if request.user.is_authenticated():
        title = "Dear %s, You can withdraw across wallet platforms " % request.user
        Request = "Request"
    instance = Investment.objects.get(user=request.user.pk)
    form = InvestmentForm(request.POST or None, instance=instance)

    context = {
        "title": title.capitalize(),
        "form": form,
        "button": Request
        }

    if form.is_valid():
        form = form.save(commit=False)

        if form.balance >= form.requested_amount:

            instance.balance = form.balance - form.requested_amount
            instance.pending_withdrawal = instance.pending_withdrawal + form.requested_amount

            instance.save()
            context = {

           "title":"%s, your request will be approuved within 12 hours and money will be sent to your account".capitalize() % request.user,
           "button":"Request sent"


           }
            return render(request, 'withdraw.html', context)
        else:
             context = {

                   "title": "%s, your balance is not enough for the amount you have requested" % request.user,
                   "button":"Request Rejected"



                   }
        return render(request, 'withdraw.html', context)
    return render(request, 'withdraw.html', context)

@login_required(login_url='/login/')
def deposit(request):
    title = 'Welcome to Xampesa',
    button ='Submit'
    if request.user.is_authenticated():
        title = "%s ,you can change your billing information here" % request.user
        Submit = "Submit "
    instance = UserInfo.objects.get(user=request.user.pk)
    form = UserInfoForm(request.POST or None, instance=instance)

    context = {
        "title": title.capitalize(),
        "button": Submit,
        "form": form
    }

    if form.is_valid():
        #user = form.save(commit=False)
        #user.save()
        user_verif = form.save(commit=False)
        if instance.shortcode != user_verif.verification_code:
            messages.error(request, "Wrong voucher")
            return redirect(regform2)
        else:
            user_verif.amount += instance.amount
            user_verif.save()
            context = {
                "title":"congratulation %s your registration was successful enjoy working with us" % request.user

            }
    return render(request, 'regform2.html', context)


def About(request):
    return render(request, 'About.html')

def Plans(request):
    return render(request, 'inverstment-plans.html')


def terms(request):
    return render(request, 'terms.html')


@login_required(login_url='/login/')
def editaccount(request):
    if request.method == "POST":
        form = Editaccount(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('app:account'))
    else:
        form = Editaccount(instance=request.user)
        args = {'form': form}
        return render(request, 'editaccount.html',args)





@login_required(login_url='/login/')
def Editpassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('account')
        else:
            return redirect('/Change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form }
        return render(request, 'Changepassword.html', args)


def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect("/account")
    return render(request, "login.html", {"form" : form, "title": title})


def register(request):
    title = "Register"
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        password = form.cleaned_data.get("password")
        user.set_password(password)
        user.save()
        # subject = 'thenk you for sign up %s' % request.user
        # message = 'we weill be in touch soon'
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [user.email, settings.EMAIL_HOST_USER]
        # send_mail(subject, message , from_email, to_list, fail_silently=True)

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        # confirmation.delay(user)
        return redirect("/regform2")

        #return
    context = {
        "form": form,
        "title": title
        }

    return render(request, 'login.html', context)


@login_required(login_url='/login/')
def logout_view(request):
    django_logout(request)
    return redirect("/")


def authorized(request):
    num = random.randint(1000, 100000)
    time = timezone.now().date()
    blog_date = datetime.date(2017, 10, 15)
    online = [random.randint(10, 200)]
    offline = [random.randint(10, 200)]
    platnum = [str(random.randint(500, 1000)) + str('000')]
    context = {
        "bool_item": True,
        "num": num,
        "online": online,
        "offline": offline,
        "blog_date": blog_date,
        "time": time
    }
    return render(request, 'authorized.html', context)

def Faq(request):
    return render(request, 'Faq.html')


@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'account.html', args)

@login_required(login_url='/login/')
def regform2(request):
    title = 'Welcome to Xampesa'
    if request.user.is_authenticated():
        title = " %s" %request.user
    cout = Investment.objects.get(user=request.user.pk)
    contentz = timer.objects.get(user=request.user.pk)
    instance = UserInfo.objects.get(user=request.user.pk)

    form = UserInfoForm(request.POST or None, instance=instance)

    context = {
        "title": title.title(),
        "form": form
        }
    if form.is_valid():
        #user = form.save(commit=False)
        #user.save()
        user_verif = form.save(commit=False)
        user_verif.save()
        # if instance.shortcode != user_verif.verification_code:
        #     messages.error(request, "Wrong voucher")
        #     return redirect(regform2)
        # else:
        #     instance.total_deposit += instance.amount
        #     contentz.bal += instance.amount
        #     contentz.save()
        #     instance.save()
        #     user_verif.save()
        #     # res = mul.delay(2, 5)
        #     # cout.balance = res.get()
        #     cout.balance = bitcoin_conversion()
        #     cout.save()
        return redirect(reverse('app:account'))

        #     context = {
        #         "title":"congratulation %s your registration was successful enjoy working with us" %request.user
        #
        # }

    return render(request, 'regform2.html', context)

# schedule.every(6).seconds.do(regform2)
# while 1:
#     schedule.run_pending()
#     time.sleep(1)








class ApiView(APIView):
    def get(self, request):
        info = UserInfo.objects.all()
        serializer = AppSerializers(info, many=True)
        return Response(serializer.data)


    def put(self, request):
        serializer = AppSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppApiDetailsView(APIView):
    def get(self, request, pk):
        info = get_object_or_404(UserInfo, pk=pk)
        serializer = AppSerializers(info)
        return Response(serializer.data)

    def delete(self, request, pk):
        info = get_object_or_404(UserInfo, pk=pk)
        info.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)






@login_required(login_url='/login/')
def airtelmoney(request):
    title = 'Welcome to Xampesa'
    button = "Request"
    mtandao = "AirtelMoney"
    if request.user.is_authenticated():
        title = "Welcome %s, you are going to use airtel money depositing to your account" %request.user
        Request = "Deposit"
        mtandao = "AirtelMoney"
    # content = UserInfo.objects.get(user=request.user.pk)

    form = AirtelMoneyForm(request.POST or None)
    context = {
        "title":title,
        "form": form,
        "mtandao": mtandao,
        "button": Request

        }

    if form.is_valid():
        user_deposit = form.save(commit=False)
        user_deposit.save()
        context = {
            "title": "congratulation %s your registration was successful enjoy working with us" % request.user

        }
        return redirect(reverse('app:verification'))

    return render(request, 'deposit.html', context)


# def verify(request, uuid):
#     try:
#         user = UserInfo.objects.get(verification_uuid=uuid, is_verified=False)
#     except User.DoesNotExist:
#         raise Http404("User does not exist or is already verified")
#     user.is_verified = True
#     user.save()
#     return redirect('/')

@login_required(login_url='/login/')
def tigopesa(request):
    title = 'Welcome to Xampesa'
    button = "Request"
    mtandao = "Tigopesa"
    if request.user.is_authenticated():
        title = "Welcome %s, you are going to use tigopesa depositing to your account" %request.user
        Request = "Deposit"
        mtandao = "Tigopesa"
    # content = UserInfo.objects.get(user=request.user.pk)
    form = TigopesaForm(request.POST or None)
    context = {
        "title":title,
        "form": form,
        "mtandao": mtandao,
        "button": Request
        }

    if form.is_valid():
        #user = form.save(commit=False)
        #user.save()
        user_deposit = form.save(commit=False)
        #sec = UserInfo.objects.get(user=request.user.pk)
        # if content.shortcode != user_deposit.verification_code:

        #     messages.error(request, "Wrong voucher")
        #     return redirect(tigopesa)
        # else:
        #     content.amount = content.amount + user_deposit.depositing_amount
        #     content.total_deposit = content.total_deposit + user_deposit.depositing_amount
        #     content.save()
        user_deposit.save()
        context = {
            "title":"congratulation %s your registration was successful enjoy working with us" %request.user

        }
        return redirect(reverse('app:verification'))

    return render(request, 'deposit.html', context)

@login_required(login_url='/login/')
def mpesa(request):
    title = 'Welcome to Xampesa'
    button = "Request"
    mtandao = "Mpesa"
    if request.user.is_authenticated():
        title = "Welcome %s, you are going to use mpesa depositing to your account" %request.user
        Request = "Deposit"
        mtandao = "Mpesa"
    # content = UserInfo.objects.get(user=request.user.pk)
    # instance = UserInfo.objects.get(user=request.user.pk)
    form = MpesaForm(request.POST or None)
    context = {
        "title":title,
        "form": form,
        "button": Request,
        "mtandao": mtandao
        }
    if form.is_valid():
        #user = form.save(commit=False)
        #user.save()
        user_deposit = form.save(commit=False)
        # if content.shortcode != user_deposit.verification_code:
        #     messages.error(request, "Wrong voucher")
        #     return redirect(mpesa)
        # else:
        #     content.amount = content.amount + user_deposit.depositing_amount
        #     content.total_deposit = content.total_deposit + user_deposit.depositing_amount
        #     content.save()
        user_deposit.save()
        # context = {
        #     "title":"congratulation %s your registration was successful enjoy working with us" %request.user
        #
        # }
        return redirect(reverse('app:verification'))

    return render(request, 'deposit.html', context)

@login_required(login_url='/login/')
def bitcoin(request, pk=None):
    title = 'Welcome to Xampesa'
    button = "Deposit"
    if request.user.is_authenticated():
        title = "Welcome %s, you are going to use bitcoin depositing to your account" %request.user
        Deposit = "Deposit"
    instance = UserInfo.objects.get(user=request.user.pk)
    form = BitcoinForm(request.POST or None, instance=instance)
    context = {
        "title":title,
        "form": form,
        "button": Deposit
        }

    if form.is_valid():
        #user = form.save(commit=False)
        #user.save()
        userv = form.save(commit=False)
        # if instance.shortcode != userv.verification_code:
        #     messages.error(request, "Wrong voucher")
        #     return redirect(bitcoin)
        # else:
        #     #print(userv.amount)
        userv.save()
        context = {
            "title":"congratulation %s your registration was successful enjoy working with us" %request.user

        }

        return redirect(reverse('app:verification'))

    return render(request, 'deposit.html', context)

@login_required(login_url='/login/')
def account(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'account.html', args)


@csrf_exempt
@login_required(login_url='/login/')
def account_type(request):
    title = 'Welcome to Xampesa'
    if request.user.is_authenticated():
        title = "Welcome %s , Choose the processor which you are going to use" % request.user
    context = {
        "title": title
    }
    return render(request, "account_type.html", context)


@csrf_exempt
@login_required(login_url='/login/')
def wallet(request, id=None):
    title = 'Welcome to Xampesa'
    if request.user.is_authenticated():
        title = " %s" %request.user
    # cout = Userz.objects.get(user=request.user.pk)
    proc = Processors.objects.get(user=request.user)
    cout = UserInfo.objects.get(user=request.user.pk)
    # watre = cout.full_name
    # instance = Products.objects.get(username=watre).order_by("id")[:0]
    form = TransactionPerfectMoneyForm(request.POST or None, request.FILES or None)
    context = {
        "title": title.title(),
        "form": form
        }
    if form.is_valid():
        user = form.save(commit=False)
        cout.amount = cout.amount + user.PAYMENT_AMOUNT
        user.actualDeposit = user.PAYMENT_AMOUNT
        cout.total_deposit = cout.total_deposit + user.PAYMENT_AMOUNT
        proc.perfectmoney = proc.perfectmoney + user.PAYMENT_AMOUNT
        if user.package == Silver:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.PAYMENT_AMOUNT,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Tarnish:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.PAYMENT_AMOUNT,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Charoite:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.PAYMENT_AMOUNT,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()

                                                  )

        elif user.package == TANZANITE:
            enddate = timezone.now() + timedelta(60)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.PAYMENT_AMOUNT,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Karat:
            enddate = timezone.now() + timedelta(60)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.PAYMENT_AMOUNT,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Corundum:
            enddate = timezone.now() + timedelta(60)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.PAYMENT_AMOUNT,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == TITANIUM:
            enddate = timezone.now() + timedelta(90)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.PAYMENT_AMOUNT,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Niello:
            enddate = timezone.now() + timedelta(90)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.PAYMENT_AMOUNT,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Zircorn:
            enddate = timezone.now() + timedelta(90)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.PAYMENT_AMOUNT,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == DIAMOND:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.PAYMENT_AMOUNT,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Gold:
            enddate = timezone.now() + timedelta(125)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.PAYMENT_AMOUNT,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Platnum:
            enddate = timezone.now() + timedelta(100)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.PAYMENT_AMOUNT,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator(),

                                                  )

        elif user.package == Carbon:
            enddate = timezone.now() + timedelta(100)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.PAYMENT_AMOUNT,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()

                                                  )
        elif user.package == Quartz:
            enddate = timezone.now() + timedelta(100)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.PAYMENT_AMOUNT,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Pearl:
            enddate = timezone.now() + timedelta(125)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.PAYMENT_AMOUNT,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )








            # sav = DepositsVerified.objects.create(user=user.user,
            #                                       username=user.username,
            #                                       processor=user.processor,
            #                                       amount_deposited=user.m_amount,
            #                                       plan=user.Plan, hashid=user.hashid,
            #                                       expected_income=user.expectedIncome,
            #                                       shortcode=user.hashid,
            #                                       startdate=user.opens,
            #                                       enddate=user.closes,
            #                                       sign=user.sign
            #                                       )

        sav.save()
        proc.save()
        cout.save()
        user.save()
        return redirect(reverse('app:account'))
    return render(request, 'wallet-depositing.html', context)

@login_required(login_url='/login/')
def payeertransaction(request, id=None):
    title = 'Welcome to Xampesa'
    # m_shop = '460804530'
    # m_orderid = '1'
    # m_curr = 'USD'
    # description = 'i have Deposited amount'
    # m_desc = binascii.b2a_base64(description.encode('utf-8'))[:-1]
    # m_key = 'OBDegT8uF96A3C6Q'
    # list_of_value_for_sign = map(str, [m_shop, m_orderid, m_curr, m_desc, m_key])
    # result_string = ":".join(list_of_value_for_sign)
    #
    # sign_hash = hashlib.sha256(result_string.encode())
    # sign = sign_hash.hexdigest().upper()
    if request.user.is_authenticated():

        # cout = Userz.objects.get(user=request.user.pk)

        proc = Processors.objects.get(user=request.user)
        cout = UserInfo.objects.get(user=request.user.pk)
        # watre = cout.full_name
        # instance = Products.objects.get(username=watre).order_by("id")[:0]
        form = TransactionPayeerForm(request.POST or None, request.FILES or None)
        user = form.save(commit=False)
        m_shop = '460804530'
        m_orderid = '12345'
        m_amount = user.m_amount
        print(user.m_amount)
        m_curr = 'USD'
        description = 'i have Deposited amount'
        m_desc = base64.b64encode(description.encode('utf8')).decode('utf-8')
        m_key = 'OBDegT8uF96A3C6Q'
        list_of_value_for_sign = map(str, [m_shop, m_orderid, m_amount, m_curr, m_desc, m_key])
        result_string = ":".join(list_of_value_for_sign)
        sign_hash = hashlib.sha256(result_string.encode())
        sign = sign_hash.hexdigest().upper()
        title = " %s" % request.user
        context = {
            "title": title.title(),
            "m_shop": m_shop,
            "m_curr": m_curr,
            "description": description,
            "m_desc": m_desc,
            "sign": sign,
            "form": form,
            "m_orderid": m_orderid

            }

        if form.is_valid():
            user = form.save(commit=False)
            cout.amount = cout.amount + user.m_amount
            user.actualDeposit = user.m_amount
            cout.total_deposit = cout.total_deposit + user.m_amount
            proc.payeer = proc.payeer + user.m_amount




            if user.package == Silver:
                enddate = timezone.now() + timedelta(30)
                sav = DepositsVerified.objects.create(user=user.user,
                                                      username=user.username,
                                                      processor=user.processor,
                                                      amount_deposited=user.m_amount,
                                                      package=user.package,
                                                      startdate=timezone.now(),
                                                      enddate=enddate,
                                                      hashid= code_generator()
                                                      )

            elif user.package == Tarnish:
                enddate = timezone.now() + timedelta(30)
                sav = DepositsVerified.objects.create(user=user.user,
                                                      username=user.username,
                                                      processor=user.processor,
                                                      amount_deposited=user.m_amount,
                                                      package=user.package,
                                                      startdate=timezone.now(),
                                                      enddate=enddate,
                                                      hashid=code_generator()
                                                      )

            elif user.package == Charoite:
                enddate = timezone.now() + timedelta(30)
                sav = DepositsVerified.objects.create(user=user.user,
                                                      username=user.username,
                                                      processor=user.processor,
                                                      amount_deposited=user.m_amount,
                                                      package=user.package,
                                                      startdate=timezone.now(),
                                                      enddate=enddate,
                                                      hashid=code_generator()

                                                      )

            elif user.package == TANZANITE:
                enddate = timezone.now() + timedelta(60)
                sav = DepositsVerified.objects.create(user=user.user,
                                                      username=user.username,
                                                      processor=user.processor,
                                                      amount_deposited=user.m_amount,
                                                      package=user.package,
                                                      startdate=timezone.now(),
                                                      enddate=enddate,
                                                      hashid=code_generator()
                                                      )

            elif user.package == Karat:
                enddate = timezone.now() + timedelta(60)
                sav = DepositsVerified.objects.create(user=user.user,
                                                      username=user.username,
                                                      processor=user.processor,
                                                      amount_deposited=user.m_amount,
                                                      package=user.package,
                                                      startdate=timezone.now(),
                                                      enddate=enddate,
                                                      hashid=code_generator()
                                                      )
            elif user.package == Corundum:
                enddate = timezone.now() + timedelta(60)
                sav = DepositsVerified.objects.create(user=user.user,
                                                      username=user.username,
                                                      processor=user.processor,
                                                      amount_deposited=user.m_amount,
                                                      package=user.package,
                                                      startdate=timezone.now(),
                                                      enddate=enddate,
                                                      hashid=code_generator()
                                                      )

            elif user.package == TITANIUM:
                enddate = timezone.now() + timedelta(90)
                sav = DepositsVerified.objects.create(user=user.user,
                                                      username=user.username,
                                                      processor=user.processor,
                                                      amount_deposited=user.m_amount,
                                                      package=user.package,
                                                      startdate=timezone.now(),
                                                      enddate=enddate,
                                                      hashid=code_generator()
                                                      )
            elif user.package == Niello:
                enddate = timezone.now() + timedelta(90)
                sav = DepositsVerified.objects.create(user=user.user,
                                                      username=user.username,
                                                      processor=user.processor,
                                                      amount_deposited=user.m_amount,
                                                      package=user.package,
                                                      startdate=timezone.now(),
                                                      enddate=enddate,
                                                      hashid=code_generator()
                                                      )

            elif user.package == Zircorn:
                enddate = timezone.now() + timedelta(90)
                sav = DepositsVerified.objects.create(user=user.user,
                                                      username=user.username,
                                                      processor=user.processor,
                                                      amount_deposited=user.m_amount,
                                                      package=user.package,
                                                      startdate=timezone.now(),
                                                      enddate=enddate,
                                                      hashid=code_generator()
                                                      )
            elif user.package == DIAMOND:
                enddate = timezone.now() + timedelta(30)
                sav = DepositsVerified.objects.create(user=user.user,
                                                      username=user.username,
                                                      processor=user.processor,
                                                      amount_deposited=user.m_amount,
                                                      package=user.package,
                                                      startdate=timezone.now(),
                                                      enddate=enddate,
                                                      hashid=code_generator()
                                                      )

            elif user.package == Gold:
                enddate = timezone.now() + timedelta(125)
                sav = DepositsVerified.objects.create(user=user.user,
                                                      username=user.username,
                                                      processor=user.processor,
                                                      amount_deposited=user.m_amount,
                                                      package=user.package,
                                                      startdate=timezone.now(),
                                                      enddate=enddate,
                                                      hashid=code_generator()
                                                      )
            elif user.package == Platnum:
                enddate = timezone.now() + timedelta(100)
                sav = DepositsVerified.objects.create(user=user.user,
                                                      username=user.username,
                                                      processor=user.processor,
                                                      amount_deposited=user.m_amount,
                                                      package=user.package,
                                                      startdate=timezone.now(),
                                                      enddate=enddate,
                                                      hashid=code_generator()
                                                      )

            elif user.package == Carbon:
                enddate = timezone.now() + timedelta(100)
                sav = DepositsVerified.objects.create(user=user.user,
                                                      username=user.username,
                                                      processor=user.processor,
                                                      amount_deposited=user.m_amount,
                                                      package=user.package,
                                                      startdate=timezone.now(),
                                                      enddate=enddate,
                                                      hashid=code_generator()
                                                      )
            elif user.package == Quartz:
                enddate = timezone.now() + timedelta(100)
                sav = DepositsVerified.objects.create(user=user.user,
                                                      username=user.username,
                                                      processor=user.processor,
                                                      amount_deposited=user.m_amount,
                                                      package=user.package,
                                                      startdate=timezone.now(),
                                                      enddate=enddate,
                                                      hashid=code_generator()
                                                      )

            elif user.package == Pearl:
                enddate = timezone.now() + timedelta(125)
                sav = DepositsVerified.objects.create(user=user.user,
                                                      username=user.username,
                                                      processor=user.processor,
                                                      amount_deposited=user.m_amount,
                                                      package=user.package,
                                                      startdate=timezone.now(),
                                                      enddate= enddate,
                                                      hashid=code_generator()
                                                      )








        # sav = DepositsVerified.objects.create(user=user.user,
        #                                       username=user.username,
        #                                       processor=user.processor,
        #                                       amount_deposited=user.m_amount,
        #                                       plan=user.Plan, hashid=user.hashid,
        #                                       expected_income=user.expectedIncome,
        #                                       shortcode=user.hashid,
        #                                       startdate=user.opens,
        #                                       enddate=user.closes,
        #                                       sign=user.sign
        #                                       )
            user.save()
            proc.save()
            sav.save()
            cout.save()
            return redirect(reverse('app:account'))
    return render(request, 'payeer-deposit.html', context)




@login_required(login_url='/login/')
def BitcoinTransactions(request, id=None):
    title = 'Welcome to Xampesa'
    if request.user.is_authenticated():
        title = " %s" %request.user
    # cout = Userz.objects.get(user=request.user.pk)
    proc = Processors.objects.get(user=request.user)
    cout = UserInfo.objects.get(user=request.user.pk)
    # watre = cout.full_name
    # instance = Products.objects.get(username=watre).order_by("id")[:0]
    form = TransactionBitcoinForm(request.POST or None, request.FILES or None)
    context = {
        "title": title.title(),
        "form": form
        }
    if form.is_valid():
        user = form.save(commit=False)

        cout.bitcoin_amount = cout.bitcoin_amount + user.b_amount
        user.actualDeposit = user.b_amount
        cout.total_bitcoin_deposit = cout.total_bitcoin_deposit + user.b_amount
        proc.bitcoin = proc.bitcoin + user.b_amount
        if user.package == Silver:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid= code_generator()
                                                  )

        elif user.package == Tarnish:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Charoite:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()

                                                  )

        elif user.package == TANZANITE:
            enddate = timezone.now() + timedelta(60)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Karat:
            enddate = timezone.now() + timedelta(60)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Corundum:
            enddate = timezone.now() + timedelta(60)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == TITANIUM:
            enddate = timezone.now() + timedelta(90)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Niello:
            enddate = timezone.now() + timedelta(90)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Zircorn:
            enddate = timezone.now() + timedelta(90)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == DIAMOND:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Gold:
            enddate = timezone.now() + timedelta(125)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Platnum:
            enddate = timezone.now() + timedelta(100)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Carbon:
            enddate = timezone.now() + timedelta(100)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Quartz:
            enddate = timezone.now() + timedelta(100)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Pearl:
            enddate = timezone.now() + timedelta(125)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate= enddate,
                                                  hashid=code_generator()
                                                  )








    # sav = DepositsVerified.objects.create(user=user.user,
    #                                       username=user.username,
    #                                       processor=user.processor,
    #                                       amount_deposited=user.m_amount,
    #                                       plan=user.Plan, hashid=user.hashid,
    #                                       expected_income=user.expectedIncome,
    #                                       shortcode=user.hashid,
    #                                       startdate=user.opens,
    #                                       enddate=user.closes,
    #                                       sign=user.sign
    #                                       )
        user.save()
        proc.save()
        sav.save()
        cout.save()
        return redirect(reverse('app:account'))
    return render(request, 'bitcoindeposit.html', context)


@login_required(login_url='/login/')
def BitcoinRedepositView(request, id=None):
    title = 'Welcome to Xampesa'
    if request.user.is_authenticated():
        title = " %s" %request.user
    # cout = Userz.objects.get(user=request.user.pk)
    proc = Processors.objects.get(user=request.user)
    cout = UserInfo.objects.get(user=request.user.pk)
    inves = Investment.objects.get(user=request.user)
    # watre = cout.full_name
    # instance = Products.objects.get(username=watre).order_by("id")[:0]
    form = BitcoinRedepositForm(request.POST or None, request.FILES or None)
    context = {
        "title": title.title(),
        "form": form
        }
    if form.is_valid():
        user = form.save(commit=False)

        cout.bitcoin_amount = cout.bitcoin_amount + user.b_amount

        print("here i am")
        user.actualDeposit = user.b_amount
        cout.total_deposit = cout.total_deposit + user.b_amount
        inves.Bitcoin_balance = inves.Bitcoin_balance - user.b_amount
        proc.bitcoin = proc.bitcoin + user.b_amount
        if user.package == Silver:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid= code_generator()
                                                  )

        elif user.package == Tarnish:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Charoite:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()

                                                  )

        elif user.package == TANZANITE:
            enddate = timezone.now() + timedelta(60)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Karat:
            enddate = timezone.now() + timedelta(60)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Corundum:
            enddate = timezone.now() + timedelta(60)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == TITANIUM:
            enddate = timezone.now() + timedelta(90)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Niello:
            enddate = timezone.now() + timedelta(90)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Zircorn:
            enddate = timezone.now() + timedelta(90)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == DIAMOND:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Gold:
            enddate = timezone.now() + timedelta(125)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Platnum:
            enddate = timezone.now() + timedelta(100)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Carbon:
            enddate = timezone.now() + timedelta(100)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Quartz:
            enddate = timezone.now() + timedelta(100)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Pearl:
            enddate = timezone.now() + timedelta(125)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.b_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate= enddate,
                                                  hashid=code_generator()
                                                  )








    # sav = DepositsVerified.objects.create(user=user.user,
    #                                       username=user.username,
    #                                       processor=user.processor,
    #                                       amount_deposited=user.m_amount,
    #                                       plan=user.Plan, hashid=user.hashid,
    #                                       expected_income=user.expectedIncome,
    #                                       shortcode=user.hashid,
    #                                       startdate=user.opens,
    #                                       enddate=user.closes,
    #                                       sign=user.sign

        inves.save()
        user.save()
        proc.save()
        sav.save()
        cout.save()
        return redirect(reverse('app:account'))
    return render(request, 'bitcoinredeposit.html', context)



@login_required(login_url='/login/')
def OkPaydepositView(request, id=None):
    title = 'Welcome to Xampesa'
    if request.user.is_authenticated():
        title = " %s" %request.user
    # cout = Userz.objects.get(user=request.user.pk)
    proc = Processors.objects.get(user=request.user)
    cout = UserInfo.objects.get(user=request.user.pk)
    # watre = cout.full_name
    # instance = Products.objects.get(username=watre).order_by("id")[:0]
    form = OKpayDeoisitForm(request.POST or None, request.FILES or None)
    context = {
        "title": title.title(),
        "form": form
        }
    if form.is_valid():
        user = form.save(commit=False)

        cout.amount = cout.amount + user.o_amount
        print("here i am")
        user.actualDeposit = user.o_amount
        cout.total_deposit = cout.total_deposit + user.o_amount
        proc.okpay = proc.okpay + user.o_amount
        if user.package == Silver:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid= code_generator()
                                                  )

        elif user.package == Tarnish:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Charoite:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()

                                                  )

        elif user.package == TANZANITE:
            enddate = timezone.now() + timedelta(60)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Karat:
            enddate = timezone.now() + timedelta(60)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Corundum:
            enddate = timezone.now() + timedelta(60)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == TITANIUM:
            enddate = timezone.now() + timedelta(90)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Niello:
            enddate = timezone.now() + timedelta(90)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Zircorn:
            enddate = timezone.now() + timedelta(90)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == DIAMOND:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Gold:
            enddate = timezone.now() + timedelta(125)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Platnum:
            enddate = timezone.now() + timedelta(100)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Carbon:
            enddate = timezone.now() + timedelta(100)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Quartz:
            enddate = timezone.now() + timedelta(100)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Pearl:
            enddate = timezone.now() + timedelta(125)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate= enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Copper:
            enddate = timezone.now() + timedelta(5)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Lapls:
            enddate = timezone.now() + timedelta(5)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Emerald:
            enddate = timezone.now() + timedelta(5)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Iron:
            enddate = timezone.now() + timedelta(7)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Glass:
            enddate = timezone.now() + timedelta(7)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Moisanite:
            enddate = timezone.now() + timedelta(7)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Calcite:
            enddate = timezone.now() + timedelta(15)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Sapphire:
            enddate = timezone.now() + timedelta(15)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )


        elif user.package == Ruby:
            enddate = timezone.now() + timedelta(15)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Amber:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Agate:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Amazonnile:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Beads:
            enddate = timezone.now() + timedelta(50)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Beryl:
            enddate = timezone.now() + timedelta(50)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Azuriite:
            enddate = timezone.now() + timedelta(50)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.o_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )








    # sav = DepositsVerified.objects.create(user=user.user,
    #                                       username=user.username,
    #                                       processor=user.processor,
    #                                       amount_deposited=user.m_amount,
    #                                       plan=user.Plan, hashid=user.hashid,
    #                                       expected_income=user.expectedIncome,
    #                                       shortcode=user.hashid,
    #                                       startdate=user.opens,
    #                                       enddate=user.closes,
    #                                       sign=user.sign
    #                                       )
        user.save()
        proc.save()
        sav.save()
        cout.save()
        return redirect(reverse('app:account'))
    return render(request, 'okpaydepositinvest.html', context)

@login_required(login_url='/login/')
def AdvCashDepositView(request, id=None):
    title = 'Welcome to Xampesa'
    if request.user.is_authenticated():
        title = " %s" %request.user
    # cout = Userz.objects.get(user=request.user.pk)
    proc = Processors.objects.get(user=request.user)
    cout = UserInfo.objects.get(user=request.user.pk)
    # watre = cout.full_name
    # instance = Products.objects.get(username=watre).order_by("id")[:0]
    form = AdvCashDepositForm(request.POST or None, request.FILES or None)
    context = {
        "title": title.title(),
        "form": form
        }
    if form.is_valid():
        user = form.save(commit=False)

        cout.amount = cout.amount + user.a_amount
        print("here i am")
        user.actualDeposit = user.a_amount
        cout.total_deposit = cout.total_deposit + user.a_amount
        proc.adcash = proc.adcash + user.a_amount
        if user.package == Silver:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid= code_generator()
                                                  )

        elif user.package == Tarnish:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Charoite:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()

                                                  )

        elif user.package == TANZANITE:
            enddate = timezone.now() + timedelta(60)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Karat:
            enddate = timezone.now() + timedelta(60)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Corundum:
            enddate = timezone.now() + timedelta(60)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == TITANIUM:
            enddate = timezone.now() + timedelta(90)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Niello:
            enddate = timezone.now() + timedelta(90)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Zircorn:
            enddate = timezone.now() + timedelta(90)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == DIAMOND:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Gold:
            enddate = timezone.now() + timedelta(125)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Platnum:
            enddate = timezone.now() + timedelta(100)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Carbon:
            enddate = timezone.now() + timedelta(100)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Quartz:
            enddate = timezone.now() + timedelta(100)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Pearl:
            enddate = timezone.now() + timedelta(125)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate= enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Copper:
            enddate = timezone.now() + timedelta(5)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Lapls:
            enddate = timezone.now() + timedelta(5)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Emerald:
            enddate = timezone.now() + timedelta(5)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Iron:
            enddate = timezone.now() + timedelta(7)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Glass:
            enddate = timezone.now() + timedelta(7)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Moisanite:
            enddate = timezone.now() + timedelta(7)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Calcite:
            enddate = timezone.now() + timedelta(15)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Sapphire:
            enddate = timezone.now() + timedelta(15)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )


        elif user.package == Ruby:
            enddate = timezone.now() + timedelta(15)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Amber:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Agate:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Amazonnile:
            enddate = timezone.now() + timedelta(30)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Beads:
            enddate = timezone.now() + timedelta(50)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )
        elif user.package == Beryl:
            enddate = timezone.now() + timedelta(50)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )

        elif user.package == Azuriite:
            enddate = timezone.now() + timedelta(50)
            sav = DepositsVerified.objects.create(user=user.user,
                                                  username=user.username,
                                                  processor=user.processor,
                                                  amount_deposited=user.a_amount,
                                                  package=user.package,
                                                  startdate=timezone.now(),
                                                  enddate=enddate,
                                                  hashid=code_generator()
                                                  )








    # sav = DepositsVerified.objects.create(user=user.user,
    #                                       username=user.username,
    #                                       processor=user.processor,
    #                                       amount_deposited=user.m_amount,
    #                                       plan=user.Plan, hashid=user.hashid,
    #                                       expected_income=user.expectedIncome,
    #                                       shortcode=user.hashid,
    #                                       startdate=user.opens,
    #                                       enddate=user.closes,
    #                                       sign=user.sign
    #                                       )

        user.save()
        proc.save()
        sav.save()
        cout.save()
        return redirect(reverse('app:account'))
    return render(request, 'advcashdepositinvest.html', context)












def payeerWithdraw(request, id=None):
    if request.user.is_authenticated():
        title = " %s" %request.user
    # cout = Userz.objects.get(user=request.user.pk)
    cout = UserInfo.objects.get(user=request.user.pk)
    proc = Processors.objects.get(user=request.user)
    stat = Statistics.objects.get(user='xampesa')
    invest = Investment.objects.get(user=request.user)
    # watre = cout.full_name
    # instance = Products.objects.get(username=watre).order_by("id")[:0]
    form = WithdrawprocessorForm(request.POST or None, request.FILES or None)
    context = {
        "title": title.title(),
        "form": form
        }
    if form.is_valid():

        user = form.save(commit=False)
        man = user.m_amount * 10 / 100
        whoa = user.m_amount + man
        if whoa > proc.payeer:
            if whoa < proc.perfectmoney:
                print("the first")
                if invest.balance > 2:
                    print("the fsecond if")
                    invest.balance = invest.balance - whoa
                    if proc.payeer > whoa:
                        print("choose payeer")
                        proc.payeer = proc.payeer - whoa
                        stat.profit = stat.profit + man
                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        proc.payeer = proc.payeer * 0
                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name,
                                                                 balance=user.balance, processor=user.processor,
                                                                 processor_account_number=user.processor_acc_number,
                                                                 m_amount=user.m_amount, Status=user.status)

                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        invest.save()
                        proc.save()
                        user.save()
                        return redirect(reverse('app:account'))
                    else:
                        print("choose perfectt")
                        proc.perfectmoney = proc.perfectmoney - whoa
                        stat.profit = stat.profit + man
                        print("conclude")
                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name,
                                                                 balance=user.balance, processor=user.processor,
                                                                 processor_account_number=user.processor_acc_number,
                                                                 m_amount=user.m_amount, Status=user.status)

                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        invest.save()
                        stat.save()
                        proc.save()
                        user.save()
                        return redirect(reverse('app:account'))

            elif whoa < proc.okpay:
                print("the first")
                if invest.balance > 2:
                    print("the fsecond if")
                    invest.balance = invest.balance - whoa
                    if proc.payeer > whoa:
                        print("choose payeer")
                        proc.payeer = proc.payeer - whoa
                        stat.profit = stat.profit + man
                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name,
                                                                 balance=user.balance, processor=user.processor,
                                                                 processor_account_number=user.processor_acc_number,
                                                                 m_amount=user.m_amount, Status=user.status)

                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        stat.save()
                        invest.save()
                        proc.save()
                        user.save()
                        return redirect(reverse('app:account'))

                    elif proc.okpay > whoa:
                        print("choose perfectt")
                        proc.okpay = proc.okpay - whoa
                        stat.profit = stat.profit + man
                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name,
                                                                 balance=user.balance, processor=user.processor,
                                                                 processor_account_number=user.processor_acc_number,
                                                                 m_amount=user.m_amount, Status=user.status)

                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        invest.save()
                        proc.save()
                        stat.save()
                        user.save()
                        return redirect(reverse('app:account'))

            elif whoa < proc.adcash:
                print("the first")
                if invest.balance > 2:
                    print("the fsecond if")
                    invest.balance = invest.balance - whoa
                    if proc.payeer > whoa:
                        print("choose payeer")
                        proc.payeer = proc.payeer - whoa
                        stat.profit =stat.profit + man
                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name,
                                                                 balance=user.balance, processor=user.processor,
                                                                 processor_account_number=user.processor_acc_number,
                                                                 m_amount=user.m_amount, Status=user.status)

                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        invest.save()
                        stat.save()
                        proc.save()
                        user.save()
                        return redirect(reverse('app:account'))
                    else:
                        print("choose perfectt")
                        proc.adcash = proc.adcash - whoa
                        stat.profit = stat.profit + man

                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name,
                                                                 balance=user.balance, processor=user.processor,
                                                                 processor_account_number=user.processor_acc_number,
                                                                 m_amount=user.m_amount, Status=user.status)

                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        invest.save()
                        proc.save()
                        stat.save()
                        user.save()
                        return redirect(reverse('app:account'))
        else:
            if invest.balance > 1:
                invest.balance = invest.balance - user.m_amount
                invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                proc.payeer = proc.payeer - user.m_amount
                proc.save()
                ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name,
                                                         balance=user.balance, processor=user.processor,
                                                         processor_account_number=user.processor_acc_number,
                                                         m_amount=user.m_amount, Status=user.status)
                print('the second')
                ver.save()
                invest.save()
                user.save()
                from django.conf import settings
                from django.core.mail import send_mail
                subject = 'Withdraw confirmed'
                message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                from_email = settings.EMAIL_HOST_USER
                to_list = [user.email]
                send_mail(subject, message, from_email, to_list, fail_silently=True)
                return redirect(reverse('app:account'))
    return render(request, 'payeerwithdraw.html', context)



def perFectmoneyWithdraw(request, id=None):
    if request.user.is_authenticated():
        title = " %s" %request.user
    # cout = Userz.objects.get(user=request.user.pk)
    # cout = UserInfo.objects.get(user=request.user.pk)
    # watre = cout.full_name
    # instance = Products.objects.get(username=watre).order_by("id")[:0]
    invest = Investment.objects.get(user=request.user)
    proc = Processors.objects.get(user=request.user)
    stat = Statistics.objects.get(user='xampesa')
    form = WithdrawprocessorForm(request.POST or None, request.FILES or None)
    context = {
        "title": title.title(),
        "form": form
        }
    if form.is_valid():
        user = form.save(commit=False)
        man = user.m_amount * 10 / 100
        whoa = user.m_amount + man
        if user.m_amount > proc.perfectmoney:
            if whoa < proc.payeer:
                print('The first')
                if invest.balance > 2:
                    invest.balance =invest.balance - whoa
                    if proc.perfectmoney > whoa:
                        proc.perfectmoney = proc.perfectmoney - whoa
                        stat.profit =stat.profit + man
                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        # invest.balance = invest.balance - user.m_amount


                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name,
                                                                 balance=user.balance, processor=user.processor,
                                                                 processor_account_number=user.processor_acc_number,
                                                                 m_amount=user.m_amount, Status=user.status)
                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        proc.save()
                        invest.save()
                        user.save()
                        return redirect(reverse('app:account'))
                    elif proc.payeer > whoa:
                        proc.payeer = proc.payeer - whoa
                        stat.profit = stat.profit + man
                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        # invest.balance = invest.balance - user.m_amount


                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name,
                                                                 balance=user.balance, processor=user.processor,
                                                                 processor_account_number=user.processor_acc_number,
                                                                 m_amount=user.m_amount, Status=user.status)
                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        proc.save()
                        invest.save()
                        user.save()
                        return redirect(reverse('app:account'))



            elif whoa < proc.okpay:
                print('The first')
                if invest.balance > 2:
                    invest.balance =invest.balance - whoa
                    if proc.perfectmoney > whoa:
                        proc.perfectmoney = proc.perfectmoney - whoa
                        stat.profit = stat.profit + man
                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        # invest.balance = invest.balance - user.m_amount


                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name,
                                                                 balance=user.balance, processor=user.processor,
                                                                 processor_account_number=user.processor_acc_number,
                                                                 m_amount=user.m_amount, Status=user.status)
                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        proc.save()
                        invest.save()
                        user.save()
                        return redirect(reverse('app:account'))
                    else:
                        proc.okpay = proc.okpay - whoa
                        proc.okpay = proc.okpay - whoa
                        stat.profit = stat.profit + man


                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        # invest.balance = invest.balance - user.m_amount


                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name, balance=user.balance, processor=user.processor, processor_account_number=user.processor_acc_number, m_amount=user.m_amount, Status=user.status )
                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        proc.save()
                        invest.save()
                        user.save()
                        return redirect(reverse('app:account'))


            elif whoa < proc.adcash:
                print('The first')
                if invest.balance > 2:
                    invest.balance = invest.balance - whoa
                    if proc.perfectmoney > whoa:
                        proc.perfectmoney = proc.perfectmoney - whoa
                        stat.profit = stat.profit + man
                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        # invest.balance = invest.balance - user.m_amount


                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name,
                                                                 balance=user.balance, processor=user.processor,
                                                                 processor_account_number=user.processor_acc_number,
                                                                 m_amount=user.m_amount, Status=user.status)
                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        proc.save()
                        invest.save()
                        user.save()
                        return redirect(reverse('app:account'))
                    else:
                        proc.adcash = proc.adcash - whoa
                        proc.adcash = proc.adcash - whoa
                        stat.profit = stat.profit + man

                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        # invest.balance = invest.balance - user.m_amount


                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name,
                                                                 balance=user.balance, processor=user.processor,
                                                                 processor_account_number=user.processor_acc_number,
                                                                 m_amount=user.m_amount, Status=user.status)
                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        proc.save()
                        invest.save()
                        user.save()
                        return redirect(reverse('app:account'))



        else:
            if invest.balance > 2:
                print('Second')
                invest.balance = invest.balance - user.m_amount
                invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                proc.perfectmoney = proc.perfectmoney - user.m_amount
                ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name, balance=user.balance,
                                                         processor=user.processor,
                                                         processor_account_number=user.processor_acc_number,
                                                         m_amount=user.m_amount, Status=user.status)
                from django.conf import settings
                from django.core.mail import send_mail
                subject = 'Withdraw confirmed'
                message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                from_email = settings.EMAIL_HOST_USER
                to_list = [user.email]
                send_mail(subject, message, from_email, to_list, fail_silently=True)
                ver.save()
                proc.save()
                invest.save()
                user.save()
                return redirect(reverse('app:account'))

    return render(request, 'perfectmoneywithdraw.html', context)


def okpaywithdrawview(request, id=None):
    if request.user.is_authenticated():
        title = " %s" %request.user
    # cout = Userz.objects.get(user=request.user.pk)
    # cout = UserInfo.objects.get(user=request.user.pk)
    # watre = cout.full_name
    # instance = Products.objects.get(username=watre).order_by("id")[:0]
    invest = Investment.objects.get(user=request.user)
    stat = Statistics.objects.get(user='xampesa')
    proc = Processors.objects.get(user=request.user)
    form = WithdrawprocessorForm(request.POST or None, request.FILES or None)
    context = {
        "title": title.title(),
        "form": form
        }
    if form.is_valid():
        user = form.save(commit=False)
        man = user.m_amount * 10/100
        whoa = user.m_amount + man
        if whoa > proc.okpay:
            if whoa < proc.payeer:
                print('The first')
                if invest.balance > 2:
                    invest.balance =invest.balance - whoa

                    if proc.okpay > whoa:
                        proc.okpay = proc.okpay - whoa
                        stat.profit = stat.profit + man
                    elif proc.perfectmoney > whoa:
                        proc.perfectmoney = proc.perfectmoney - whoa
                        stat.profit = stat.profit + man

                    if invest.balance > whoa:
                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        # invest.balance = invest.balance - user.m_amount


                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name, balance=user.balance, processor=user.processor, processor_account_number=user.processor_acc_number, m_amount=user.m_amount, Status=user.status )
                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        proc.save()
                        invest.save()
                        user.save()
                        return redirect(reverse('app:account'))

            elif whoa < proc.perfectmoney:
                print('The first.1')
                if invest.balance > 2:
                    invest.balance =invest.balance - whoa


                    if proc.perfectmoney > whoa:
                        proc.perfectmoney = proc.perfectmoney - whoa
                        stat.profit =stat.profit + man


                    elif proc.okpay > whoa:
                        proc.okpay = proc.okpay - whoa
                        stat.profit = stat.profit + man


                    if invest.balance > user.m_amount:
                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        # invest.balance = invest.balance - user.m_amount


                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name, balance=user.balance, processor=user.processor, processor_account_number=user.processor_acc_number, m_amount=user.m_amount, Status=user.status )
                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        proc.save()
                        stat.save()
                        invest.save()
                        user.save()
                        return redirect(reverse('app:account'))



            elif whoa < proc.adcash:
                print('The first.2')
                if invest.balance > 2:
                    invest.balance =invest.balance - whoa

                    if proc.okpay > whoa:
                        proc.okpay = proc.okpay - whoa
                        stat.profit = stat.profit + man
                    elif proc.adcash > whoa:
                        proc.adcash = proc.adcash - whoa
                        stat.profit = stat.profit + man


                        if invest.balance > user.m_amount:
                            invest.balance = invest.balance - whoa
                            invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                            invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                            # invest.balance = invest.balance - user.m_amount


                            ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name, balance=user.balance, processor=user.processor, processor_account_number=user.processor_acc_number, m_amount=user.m_amount, Status=user.status )
                            from django.conf import settings
                            from django.core.mail import send_mail
                            subject = 'Withdraw confirmed'
                            message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                            from_email = settings.EMAIL_HOST_USER
                            to_list = [user.email]
                            send_mail(subject, message, from_email, to_list, fail_silently=True)
                            ver.save()
                            proc.save()
                            stat.save()
                            invest.save()
                            user.save()
                            return redirect(reverse('app:account'))



        else:
            if invest.balance > 2:
                print('Second')
                invest.balance = invest.balance - user.m_amount
                invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                proc.okpay = proc.okpay - user.m_amount
                ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name, balance=user.balance,
                                                         processor=user.processor,
                                                         processor_account_number=user.processor_acc_number,
                                                         m_amount=user.m_amount, Status=user.status)
                from django.conf import settings
                from django.core.mail import send_mail
                subject = 'Withdraw confirmed'
                message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                from_email = settings.EMAIL_HOST_USER
                to_list = [user.email]
                send_mail(subject, message, from_email, to_list, fail_silently=True)
                ver.save()
                proc.save()
                invest.save()
                user.save()
                return redirect(reverse('app:account'))

    return render(request, 'okpaywithdraw.html', context)



def Advcashwithdraw(request, id=None):
    if request.user.is_authenticated():
        title = " %s" %request.user
    # cout = Userz.objects.get(user=request.user.pk)
    # cout = UserInfo.objects.get(user=request.user.pk)
    # watre = cout.full_name
    # instance = Products.objects.get(username=watre).order_by("id")[:0]
    invest = Investment.objects.get(user=request.user)
    proc = Processors.objects.get(user=request.user)
    stat = Statistics.objects.get(user= 'xampesa')
    form = WithdrawprocessorForm(request.POST or None, request.FILES or None)
    context = {
        "title": title.title(),
        "form": form
        }
    if form.is_valid():
        user = form.save(commit=False)
        man = user.m_amount * 10/100
        whoa = user.m_amount + man
        if whoa > proc.adcash:
            if whoa < proc.payeer:
                print('The first')
                if invest.balance > 2:
                    invest.balance =invest.balance - whoa
                    if proc.adcash > whoa:
                        proc.adcash = proc.adcash - whoa
                        stat.profit = stat.profit + man
                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        proc.adcash = proc.adcash * 0
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        # invest.balance = invest.balance - user.m_amount


                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name,
                                                                 balance=user.balance, processor=user.processor,
                                                                 processor_account_number=user.processor_acc_number,
                                                                 m_amount=user.m_amount, Status=user.status)
                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        proc.save()
                        stat.save()
                        invest.save()
                        user.save()
                        return redirect(reverse('app:account'))
                    else:
                        proc.payeer = proc.payeer - whoa
                        stat.profit = stat.profit + man



                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        proc.adcash = proc.adcash * 0
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        # invest.balance = invest.balance - user.m_amount


                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name, balance=user.balance, processor=user.processor, processor_account_number=user.processor_acc_number, m_amount=user.m_amount, Status=user.status )
                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        proc.save()
                        stat.save()
                        invest.save()
                        user.save()
                        return redirect(reverse('app:account'))

            elif whoa < proc.okpay:
                print('The first')
                if invest.balance > 2:
                    invest.balance =invest.balance - whoa
                    if proc.adcash > whoa:
                        proc.adcash = proc.adcash - whoa
                        stat.profit = stat.profit + man
                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        proc.adcash = proc.adcash * 0
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        # invest.balance = invest.balance - user.m_amount


                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name,
                                                                 balance=user.balance, processor=user.processor,
                                                                 processor_account_number=user.processor_acc_number,
                                                                 m_amount=user.m_amount, Status=user.status)
                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        proc.save()
                        stat.save()
                        invest.save()
                        user.save()
                        return redirect(reverse('app:account'))

                    elif proc.okpay > whoa:
                        proc.okpay = proc.okpay - whoa
                        stat.profit = stat.profit + man


                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        proc.adcash = proc.adcash * 0
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        # invest.balance = invest.balance - user.m_amount


                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name, balance=user.balance, processor=user.processor, processor_account_number=user.processor_acc_number, m_amount=user.m_amount, Status=user.status )
                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        proc.save()
                        invest.save()
                        stat.save()
                        user.save()
                        return redirect(reverse('app:account'))

            elif whoa < proc.perfectmoney:
                print('The first')
                if invest.balance > 2:
                    invest.balance =invest.balance - whoa
                    if proc.adcash > whoa:
                        proc.adcash = proc.adcash - whoa
                        stat.profit = stat.profit + man
                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        proc.adcash = proc.adcash * 0
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        # invest.balance = invest.balance - user.m_amount
                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name,
                                                                 balance=user.balance, processor=user.processor,
                                                                 processor_account_number=user.processor_acc_number,
                                                                 m_amount=user.m_amount, Status=user.status)
                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        proc.save()
                        stat.save()
                        invest.save()
                        user.save()
                        return redirect(reverse('app:account'))
                    elif proc.perfectmoney > whoa:
                        proc.perfectmoney = proc.perfectmoney - whoa
                        stat.profit = stat.profit + man
                        invest.balance = invest.balance - whoa
                        invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                        proc.adcash = proc.adcash * 0
                        invest.last_withdrawal = (invest.last_withdrawal * 0) + user.m_amount
                        # invest.balance = invest.balance - user.m_amount
                        ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name, balance=user.balance, processor=user.processor, processor_account_number=user.processor_acc_number, m_amount=user.m_amount, Status=user.status )
                        from django.conf import settings
                        from django.core.mail import send_mail
                        subject = 'Withdraw confirmed'
                        message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                        from_email = settings.EMAIL_HOST_USER
                        to_list = [user.email]
                        send_mail(subject, message, from_email, to_list, fail_silently=True)
                        ver.save()
                        proc.save()
                        stat.save()
                        invest.save()
                        user.save()
                        return redirect(reverse('app:account'))



        else:
            if invest.balance > 2:
                print('Second')
                invest.balance = invest.balance - user.m_amount
                invest.pending_withdrawal = invest.pending_withdrawal + user.m_amount
                proc.adcash = proc.adcash - user.m_amount
                ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name, balance=user.balance,
                                                         processor=user.processor,
                                                         processor_account_number=user.processor_acc_number,
                                                         m_amount=user.m_amount, Status=user.status)
                from django.conf import settings
                from django.core.mail import send_mail
                subject = 'Withdraw confirmed'
                message = 'we will be depositing your cash ( %s usd) within 24 hours' % user.m_amount
                from_email = settings.EMAIL_HOST_USER
                to_list = [user.email]
                send_mail(subject, message, from_email, to_list, fail_silently=True)
                ver.save()
                proc.save()
                invest.save()
                user.save()
                return redirect(reverse('app:account'))

    return render(request, 'adcashwithdraw.html', context)

class BitcoinWithdrawModelViews(generic.CreateView):
    model = BitcoinWithdrawModel
    form_class = BitcoinWithdrawForm
    template_name = 'bitcoinwithdrawpro.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        getBitcoin_balance = Investment.objects.get(user=self.request.user)
        getprocessorbtc = Processors.objects.get(user=self.request.user)
        if getBitcoin_balance.Bitcoin_balance > 0.0002:
            getBitcoin_balance.Bitcoin_balance = getBitcoin_balance.Bitcoin_balance - user.b_amount
            getprocessorbtc.bitcoin = getprocessorbtc.bitcoin - user.b_amount
            ver = VerifiedWithdrawals.objects.create(user=user.user, full_name=user.full_name, balance=user.balance,
                                                     processor=user.processor,
                                                     processor_account_number=user.processor_acc_number,
                                                     m_amount=user.b_amount, Status=user.status)
            getBitcoin_balance.save()
            ver.save()
            user.save()
            getprocessorbtc.save()
            return redirect(reverse('app:account'))
        return redirect(reverse('app:BitcoinWithdraw'))




@login_required(login_url='/login/')
def BalanceTransactionview(request, id=None):
    title = 'Welcome to Xampesa'
    if request.user.is_authenticated():
        title = " %s" %request.user
    walt = Investment.objects.get(user=request.user.pk)
    Prc = Processors.objects.get(user=request.user)
    form = BalanceTransactionForm(request.POST or None, request.FILES or None)
    context = {
        "title": title.title(),
        "form": form
        }
    if form.is_valid():
        userm = form.save(commit=False)
        if userm.currency_transfered == Usd:

            d = userm.username_receiver

            m = userm.amount_transfered
            Pub = Investment.objects.filter(account_no=d)
            inst = UserInfo.objects.get(user=request.user.pk)
            if Pub.exists():
                kim = Investment.objects.get(account_no=d)
                n = kim.user
                whoa = userm.amount_transfered * 0.01
                mor = whoa + userm.amount_transfered
                if walt.balance >= mor:
                    if Prc.payeer >= mor:
                        if userm.security_code == inst.security_code:
                            for a in Pub:
                                a.balance = userm.amount_transfered + a.balance
                                walt.balance = walt.balance - userm.amount_transfered
                                stat = Statistics.objects.get(user="xampesa")
                                Prc.payeer = Prc.payeer - mor
                                stat.bitcoin_profit = stat.bitcoin_profit + whoa
                                walt.save()
                                stat.save()
                                a.save()
                                Prc.save()
                                userm.save()
                                messages.success(request, '%s USD, Has been successful transferred to  %s ' % (m, n))
                                return redirect(reverse('app:account'))
                        else:
                            messages.success(request, 'Security code entered is not correct ')
                            return redirect(reverse('app:Balance'))


                    elif Prc.perfectmoney >= mor:
                        if userm.security_code == inst.security_code:
                            for a in Pub:
                                a.balance = userm.amount_transfered + a.balance
                                walt.balance = walt.balance - userm.amount_transfered
                                stat = Statistics.objects.get(user="xampesa")
                                Prc.perfectmoney = Prc.perfectmoney - mor
                                stat.bitcoin_profit = stat.bitcoin_profit + whoa
                                walt.save()
                                stat.save()
                                a.save()
                                Prc.save()
                                userm.save()
                                messages.success(request, '%s USD, Has been successful transferred to  %s ' % (m, n))
                                return redirect(reverse('app:account'))
                        else:
                            messages.success(request, 'Security code entered is not correct ')
                            return redirect(reverse('app:Balance'))

                    elif Prc.okpay >= mor:
                        if userm.security_code == inst.security_code:
                            for a in Pub:
                                a.balance = userm.amount_transfered + a.balance
                                walt.balance = walt.balance - userm.amount_transfered
                                stat = Statistics.objects.get(user="xampesa")
                                Prc.okpay = Prc.okpay - mor
                                stat.bitcoin_profit = stat.bitcoin_profit + whoa
                                walt.save()
                                stat.save()
                                a.save()
                                Prc.save()
                                userm.save()
                                messages.success(request, '%s USD, Has been successful transferred to  %s ' % (m, n))
                                return redirect(reverse('app:account'))
                        else:
                            messages.success(request, 'Security code entered is not correct ')
                            return redirect(reverse('app:Balance'))

                    elif Prc.adcash >= mor:
                        if userm.security_code == inst.security_code:
                            for a in Pub:
                                a.balance = userm.amount_transfered + a.balance
                                walt.balance = walt.balance - userm.amount_transfered
                                stat = Statistics.objects.get(user="xampesa")
                                Prc.adcash = Prc.adcash - mor
                                stat.bitcoin_profit = stat.bitcoin_profit + whoa
                                walt.save()
                                stat.save()
                                a.save()
                                Prc.save()
                                userm.save()
                                messages.success(request, '%s USD, Has been successful transferred to  %s ' % (m, n))
                                return redirect(reverse('app:account'))
                        else:
                            messages.success(request, 'Security code entered is not correct ')
                            return redirect(reverse('app:Balance'))
                else:

                    return redirect(reverse('app:account'))
            else:
                messages.success(request, 'Dear %s, This account number you entered (%s), does not exists' %(request.user, d))
                return redirect(reverse('app:Balance'))
        elif userm.currency_transfered == Bitcoin:
            d = userm.username_receiver
            m = userm.amount_transfered
            Pub = Investment.objects.filter(account_no=d)
            inst = UserInfo.objects.get(user=request.user.pk)

            if Pub.exists():
                kim = Investment.objects.get(account_no=d)
                n = kim.user
                whoa = userm.amount_transfered * 0.05
                mor = whoa + userm.amount_transfered
                if walt.Bitcoin_balance >= mor:
                    if Prc.bitcoin >= mor:

                        if userm.security_code == inst.security_code:
                            for a in Pub:
                                a.Bitcoin_balance = userm.amount_transfered + a.Bitcoin_balance
                                walt.Bitcoin_balance = walt.Bitcoin_balance - mor
                                stat = Statistics.objects.get(user="xampesa")
                                Prc.bitcoin = Prc.bitcoin - mor
                                stat.bitcoin_profit = stat.bitcoin_profit + whoa
                                walt.save()
                                a.save()
                                Prc.save()
                                stat.save()
                                userm.save()
                                messages.success(request, '%s BTC, Has been successful transferred to  %s ' % (m, n))
                                return redirect(reverse('app:account'))
                        else:
                            messages.success(request, 'Security code entered is not correct ')
                            return redirect(reverse('app:Balance'))
                else:

                    return redirect(reverse('app:account'))
            else:
                messages.success(request,
                                 'Dear %s, This account number you entered (%s), does not exists' % (request.user, d))
                return redirect(reverse('app:Balance'))


    return render(request, 'balancetransaction.html', context)


@login_required(login_url='/login/')
def balanceredeposit(request, id=None):
    title = 'Welcome to Xampesa'
    if request.user.is_authenticated():
        title = " %s" %request.user
    walt = UserInfo.objects.get(user=request.user.pk)

    form = BalanceRedepositForm(request.POST or None, request.FILES or None)

    context = {
        "title": title.title(),
        "form": form
        }
    if form.is_valid():
        userm = form.save(commit=False)
        d = userm.Xumpesa_account
        mor = Investment.objects.filter(account_no=d)
        Pub = Investment.objects.get(user=request.user.pk)
        if userm.amount_transfered <= Pub.balance:
            for mo in mor:
                walt.amount = walt.amount + userm.amount_transfered
                mo.balance = mo.balance + userm.amount_transfered
                Pub.balance = Pub.balance - userm.amount_transfered

                userm.actualDeposit = userm.amount_transfered
                walt.total_deposit = walt.total_deposit + userm.amount_transfered
                prom = Processors.objects.get(user=request.user)
                prom.XamCoin = prom.XamCoin + userm.amount_transfered
                if userm.package == Silver:
                    enddate = timezone.now() + timedelta(30)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )


                elif userm.package == Tarnish:
                    enddate = timezone.now() + timedelta(30)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid = code_generator()
                                                          )


                elif userm.package == Charoite:
                    enddate = timezone.now() + timedelta(30)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()

                                                          )

                elif userm.package == TANZANITE:
                    enddate = timezone.now() + timedelta(60)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )

                elif userm.package == Karat:
                    enddate = timezone.now() + timedelta(60)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )
                elif userm.package == Corundum:
                    enddate = timezone.now() + timedelta(60)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )

                elif userm.package == TITANIUM:
                    enddate = timezone.now() + timedelta(90)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )
                elif userm.package == Niello:
                    enddate = timezone.now() + timedelta(90)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )

                elif userm.package == Zircorn:
                    enddate = timezone.now() + timedelta(90)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )
                elif userm.package == DIAMOND:
                    enddate = timezone.now() + timedelta(30)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )

                elif userm.package == Gold:
                    enddate = timezone.now() + timedelta(125)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )
                elif userm.package == Platnum:
                    enddate = timezone.now() + timedelta(100)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )

                elif userm.package == Carbon:
                    enddate = timezone.now() + timedelta(100)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )
                elif userm.package == Quartz:
                    enddate = timezone.now() + timedelta(100)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )

                elif userm.package == Pearl:
                    enddate = timezone.now() + timedelta(125)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )

                elif userm.package == Copper:
                    enddate = timezone.now() + timedelta(5)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )

                elif userm.package == Lapls:
                    enddate = timezone.now() + timedelta(5)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )
                elif userm.package == Emerald:
                    enddate = timezone.now() + timedelta(5)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )

                elif userm.package == Iron:
                    enddate = timezone.now() + timedelta(7)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )
                elif userm.package == Glass:
                    enddate = timezone.now() + timedelta(7)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )

                elif userm.package == Moisanite:
                    enddate = timezone.now() + timedelta(7)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )
                elif userm.package == Calcite:
                    enddate = timezone.now() + timedelta(15)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )

                elif userm.package == Sapphire:
                    enddate = timezone.now() + timedelta(15)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )


                elif userm.package == Ruby:
                    enddate = timezone.now() + timedelta(15)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )
                elif userm.package == Amber:
                    enddate = timezone.now() + timedelta(30)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )

                elif userm.package == Agate:
                    enddate = timezone.now() + timedelta(30)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )
                elif userm.package == Amazonnile:
                    enddate = timezone.now() + timedelta(30)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )

                elif userm.package == Beads:
                    enddate = timezone.now() + timedelta(50)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )
                elif userm.package == Beryl:
                    enddate = timezone.now() + timedelta(50)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )

                elif userm.package == Azuriite:
                    enddate = timezone.now() + timedelta(50)
                    sav = DepositsVerified.objects.create(user=userm.user,
                                                          username=userm.username,
                                                          processor=userm.processor,
                                                          amount_deposited=userm.amount_transfered,
                                                          package=userm.package,
                                                          startdate=timezone.now(),
                                                          enddate=enddate,
                                                          hashid=code_generator()
                                                          )

                walt.save()
                mo.save()
                sav.save()
                Pub.save()
                prom.save()
                userm.save()
                return redirect(reverse('app:account'))
        else:
            return redirect(reverse('app:Redeposit'))
    return render(request, 'balanceredeposit.html', context)


class history_to(generic.ListView):
    model = BalanceTransaction
    template_name = 'history_to.html'

    def get_context_data(self, **kwargs):
        context = super(history_to, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        cout = UserInfo.objects.get(user=self.request.user.pk)
        walte = cout.user
        context['send'] = BalanceTransaction.objects.filter(user=walte)
        return context


class history_from(generic.ListView):
    login_required = True
    model = BalanceTransaction
    template_name = 'Receivinghistory.html'

    def get_context_data(self, **kwargs):
        context = super(history_from, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        cout = Investment.objects.get(user=self.request.user.pk)
        walt = cout.account_no
        context['receive'] = BalanceTransaction.objects.filter(username_receiver=walt)
        return context


def recurence(request):
    wamba = UserInfo.objects.get(amount=request.user.pk)
    wolt = Investment.objects.all()
    for m in wolt:
        for w in wamba:

            if w.amount >= 10000:
                m.balance = w.amount * 2
                print(m.balance)
                m.save()


class Verification(generic.CreateView):
    template_name = 'verification_code.html'
    form_class = VerificationForm
    success_url = reverse_lazy('app:account')

    def get_context_data(self, **kwargs):
        context = super(Verification, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        coz = UserInfo.objects.get(user=self.request.user.pk)
        watr = coz.user
        moz = Deposits.objects.filter(user=watr).order_by('-id')[0]
        context['cout'] = moz
        return context

    # def get_queryset(self):
    #     coz = UserInfo.objects.get(user=self.request.user.pk)
    #     watr = coz.user
    #     return Deposits.objects.filter(user=watr)

    def form_valid(self, form):
        user = form.save(commit=False)
        mor = UserInfo.objects.get(user=self.request.user.pk)
        cout = Investment.objects.get(user=self.request.user.pk)
        cota = cout.user
        M = Deposits.objects.filter(user=cota, shortcode=user.verification_code)
        more = DepositsVerified.objects.filter(verification_code=user.verification_code)

        # c = more.get()
        # k = M.get(shortcode=user.verification_code)
        # walt = cout.user
        # moz = DepositsVerified.objects.filter(user=walt, status='Verified').order_by('-timestamp')[0]
        # woza = UserInfo.objects.get(user=self.request.user.pk)
        # flt = Deposits.objects.filter(user=woza).order_by('-id')
        # if flt.shortcode != user.verification_code:
        #     return redirect(reverse('app:verification'))
        # else:
        if M.exists():
            if more.exists():

                return redirect(reverse("app:verification"))
            else:
                mor.amount = mor.amount + user.depositing_amount
                moa = DepositsVerified.objects.update(status='Verified')
                # m = Deposits.objects.update(status=Verified)
                mor.save()
                user.save()
                return redirect(reverse("app:account"))

        else:
            return redirect(reverse("app:index"))


class Verificationdetail(generic.CreateView):
    template_name = 'verification_code.html'
    form_class = VerificationForm
    success_url = reverse_lazy('app:account')

    def get_context_data(self, **kwargs):
        context = super(Verificationdetail, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        coz = UserInfo.objects.get(user=self.request.user.pk)
        watr = coz.user
        moz = Deposits.objects.filter(user=watr).order_by('-id')[0]
        context['cout'] = moz
        return context

    # def get_queryset(self):
    #     coz = UserInfo.objects.get(user=self.request.user.pk)
    #     watr = coz.user
    #     return Deposits.objects.filter(user=watr)

    def form_valid(self, form):
        user = form.save(commit=False)
        mor = UserInfo.objects.get(user=self.request.user.pk)
        cout = Investment.objects.get(user=self.request.user.pk)
        cota = cout.user
        M = Deposits.objects.filter(user=cota, shortcode=user.verification_code)
        more = DepositsVerified.objects.filter(verification_code=user.verification_code)

        # c = more.get()
        # k = M.get(shortcode=user.verification_code)
        # walt = cout.user
        # moz = DepositsVerified.objects.filter(user=walt, status='Verified').order_by('-timestamp')[0]
        # woza = UserInfo.objects.get(user=self.request.user.pk)
        # flt = Deposits.objects.filter(user=woza).order_by('-id')
        # if flt.shortcode != user.verification_code:
        #     return redirect(reverse('app:verification'))
        # else:
        if M.exists():
            if more.exists():

                return redirect(reverse("app:verificationdetail"))
            else:
                mor.amount = mor.amount + user.depositing_amount
                moa = DepositsVerified.objects.update(status='Verified')
                m = Deposits.objects.update(status=Verified)
                mor.save()
                user.save()
                return redirect(reverse("app:account"))

        else:
            return redirect(reverse("app:index"))

class Verifiedm(generic.ListView):
    template_name = 'verified.html'

    # def get_context_data(self, **kwargs):
    #     context = super(Verifiedm, self).get_context_data(**kwargs)
    #     context['user'] = self.request.user
    #     cout = Deposits.objects.get(user=self.request.user.pk)
    #     watre = cout.user
    #     # filtered = DepositsVerified.objects.get(user=watre)
    #     # mostvrfd = filtered.status
    #     context['verified'] = DepositsVerified.objects.filter(user=watre, status='Verified')
    #     return context

    def get_queryset(self):
        cout = UserInfo.objects.get(user=self.request.user.pk)
        watre = cout.user
        # filtered = DepositsVerified.objects.get(user=watre)
        # mostvrfd = filtered.status
        return DepositsVerified.objects.filter(user=watre).order_by('-id')


class unVerifiedm(generic.ListView):
    model = DepositsVerified
    template_name = 'unverified.html'

    def get_context_data(self, **kwargs):
        context = super(unVerifiedm, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        cout = UserInfo.objects.get(user=self.request.user.pk)
        watre = cout.user
        # filtered = DepositsVerified.objects.get(user=watre)
        # mostvrfd = filtered.status
        # context['pending'] = DepositsVerified.objects.filter(user=watre, status=Not_verified)
        return context

    # def get_queryset(self):
    #     cout = UserInfo.objects.get(user=self.request.user.pk)
    #     watre = cout.user
    #     # filtered = DepositsVerified.objects.get(user=watre)
    #     # mostvrfd = filtered.status
    #     return DepositsVerified.objects.filter(user=watre, status='Not verified')



class VerifiedDetails(generic.DetailView):
    model = DepositsVerified
    template_name = 'VerifiedDetais.html'




# def home(request):
#     num = random.randint(0, 10000)
#     some_list = [num, random.randint(0, 10000), random.randint(0, 10000)]
#     context = {
#         "bool_item": True,
#         "num": num,
#         "some_list": some_list
#     }
#     return render(request, 'index.html', context)


@login_required(login_url='/login/')
def tigowithdraw(request):
    title = 'Welcome to Xampesa'
    button = "Request"
    processor = 'TIGO'
    mtandao = "tigopesa"
    if request.user.is_authenticated():
        title = "Dear %s, you are going to use tigopesa withdrawing to your balance" %request.user
        Request = "withdraw"
        processor = 'TIGO'
        mtandao = "tigopesa"

    content = Investment.objects.get(user=request.user.pk)
    form = TigopesaWithdrawForm(request.POST or None)
    context = {
        "title":title,
        "form": form,
        "button": Request,
        "mtandao": mtandao,
        "processor": processor,

        }

    if form.is_valid():
        user_withdraw = form.save(commit=False)
        if content.balance >= user_withdraw.withdrawing_amount:
            content.balance = content.balance - user_withdraw.withdrawing_amount

            user_withdraw.save()
            content.save()
            messages.success(request, "REQUEST SUCCESS")
            return redirect(reverse('app:withdraw'))
        else:
            messages.error(request, "Insufficient fund")
            return redirect(reverse('app:tigopesawithdraw'))

    return render(request, 'balancewithdrawal.html', context)


@login_required(login_url='/login/')
def mpesawithdraw(request):
    title = 'Welcome to Xampesa'
    button = "Request"
    processor = 'MPESA'
    mtandao = "mpesa"
    if request.user.is_authenticated():
        processor = 'MPESA'
        title = "Dear %s, you are going to use mpesa withdrawing to your balance" %request.user
        Request = "withdraw"
        mtandao = "mpesa"
    content = Investment.objects.get(user=request.user.pk)
    form = MpesaWithdrawForm(request.POST or None)
    context = {
        "title":title,
        "form": form,
        "button": Request,
        "mtandao": mtandao,
        "processor": processor
        }

    if form.is_valid():
        user_withdraw = form.save(commit=False)
        if content.balance >= user_withdraw.withdrawing_amount:
            content.balance = content.balance - user_withdraw.withdrawing_amount
            user_withdraw.save()
            content.save()
            messages.success(request, "REQUEST SUCCESS")
            return redirect(reverse('app:withdraw'))
        else:
            messages.error(request, "Insufficient fund")
            return redirect(reverse('app:mpesawithdraw'))
    return render(request, 'balancewithdrawal.html', context)


@login_required(login_url='/login/')
def AirtelWithdraw(request):
    title = 'Welcome to Xampesa'
    button = "Request"
    mtandao = "Airtelmoney"

    processor = 'AIRTELMONEY'
    if request.user.is_authenticated():
        processor = 'AIRTELMONEY'
        title = "Dear %s, you are going to use airtel money withdrawing to your balance" %request.user
        Request = "withdraw"
        mtandao = "airtelmoney"

    content = Investment.objects.get(user=request.user.pk)
    form = AirtelWithdrawForm(request.POST or None)
    context = {
        "title":title,
        "form": form,
        "button": Request,
        "mtandao": mtandao,
        "processor": processor
        }

    if form.is_valid():
        user_withdraw = form.save(commit=False)
        if content.balance >= user_withdraw.withdrawing_amount:
            content.balance = content.balance - user_withdraw.withdrawing_amount
            user_withdraw.save()
            content.save()
            messages.success(request, "REQUEST SUCCESS")
            return redirect(reverse('app:withdraw'))
        else:
            messages.error(request, "Insufficient fund")
            return redirect(reverse('app:airtelmoneywithdraw'))

    return render(request, 'balancewithdrawal.html', context)



class SelectType(generic.TemplateView):
    template_name = 'selecttype.html'



class intermediateDeposit(generic.TemplateView):
    template_name = 'intermediateDeposit.html'


class accountbalance(generic.TemplateView):
    template_name = 'accountbalance.html'

class AdvancedBalancedepositView(generic.CreateView):
    template_name = 'advencedDeposit.html'
    form_class = AdvCashBalanceDepositForm
    success_url = reverse_lazy('app:interDeposit')

    def form_valid(self, form):
        user = form.save(commit=False)
        getamount = UserInfo.objects.get(user=self.request.user)
        getprocessor = Processors.objects.get(user=self.request.user)
        getbalance = Investment.objects.get(user=self.request.user)
        getprocessor.adcash = getprocessor.adcash + user.a_amount
        getbalance.balance = getbalance.balance + user.a_amount
        getbalance.save()
        getprocessor.save()
        user.save()
        return redirect(reverse('app:interDeposit'))


class OKpayBalancedepositView(generic.CreateView):
    template_name = 'okpaybalancedeposit.html'
    form_class = OKPayBalanceDepositForm
    success_url = reverse_lazy('app:interDeposit')

    def form_valid(self, form):
        user = form.save(commit=False)
        getamount = UserInfo.objects.get(user=self.request.user)
        getprocessor = Processors.objects.get(user=self.request.user)
        getbalance = Investment.objects.get(user=self.request.user)
        getbalance.balance = getbalance.balance + user.o_amount
        getprocessor.okpay = getprocessor.okpay + user.o_amount
        getbalance.save()
        getprocessor.save()
        user.save()
        return redirect(reverse('app:interDeposit'))

class PerfectMoneyBalancedepositView(generic.CreateView):
    template_name = 'perfectmoneybalancedeposit.html'
    form_class = PerfectMoneyrBalanceDepositForm
    success_url = reverse_lazy('app:interDeposit')

    def form_valid(self, form):
        user = form.save(commit=False)
        getamount = UserInfo.objects.get(user=self.request.user)
        proc = Processors.objects.get(user=self.request.user)
        getbalance = Investment.objects.get(user=self.request.user)
        getbalance.balance = getbalance.balance + user.p_amount
        proc.perfectmoney = proc.perfectmoney + user.p_amount
        proc.save()
        getbalance.save()
        user.save()
        return  redirect(reverse('app:interDeposit'))


class PayeerBalancedepositView(generic.CreateView):
    template_name = 'payeerbalancedeposit.html'
    form_class = PayeerBalanceDepositForm
    success_url = reverse_lazy('app:interDeposit')

    def form_valid(self, form):
        user = form.save(commit=False)
        getamount = UserInfo.objects.get(user=self.request.user)
        getbalance = Investment.objects.get(user=self.request.user)
        getbalance.balance = getbalance.balance + user.m_amount
        getbalance.save()
        user.save()
        return  redirect(reverse('app:interDeposit'))


class BitcoinBalancedepositView(generic.CreateView):
    template_name = 'bitcoinbalancedeposit.html'
    form_class = bitcoinBalanceDepositForm
    success_url = reverse_lazy('app:interDeposit')

    def form_valid(self, form):
        user = form.save(commit=False)
        getamount = UserInfo.objects.get(user=self.request.user)
        Proc = Processors.objects.get(user=self.request.user)
        getbalance = Investment.objects.get(user=self.request.user)
        Proc.bitcoin = Proc.bitcoin + user.b_amount
        getbalance.Bitcoin_balance = getbalance.Bitcoin_balance + user.b_amount
        getbalance.save()
        Proc.save()
        user.save()
        return redirect(reverse('app:interDeposit'))