from django.contrib import admin

from .models import UserInfo, \
    Investment, \
    Deposits, \
    TransactionPerfectMoney, \
    TransactionPayeer, \
    BalanceTransaction, \
    BalanceRedeposit, \
    DepositsVerified, \
    Withdraw, \
    Statistics, \
    Withdrawprocessor, \
    Processors, \
    VerifiedWithdrawals, \
    TransactionBitcoin, \
    OKPayBalanceDeposit, \
    bitcoinBalanceDeposit, \
    AdvCashBalanceDeposit, \
    PayeerBalanceDeposit, \
    PerfectMoneyrBalanceDeposit, \
    OKpayDeoisitModel, \
    AdvCashDeposit, \
    BitcoinRedepositModels

from .forms import UserInfoForm, InvestmentForm


def verified (Modeladmin, request, queryset):
    queryset.update(status='Verified')


def not_verified(Modeladmin, request, queryset):
    queryset.update(status='Not verified')


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ["user", "full_name", "Phone_no", "Perfect_money", "Bitcoin", "Payeer", "advcash", "country", "timestamp", "updated", "amount", "bitcoin_amount", "total_deposit", "total_bitcoin_deposit",
                    "verification_code", "Bio", "shortcode"]
    # list_editable = ["verification_code"]


class InvestmentAdmin(admin.ModelAdmin):
    list_display = ["user", "account_no", "balance", "account_type", "Bitcoin_balance", "pending_withdrawal", "last_withdrawal"]

class StasticAdmin(admin.ModelAdmin):
    list_display = ["user", "profit", "total_deposited", "total_withdrawn", "last_withdrawn", "total_balance", "bitcoin_profit", "bitcoin_total_deposited", "bitcoin_total_withdrawn", "bitcoin_last_withdrawn", "bitcoin_total_balance"]






class VerifiedwithdrawalsAdmin(admin.ModelAdmin):
    list_display = ["user", "full_name", "processor", "processor_account_number", "m_amount", "timestamp", "Status"]














class DepositsAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "depositing_amount", "name", "package", "account_number", "processor", 'kumbukumbu_no', 'shortcode', "closes","opens", ]
    # list_editable = ['kumbukumbu_no']

class DepositsVerifiedAdmin(admin.ModelAdmin):
    list_display = ["user", "username", "processor", "amount_deposited", "package",  "startdate", "enddate", "sign", "hashid"]
    # list_editable = ['kumbukumbu_no']



class ProcessorsAdmin(admin.ModelAdmin):
    list_display = ["user", "payeer", "perfectmoney", "bitcoin", "adcash",  "Etherium", "XamCoin", "okpay"]






class TransactionPerfectMoneyAdmin(admin.ModelAdmin):
    list_display = ["user", "package", "username", "processor", "PAYMENT_AMOUNT", "date" , "closes", "opens", "Plan", "actualDeposit", "sign", "hashid", "expectedIncome"]





class OkpayModelAdmin(admin.ModelAdmin):
    list_display = ["user", "package", "username", "processor", "o_amount", "date" , "closes", "opens", "Plan", "actualDeposit", "sign", "hashid", "expectedIncome"]



class AdvCashDepositAdmin(admin.ModelAdmin):
    list_display = ["user", "package", "username", "processor", "a_amount", "date" , "closes", "opens", "Plan", "actualDeposit", "sign", "hashid", "expectedIncome"]






class TransactionBitcoinAdmin(admin.ModelAdmin):
    list_display = ["user", "package", "username", "processor", "b_amount", "date" , "closes", "opens", "Plan", "actualDeposit", "sign", "hashid", "expectedIncome"]





class BitcoinRedepositAdmin(admin.ModelAdmin):
    list_display = ["user", "package", "username", "processor", "b_amount", "date" , "closes", "opens", "Plan", "actualDeposit", "sign", "hashid", "expectedIncome"]




class TransactionPayeerAdmin(admin.ModelAdmin):
    list_display = ["user", "package", "username", "processor", "m_amount", "actualDeposit", "date", "opens", "closes", "Plan", "sign", "hashid", "expectedIncome"]





class OKPayBalanceDepositAdmin(admin.ModelAdmin):
    list_display = ["user", "username", "processor", "o_amount", "actualDeposit", "date", "sign", "hashid"]


class bitcoinBalanceDepositAdmin(admin.ModelAdmin):
    list_display = ["user", "username", "processor", "b_amount", "actualDeposit", "date", "sign", "hashid"]


class AdvCashBalanceDepositAdmin(admin.ModelAdmin):
    list_display = ["user", "username", "processor", "a_amount", "actualDeposit", "date", "sign", "hashid"]


class PayeerBalanceDepositAdmin(admin.ModelAdmin):
    list_display = ["user", "username", "processor", "m_amount", "actualDeposit", "date", "sign", "hashid"]


class PerfectMoneyrBalanceDepositAdmin(admin.ModelAdmin):
    list_display = ["user", "username", "processor", "p_amount", "actualDeposit", "date", "sign", "hashid"]


class WithdrawprocessorAdmin(admin.ModelAdmin):
    list_display = ["user", "full_name", "balance", "processor", "m_amount", "processor_acc_number", "account_number", "timestamp", "status"]



class BitcoinWithdrawModelAdmin(admin.ModelAdmin):
    list_display = ["user", "full_name", "balance", "processor", "b_amount", "processor_acc_number", "account_number", "timestamp", "status"]











class BalanceTransactionAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "from_account_no", "username_receiver", "amount_transfered", "date_stamp", "currency_transfered"]

# class WithdrawAdmin(admin.ModelAdmin):
#     list_display = ["user", "tigopesa_number", "full_name", "processor", "withdrawing_amount",  "balance",
#                     "timestamp", "account_number", "status"]
class BalanceRedepositAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "package", "closes", "opens", "Xumpesa_account", "amount_transfered", "expectedIncome", "date_stamp", "Plan", "hashid", "actualDeposit", "sign"]














admin.site.register(Deposits, DepositsAdmin)
admin.site.register(DepositsVerified, DepositsVerifiedAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Investment, InvestmentAdmin)
# admin.site.register(Withdraw, WithdrawAdmin)
admin.site.register(TransactionPerfectMoney, TransactionPerfectMoneyAdmin)
admin.site.register(TransactionPayeer, TransactionPayeerAdmin)
admin.site.register(BalanceTransaction, BalanceTransactionAdmin)
admin.site.register(BalanceRedeposit, BalanceRedepositAdmin)
admin.site.register(Statistics, StasticAdmin)
admin.site.register(Withdrawprocessor, WithdrawprocessorAdmin)
admin.site.register(Processors, ProcessorsAdmin)
admin.site.register(VerifiedWithdrawals, VerifiedwithdrawalsAdmin)
admin.site.register(TransactionBitcoin, TransactionBitcoinAdmin)
admin.site.register(OKPayBalanceDeposit, OKPayBalanceDepositAdmin)
admin.site.register(bitcoinBalanceDeposit, bitcoinBalanceDepositAdmin)
admin.site.register(AdvCashBalanceDeposit, AdvCashBalanceDepositAdmin)
admin.site.register(PayeerBalanceDeposit, PayeerBalanceDepositAdmin)
admin.site.register(PerfectMoneyrBalanceDeposit, PerfectMoneyrBalanceDepositAdmin)
admin.site.register(OKpayDeoisitModel, OkpayModelAdmin)
admin.site.register(AdvCashDeposit, AdvCashDepositAdmin)
admin.site.register(BitcoinRedepositModels, BitcoinRedepositAdmin)











