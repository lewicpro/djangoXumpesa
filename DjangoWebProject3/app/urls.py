from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordChangeView, PasswordChangeDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views
app_name = 'app'

urlpatterns = [

                url(r'^$', views.index, name='index'),
                url(r'^About/$', views.About, name='About'),
                url(r'^plans/$', views.Plans, name='Plans'),
                url(r'^terms/$', views.terms, name='terms'),
                # url(r'^verify/$', views.verify, name='verify'),
                url(r'^register/$', views.register, name='register'),
                url(r'^api/$', views.ApiView.as_view(), name='apiview'),
                url(r'^api/(?P<pk>[0-9]+)/', views.AppApiDetailsView.as_view(), name='apiviewdetails'),
                url(r'^Historygo/', views.history_to.as_view(), name='hist'),
                url(r'^Historyfrom/', views.history_from.as_view(), name='history_fro'),




                url(r'^login/$', views.login_view, name='login'),
                url(r'^logout/$', views.logout_view, name='logout'),



                url(r'^authorized/$', views.authorized, name='authorized'),
                url(r'^account/$', views.account, name='account'),
                url(r'^withdraw/$',views.withdraw, name='withdraw'),
                url(r'^deposit/$',views.deposit, name='deposit'),
                url(r'^account/(?P<pk>\d+)/$', views.account, name='account_with_pk'),
                url(r'^Change-password/$', views.Editpassword, name='Editpassword'),
                url(r'^password-reset/$', PasswordResetView.as_view(template_name='password_reset.html',
                                                                    success_url=reverse_lazy('app:password_reset_done'),
                                                                    email_template_name='password_reset_email.html',
                                                                    subject_template_name='password_reset_subject.txt',), name='password_reset'),


                url(r'^password-reset/done/$', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),



                url(r'^Withdraw/tigiopesa/$', views.tigowithdraw, name='tigopesawithdraw'),
                url(r'^Withdraw/mpesawithdraw/$', views.mpesawithdraw, name='mpesawithdraw'),
                url(r'^Withdraw/airtelwithdraw/$', views.AirtelWithdraw, name='airtelmoneywithdraw'),
                url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', success_url=reverse_lazy('app:password_reset_complete')), name='password_reset_confirm'),
                url(r'^editaccount/$', views.editaccount, name='editaccount'),
                url(r'^password-reset/complete/$', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),



                url(r'^Faq/$', views.Faq, name='Faq'),
                url(r'^(?P<pk>[0-9]+)/Detail/$', views.VerifiedDetails.as_view(), name='Vdetails'),
                # url(r'^(?P<code>[a-z0-9]+). */$', views.activate_user_view, name='activate_user'),
                url(r'^regform2/$', views.regform2, name='regform2'),
                url(r'^tigopesa/', views.tigopesa, name='tigopesa'),
                url(r'^verification/$', views.Verification.as_view(), name='verification'),
                url(r'^verification/(?P<pk>[0-9]+)/$', views.Verificationdetail.as_view(), name='verificationdetail'),
                url(r'^verifie/$', views.Verifiedm.as_view(), name='verified'),
                url(r'^unverifie/$', views.unVerifiedm.as_view(), name='unverified'),
                url(r'^Chooseoptions/$', views.intermediateDeposit.as_view(), name='interDeposit'),
                url(r'^AdvCash/$', views.AdvancedBalancedepositView.as_view(), name='AdvcashBalanceDeposit'),
                url(r'^OK-Pay/$', views.OKpayBalancedepositView.as_view(), name='OKpayBalancedeposittemp'),
                url(r'^OK-Paydeposit/$', views.OkPaydepositView, name='OkPaydepositView'),
                url(r'^advcasdeposit/$', views.AdvCashDepositView, name='AdvCashDepositView'),
                url(r'^Perfectmoneybalancedeposit/$', views.PerfectMoneyBalancedepositView.as_view(), name='PerfectMoneyBalancedeposittemp'),
                url(r'^Payeerbalance-deposit/$', views.PayeerBalancedepositView.as_view(), name='PayeerBalancedeposittemp'),
                url(r'^Bitcoin-balance-deposit/$', views.BitcoinBalancedepositView.as_view(), name='BitcoinBalancedeposittemp'),
                url(r'^Bitcoin-BitcoinRedepositView-deposit/$', views.BitcoinRedepositView, name='BitcoinRedepositView'),
                url(r'^accountbalance/$', views.accountbalance.as_view(), name='accountbalance'),
                url(r'^selecttype/$', views.SelectType.as_view(), name='selecttype'),
                url(r'^mpesa/$', views.mpesa, name='mpesa'),
                url(r'^airtelmoney/', views.airtelmoney, name='airtelmoney'),
                url(r'^payeer/$', views.payeertransaction, name='payeer'),
                url(r'^Bitcoin/$', views.BitcoinTransactions, name='bitco'),
                url(r'^withdrawp/$', views.payeerWithdraw, name='payeerwithdraw'),
                url(r'^BitcoinWithdraw/$', views.BitcoinWithdrawModelViews.as_view(), name='BitcoinWithdraw'),
                url(r'^withdrawperfect/$', views.perFectmoneyWithdraw, name='perfectwithdraw'),
                url(r'^withdrawokpay/$', views.okpaywithdrawview, name='withdrawokpay'),
                url(r'^withdrawadvcash/$', views.Advcashwithdraw, name='withdrawadvcash'),
                url(r'^account_type/$', views.account_type, name='account_type'),
                url(r'^Wallet/$', views.wallet, name='wallet'),
                url(r'^Balancetransaction/$', views.BalanceTransactionview, name='Balance'),
                url(r'^Redeposit/$', views.balanceredeposit, name='Redeposit'),

]
