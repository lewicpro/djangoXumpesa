from django import forms
from django.db.models import Count
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )


User = get_user_model()
from .models import *
from .validators import *
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 100%; padding-bottom: 3%'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Passwords', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        um = UserInfo.objects.filter(user__username=username)
        if um.exists():
            if username and password:
                user = authenticate(username=username, password=password)
                if not user:
                    raise forms.ValidationError("Try to check your password")
                elif not user.check_password(password):
                    raise forms.ValidationError("password ulioingiza sio sahihi")
                elif not user.is_active:
                    raise forms.ValidationError("mtumiaji ulomjaza hatumii tena account yake.")
            return super(UserLoginForm, self).clean(*args, **kwargs)
        else:
            raise forms.ValidationError("User is not in the system")



class UserRegisterForm(forms.ModelForm):
    first_name= forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'first name', 'style': 'width: 100%; padding-bottom: 3%;'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'last name', 'style': 'width: 100%; padding-bottom: 3%'}))
    # products = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Products', 'style': 'width: 100%; padding-bottom: 3%'}))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username', 'style': 'width: 100%; padding-bottom: 3%'}))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email address', 'style': 'width: 100%; padding-bottom: 3%'}))
    email2 = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Confirm email', 'style': 'width: 100%; padding-bottom: 3%'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Passwords', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'email2',
            'password'
                              
]


    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('this email has already been used')
        return email

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()

        return user

    def Validate(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Length of the password should be more than 8 characters"

            )
        return password

class UserInfoForm(forms.ModelForm):

    full_name= forms.CharField(label='', validators=[clean_full_name], widget=forms.TextInput(attrs={'placeholder': 'full name', 'style': 'width: 100%; padding-bottom: 3%;'}))
    Phone_no = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Phone no', 'style': 'width: 100%; padding-bottom: 3%'}))
    Perfect_money = forms.CharField(label='', required=False,  widget=forms.TextInput(attrs={'placeholder': 'Perfect money account', 'style': 'width: 100%; padding-bottom: 3%'}))
    Bitcoin = forms.CharField(label='',required=False, widget=forms.TextInput(attrs={'placeholder': 'Bitcoin account', 'style': 'width: 100%; padding-bottom: 3%'}))
    Payeer = forms.CharField(label='',required=False, widget=forms.TextInput(attrs={'placeholder': 'Payeer account ---option---', 'style': 'width: 100%; padding-bottom: 3%'}))
    advcash = forms.CharField(label='',required=False, widget=forms.TextInput(attrs={'placeholder': 'AdvCash account', 'style': 'width: 100%; padding-bottom: 3%'}))
    # amount = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'amount', 'style': 'width: 100%; padding-bottom: 3%'}))
    Bio = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Bio ', 'style': 'width: 100%; padding-bottom: 3%'}))
    security_code = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Security code', 'style': 'width: 100%; padding-bottom: 3%'}))
    # email2 = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Confirm email', 'style': 'width: 100%; padding-bottom: 3%'}))
    # password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Passwords', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)

    class Meta:
        model = UserInfo

        fields = [
            'full_name',
            'Phone_no',
            'Perfect_money',
            'Bitcoin',
            'Payeer',
            'advcash',
            'country',
            'Bio',
            'security_code',

                  ]




class InvestmentForm(forms.ModelForm):
    # requested_amount = forms.ChoiceField(choices=pack, label="", initial='', widget=forms.RadioSelect(attrs={'style': 'width: 100%', 'type': 'radio', "type": "text",'required': True}), )  # user = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'email', 'style': 'width: 100%; padding-bottom: 3%;'}))
    requested_amount = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'amount', 'style': 'width: 100%; padding-bottom: 3%', "class": "textinput textInput form-control ",'required': True}))
    # processor = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'wallet', 'style': 'width: 100%; padding-bottom: 3%'}))
    # PAYMENT_AMOUNT = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Depositing amount', 'style': 'width: 100%; padding-bottom: 3%'}))

    class Meta:
        model = Investment

        fields = [
                  'account_type',
                  'requested_amount'
                  ]
        

class Editaccount(UserChangeForm):
    email= forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'email', 'style': 'width: 100%; padding-bottom: 3%;'}))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'username', 'style': 'width: 100%; padding-bottom: 3%'}))
    # products = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Products', 'style': 'width: 100%; padding-bottom: 3%'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'first name', 'style': 'width: 100%; padding-bottom: 3%'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'last name', 'style': 'width: 100%; padding-bottom: 3%'}))
    email2 = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Confirm email', 'style': 'width: 100%; padding-bottom: 3%'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Passwords', 'style': 'width: 100%; padding-bottom: 3%'}), required=True, disabled=True)
    class Meta:
        model = User
        fields = {
            'email',
            'username',
            'first_name',
            'last_name',
            'password'
            }


class BitcoinForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'name', 'style': 'width: 100%; padding-bottom: 3%'}))
    depositing_amount = forms.FloatField(label='', min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'depositing_amount', 'style': 'width: 100%; padding-bottom: 3%', "class": "textinput textInput form-control ", 'required': True}))
    verification_code = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'verification_code', "class": "textinput textInput form-control ", 'style': 'width: 100%; padding-bottom: 3%'}))
    #PAYMENT_AMOUNT = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Depositing amount', 'style': 'width: 100%; padding-bottom: 3%'}))


    class Meta:
        model = Deposits
        fields = {
            'name',
            'depositing_amount',
            'verification_code'

        }


class TigopesaForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'name', 'style': 'width: 100%; padding-bottom: 3%', "class": "textinput textInput form-control ",'required': True}))
    account_number = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'account number', 'style': 'width: 100%; padding-bottom: 3%',"class": "textinput textInput form-control ", 'required': True}))
    package = forms.ChoiceField(choices=pack, label="", initial='', widget=forms.RadioSelect(attrs={'style': 'width: 100%', 'type': 'radio', "type": "text",'required': True}), )
    depositing_amount = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'depositing amount', "class": "textinput textInput form-control ", 'style': 'width: 100%; padding-bottom: 3%'}))
    kumbukumbu_no = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'kumbukumbu number', "class": "textinput textInput form-control ", 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = Deposits
        fields = {
            'user',
            'name',
            'package',
            'processor',
            'account_number',
            'depositing_amount',
            'kumbukumbu_no'

        }


class AirtelMoneyForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'name', 'style': 'width: 100%; padding-bottom: 3%',"class": "textinput textInput form-control ", 'required': True}))
    account_number = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'account_number', 'style': 'width: 100%; padding-bottom: 3%',"class": "textinput textInput form-control ", 'required': True}))
    package = forms.ChoiceField(choices=pack, label="", initial='', widget=forms.RadioSelect(attrs={'style': 'width: 100%', 'type': 'radio', "type": "text",'required': True}), )
    depositing_amount = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'depositing_amount', "class": "textinput textInput form-control ", 'style': 'width: 100%; padding-bottom: 3%'}))
    kumbukumbu_no = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'kumbukumbu number', "class": "textinput textInput form-control ", 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = Deposits
        fields = {
            'user',
            'name',
            'account_number',
            'package',
            'processor',
            'depositing_amount',
            'kumbukumbu_no'

        }


class MpesaForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'full name', 'style': 'width: 100%; padding-bottom: 3%', "class": "textinput textInput form-control ", 'required': True}))
    account_number = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Phone number', 'style': 'width: 100%; padding-bottom: 3%',"class": "textinput textInput form-control ", 'required': True}))
    package = forms.ChoiceField(choices=pack, label="", initial='',widget=forms.RadioSelect(attrs={'style': 'width: 100%',   'type': 'radio', "type" :"text", 'required':True}), )
    depositing_amount = forms.FloatField(label='',min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'amount', "class": "textinput textInput form-control ", 'style': 'width: 100%; padding-bottom: 3%'}))
    kumbukumbu_no = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'kumbukumbu number', "class": "textinput textInput form-control ", 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = Deposits
        fields = {
            'user',
            'name',
            'account_number',
            'package',
            'processor',
            'depositing_amount',
            'kumbukumbu_no'

        }


class TransactionPerfectMoneyForm(forms.ModelForm):
    package = forms.ChoiceField(choices=pack, label="", initial='',widget=forms.RadioSelect(attrs={'style': 'width: 100%',   'type': 'radio', "type" :"text", 'required':True}), )    # user = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'email', 'style': 'width: 100%; padding-bottom: 3%;'}))
    PAYMENT_AMOUNT = forms.FloatField(label='', min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'username', 'type': 'number', 'style': 'width: 100%; padding-bottom: 3%', "name": "PAYMENT_AMOUNT", "id": "PAYMENT_AMOUNT", "class":"textinput textInput form-control ", "placeholder":"perfect money amount", 'required':True}))
    # processor = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'wallet', 'style': 'width: 100%; padding-bottom: 3%'}))
    #         PAYMENT_AMOUNT = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Depositing amount', 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = TransactionPerfectMoney
        fields = {
            "user",
            "username",
            "package",
            "processor",
            "PAYMENT_AMOUNT",

        }

    def clean(self, *args, **kwargs):
        PAYMENT_AMOUNT = self.cleaned_data.get("PAYMENT_AMOUNT")
        package = self.cleaned_data.get("package")
        if package == 'Silver':
            if PAYMENT_AMOUNT < 10 or PAYMENT_AMOUNT > 300:
                raise forms.ValidationError(" Silver package require to deposit 10usd to 300usd")

        elif package == 'Tarnish':
            if PAYMENT_AMOUNT < 5001 or PAYMENT_AMOUNT > 10000:
                raise forms.ValidationError("Tarnish package require to deposit 5001usd to 10000usd")

        elif package == 'Charoite':
            if PAYMENT_AMOUNT < 10001 or PAYMENT_AMOUNT > 50000:
                raise forms.ValidationError("Charoite package require to deposit 10001usd to 50000usd")

        elif package == 'TANZANITE':
            if PAYMENT_AMOUNT < 10 or PAYMENT_AMOUNT > 300:
                raise forms.ValidationError("Tanzanite package require to deposit 10usd to 300usd")

        elif package == 'Karat':
            if PAYMENT_AMOUNT < 5001 or PAYMENT_AMOUNT > 50000:
                raise forms.ValidationError(" Karat package require to deposit 5001usd to 50000usd")

        elif package == 'Corundum':
            if PAYMENT_AMOUNT < 10001 or PAYMENT_AMOUNT > 50000:
                raise forms.ValidationError("Corundum package require to deposit 10001usd to 50000usd")

        elif package == 'Charoite':
            if PAYMENT_AMOUNT < 10001 or PAYMENT_AMOUNT > 50000:
                raise forms.ValidationError("Charoite package require to deposit 10001usd to 50000usd")

        elif package == 'TITANIUM':
            if PAYMENT_AMOUNT < 2000 or PAYMENT_AMOUNT > 30000:
                raise forms.ValidationError("Titanium package require to deposit 2000usd to 30000usd")

        elif package == 'Niello':
            if PAYMENT_AMOUNT < 1001 or PAYMENT_AMOUNT > 10000:
                raise forms.ValidationError("Niello package require to deposit 1001usd to 10000usd")


        elif package == 'Zircorn':
            if PAYMENT_AMOUNT < 20001 or PAYMENT_AMOUNT > 50000:
                raise forms.ValidationError("Zircorn package require to deposit 20001usd to 50000usd")

        elif package == 'DIAMOND':
            if PAYMENT_AMOUNT < 70 or PAYMENT_AMOUNT > 1000:
                raise forms.ValidationError("Titanium package require to deposit 70usd to 1000usd")

        elif package == 'Quartz':
            if PAYMENT_AMOUNT < 1001 or PAYMENT_AMOUNT > 10000:
                raise forms.ValidationError("Quartz package require to deposit 10usd to 300usd")

        elif package == 'Carbon':
            if PAYMENT_AMOUNT < 10001 or PAYMENT_AMOUNT > 50000:
                raise forms.ValidationError("Carbon package require to deposit 5001usd to 50000usd")

        elif package == 'Gold':
            if PAYMENT_AMOUNT < 350 or PAYMENT_AMOUNT > 900:
                raise forms.ValidationError("Gold package require to deposit 350usd to 900usd")

        elif package == 'Platnum':
            if PAYMENT_AMOUNT < 1001 or PAYMENT_AMOUNT > 10000:
                raise forms.ValidationError("Platnum package require to deposit 1001usd to 10000usd")

        elif package == 'Pearl':
            if PAYMENT_AMOUNT < 10001 or PAYMENT_AMOUNT > 50000:
                raise forms.ValidationError("Pearl package require to deposit 2000usd to 30000usd")

        elif package == 'Copper':
            if PAYMENT_AMOUNT < 10 or PAYMENT_AMOUNT > 300:
                raise forms.ValidationError("Copper package require to deposit 10usd to 300usd")




        elif package == 'Lapls':
            if PAYMENT_AMOUNT < 5001 or  PAYMENT_AMOUNT > 10000:
                raise forms.ValidationError("Lapls package require to deposit 5001usd to 10000usd")

        elif package == 'Emerald':
            if PAYMENT_AMOUNT < 10001 or PAYMENT_AMOUNT > 50000:
                raise forms.ValidationError(" Emerald package require to deposit 5001usd to 50000usd")

        elif package == 'Iron':
            if PAYMENT_AMOUNT < 10001 or PAYMENT_AMOUNT > 50000:
                raise forms.ValidationError("Iron package require to deposit 10001usd to 50000usd")

        elif package == 'Glass':
            if PAYMENT_AMOUNT < 5001 or PAYMENT_AMOUNT > 10000:
                raise forms.ValidationError("Glass package require to deposit 5001usd to 10000usd")

        elif package == 'Moisanite':
            if PAYMENT_AMOUNT < 10001 or PAYMENT_AMOUNT > 50000:
                raise forms.ValidationError("Moisanite package require to deposit 10001usd to 50000usd")

        elif package == 'Calcite':
            if PAYMENT_AMOUNT < 2000 or PAYMENT_AMOUNT > 30000:
                raise forms.ValidationError("Calcite package require to deposit 2000usd to 30000usd")


        elif package == 'Sapphire':
            if PAYMENT_AMOUNT < 1001 or PAYMENT_AMOUNT > 10000:
                raise forms.ValidationError("Sapphire package require to deposit 1001usd to 10000usd")

        elif package == 'Ruby':
            if PAYMENT_AMOUNT < 20001 or PAYMENT_AMOUNT > 50000:
                raise forms.ValidationError("Ruby package require to deposit 20001usd to 50000usd")

        elif package == 'Amber':
            if PAYMENT_AMOUNT < 70 or PAYMENT_AMOUNT > 1000:
                raise forms.ValidationError("Amber package require to deposit 70usd to 1000usd")

        elif package == 'Agate':
            if PAYMENT_AMOUNT < 1001 or PAYMENT_AMOUNT > 10000:
                raise forms.ValidationError("Agate package require to deposit 1001usd to 10000usd")

        elif package == 'Amazonnile':
            if PAYMENT_AMOUNT < 10001 or PAYMENT_AMOUNT > 50000:
                raise forms.ValidationError("Amazonnile package require to deposit 10001usd to 50000usd")

        elif package == 'Beads':
            if PAYMENT_AMOUNT < 350 or PAYMENT_AMOUNT > 900:
                raise forms.ValidationError("Beads package require to deposit 350usd to 900usd")

        elif package == 'Beryl':
            if PAYMENT_AMOUNT < 1001 or PAYMENT_AMOUNT > 10000:
                raise forms.ValidationError("Beryl package require to deposit 1001usd to 10000usd")

        elif package == 'Azuriite':
            if PAYMENT_AMOUNT < 10001 or PAYMENT_AMOUNT > 50000:
                raise forms.ValidationError("Azuriite package require to deposit 10001usd to 50000usd")

        elif package == '':
            raise forms.ValidationError("You should choose a package")
        return super(TransactionPerfectMoneyForm, self).clean(*args, **kwargs)



class TransactionPayeerForm(forms.ModelForm):
    package = forms.ChoiceField(choices=pack, label="", initial='', widget=forms.RadioSelect(attrs={'style': 'width: 100%', 'type':'radio', 'required':True }), )
    m_amount = forms.FloatField(label='', required="", min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Payeer amount', "maxlength":"35", "name" :"m_amount", "id":"id_m_amount", "type" :"number", 'style': 'width: 100%; padding-bottom: 3%;',"class":"textinput textInput form-control "}))
    # username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'username', 'style': 'width: 100%; padding-bottom: 3%'}))
    # processor = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'wallet', 'style': 'width: 100%; padding-bottom: 3%'}))
    #         PAYMENT_AMOUNT = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Depositing amount', 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = TransactionPayeer
        fields = {
            "user",
            "username",
            "processor",
            "m_orderid",
            "package",
            "m_amount",

        }


class TransactionBitcoinForm(forms.ModelForm):
    package = forms.ChoiceField(choices=pack, label="", initial='', widget=forms.RadioSelect(attrs={'style': 'width: 100%', 'type':'radio', 'required':True }), )
    b_amount = forms.FloatField(label='', required="", min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Bitcoin amount', "maxlength":"35", "name" :"m_amount", "id":"id_m_amount", "type" :"number", 'style': 'width: 100%; padding-bottom: 3%;',"class":"textinput textInput form-control "}))
    # username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'username', 'style': 'width: 100%; padding-bottom: 3%'}))
    # processor = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'wallet', 'style': 'width: 100%; padding-bottom: 3%'}))
    #         PAYMENT_AMOUNT = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Depositing amount', 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = TransactionBitcoin
        fields = {
            "user",
            "username",
            "processor",
            "package",
            "b_amount",

        }


    def clean(self, *args, **kwargs):
        b_amount = self.cleaned_data.get("b_amount")
        package = self.cleaned_data.get("package")
        if package == 'Silver':
            if b_amount < 0.00146 or b_amount > 0.02555:
                raise forms.ValidationError(" Silver package require to deposit 10usd to 300usd")

        elif package == 'Tarnish':
            if b_amount < 0.365073 or b_amount > 0.73:
                raise forms.ValidationError("Tarnish package require to deposit 5001usd to 10000usd")

        elif package == 'Charoite':
            if b_amount < 0.730073 or b_amount > 3.65:
                raise forms.ValidationError("Charoite package require to deposit 10001usd to 50000usd")

        elif package == 'TANZANITE':
            if b_amount < 0.00073 or b_amount > 0.0219:
                raise forms.ValidationError("Tanzanite package require to deposit 10usd to 300usd")

        elif package == 'Karat':
            if b_amount < 0.365073 or b_amount > 0.73:
                raise forms.ValidationError(" Karat package require to deposit 5001usd to 50000usd")

        elif package == 'Corundum':
            if b_amount < 0.730073 or b_amount > 3.65:
                raise forms.ValidationError("Corundum package require to deposit 10001usd to 50000usd")

        elif package == 'Charoite':
            if b_amount < 10001 or b_amount > 50000:
                raise forms.ValidationError("Charoite package require to deposit 10001usd to 50000usd")

        elif package == 'TITANIUM':
            if b_amount < 0.146 or b_amount > 2.19:
                raise forms.ValidationError("Titanium package require to deposit 2000usd to 30000usd")

        elif package == 'Niello':
            if b_amount < 0.073073 or b_amount > 0.073:
                raise forms.ValidationError("Niello package require to deposit 1001usd to 10000usd")


        elif package == 'Zircorn':
            if b_amount < 1.460073 or b_amount > 3.65:
                raise forms.ValidationError("Zircorn package require to deposit 20001usd to 50000usd")

        elif package == 'DIAMOND':
            if b_amount < 0.0511 or b_amount > 0.073:
                raise forms.ValidationError("Titanium package require to deposit 70usd to 1000usd")

        elif package == 'Quartz':
            if b_amount < 0.073073 or b_amount > 0.73:
                raise forms.ValidationError("Quartz package require to deposit 10usd to 300usd")

        elif package == 'Carbon':
            if b_amount < 0.730073 or b_amount > 3.65:
                raise forms.ValidationError("Carbon package require to deposit 5001usd to 50000usd")

        elif package == 'Gold':
            if b_amount < 0.02555 or b_amount > 0.0657:
                raise forms.ValidationError("Gold package require to deposit 350usd to 900usd")

        elif package == 'Platnum':
            if b_amount < 0.073073 or b_amount > 0.73:
                raise forms.ValidationError("Platnum package require to deposit 1001usd to 10000usd")

        elif package == 'Pearl':
            if b_amount < 0.730073 or b_amount > 3.65:
                raise forms.ValidationError("Pearl package require to deposit 2000usd to 30000usd")

        elif package == 'Copper':
            if b_amount < 0.00073 or b_amount > 0.0219:
                raise forms.ValidationError("Copper package require to deposit 10usd to 300usd")




        elif package == 'Lapls':
            if b_amount < 3.650073 or b_amount > 0.73:
                raise forms.ValidationError("Lapls package require to deposit 5001usd to 10000usd")

        elif package == 'Emerald':
            if b_amount < 0.730073 or b_amount > 3.65:
                raise forms.ValidationError(" Emerald package require to deposit 5001usd to 50000usd")

        elif package == 'Iron':
            if b_amount < 0.00073 or b_amount > 0.0219:
                raise forms.ValidationError("Iron package require to deposit 10001usd to 50000usd")

        elif package == 'Glass':
            if b_amount < 0.365073 or b_amount > 0.73:
                raise forms.ValidationError("Glass package require to deposit 5001usd to 10000usd")

        elif package == 'Moisanite':
            if b_amount < 0.730073 or b_amount > 3.65:
                raise forms.ValidationError("Moisanite package require to deposit 10001usd to 50000usd")

        elif package == 'Calcite':
            if b_amount < 0.146 or b_amount > 2.19:
                raise forms.ValidationError("Calcite package require to deposit 2000usd to 30000usd")


        elif package == 'Sapphire':
            if b_amount < 0.073073 or b_amount > 0.73:
                raise forms.ValidationError("Sapphire package require to deposit 1001usd to 10000usd")

        elif package == 'Ruby':
            if b_amount < 1.460073 or b_amount > 3.65:
                raise forms.ValidationError("Ruby package require to deposit 20001usd to 50000usd")

        elif package == 'Amber':
            if b_amount < 0.00511 or b_amount > 0.073:
                raise forms.ValidationError("Amber package require to deposit 70usd to 1000usd")

        elif package == 'Agate':
            if b_amount < 0.073073 or b_amount > 0.73:
                raise forms.ValidationError("Agate package require to deposit 1001usd to 10000usd")

        elif package == 'Amazonnile':
            if b_amount < 0.730073 or b_amount > 3.65:
                raise forms.ValidationError("Amazonnile package require to deposit 10001usd to 50000usd")

        elif package == 'Beads':
            if b_amount < 0.02555 or b_amount > 0.0657:
                raise forms.ValidationError("Beads package require to deposit 350usd to 900usd")

        elif package == 'Beryl':
            if b_amount < 0.073073 or b_amount > 0.73:
                raise forms.ValidationError("Beryl package require to deposit 1001usd to 10000usd")

        elif package == 'Azuriite':
            if b_amount < 0.730073 or b_amount > 3.65:
                raise forms.ValidationError("Azuriite package require to deposit 10001usd to 50000usd")

        elif package == '':
            raise forms.ValidationError("You should choose a package")
        return super(TransactionBitcoinForm, self).clean(*args, **kwargs)


class BitcoinRedepositForm(forms.ModelForm):
    package = forms.ChoiceField(choices=pack, label="", initial='', widget=forms.RadioSelect(attrs={'style': 'width: 100%', 'type':'radio', 'required':True }), )
    b_amount = forms.FloatField(label='', required="", min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Bitcoin amount', "maxlength":"35", "name" :"m_amount", "id":"id_m_amount", "type" :"number", 'style': 'width: 100%; padding-bottom: 3%;',"class":"textinput textInput form-control "}))
    # username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'username', 'style': 'width: 100%; padding-bottom: 3%'}))
    # processor = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'wallet', 'style': 'width: 100%; padding-bottom: 3%'}))
    #         PAYMENT_AMOUNT = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Depositing amount', 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = BitcoinRedepositModels
        fields = {
            "user",
            "username",
            "processor",
            "package",
            "b_amount",

        }


    def clean(self, *args, **kwargs):
        b_amount = self.cleaned_data.get("b_amount")
        package = self.cleaned_data.get("package")
        if package == 'Silver':
            if b_amount < 0.00146 or b_amount > 0.02555:
                raise forms.ValidationError(" Silver package require to deposit 10usd to 300usd")

        elif package == 'Tarnish':
            if b_amount < 0.365073 or b_amount > 0.73:
                raise forms.ValidationError("Tarnish package require to deposit 5001usd to 10000usd")

        elif package == 'Charoite':
            if b_amount < 0.730073 or b_amount > 3.65:
                raise forms.ValidationError("Charoite package require to deposit 10001usd to 50000usd")

        elif package == 'TANZANITE':
            if b_amount < 0.00073 or b_amount > 0.0219:
                raise forms.ValidationError("Tanzanite package require to deposit 10usd to 300usd")

        elif package == 'Karat':
            if b_amount < 0.365073 or b_amount > 0.73:
                raise forms.ValidationError(" Karat package require to deposit 5001usd to 50000usd")

        elif package == 'Corundum':
            if b_amount < 0.730073 or b_amount >  3.65:
                raise forms.ValidationError("Corundum package require to deposit 10001usd to 50000usd")

        elif package == 'Charoite':
            if b_amount < 10001 or b_amount > 50000:
                raise forms.ValidationError("Charoite package require to deposit 10001usd to 50000usd")

        elif package == 'TITANIUM':
            if b_amount < 0.146 or b_amount > 2.19:
                raise forms.ValidationError("Titanium package require to deposit 2000usd to 30000usd")

        elif package == 'Niello':
            if b_amount < 0.073073 or b_amount >  0.073:
                raise forms.ValidationError("Niello package require to deposit 1001usd to 10000usd")


        elif package == 'Zircorn':
            if b_amount < 1.460073 or b_amount > 3.65:
                raise forms.ValidationError("Zircorn package require to deposit 20001usd to 50000usd")

        elif package == 'DIAMOND':
            if b_amount < 0.0511 or b_amount > 0.073:
                raise forms.ValidationError("Titanium package require to deposit 70usd to 1000usd")

        elif package == 'Quartz':
            if b_amount < 0.073073 or b_amount > 0.73:
                raise forms.ValidationError("Quartz package require to deposit 10usd to 300usd")

        elif package == 'Carbon':
            if b_amount < 0.730073 or b_amount >  3.65:
                raise forms.ValidationError("Carbon package require to deposit 5001usd to 50000usd")

        elif package == 'Gold':
            if b_amount < 0.02555 or b_amount > 0.0657:
                raise forms.ValidationError("Gold package require to deposit 350usd to 900usd")

        elif package == 'Platnum':
            if b_amount < 0.073073 or b_amount > 0.73:
                raise forms.ValidationError("Platnum package require to deposit 1001usd to 10000usd")

        elif package == 'Pearl':
            if b_amount < 0.730073  or b_amount > 3.65:
                raise forms.ValidationError("Pearl package require to deposit 2000usd to 30000usd")

        elif package == 'Copper':
            if b_amount < 0.00073 or b_amount > 0.0219:
                raise forms.ValidationError("Copper package require to deposit 10usd to 300usd")




        elif package == 'Lapls':
            if b_amount < 3.650073 or b_amount > 0.73:
                raise forms.ValidationError("Lapls package require to deposit 5001usd to 10000usd")

        elif package == 'Emerald':
            if b_amount < 0.730073 or b_amount > 3.65:
                raise forms.ValidationError(" Emerald package require to deposit 5001usd to 50000usd")

        elif package == 'Iron':
            if b_amount < 0.00073 or b_amount > 0.0219:
                raise forms.ValidationError("Iron package require to deposit 10001usd to 50000usd")

        elif package == 'Glass':
            if b_amount < 0.365073 or b_amount > 0.73:
                raise forms.ValidationError("Glass package require to deposit 5001usd to 10000usd")

        elif package == 'Moisanite':
            if b_amount < 0.730073 or b_amount > 3.65:
                raise forms.ValidationError("Moisanite package require to deposit 10001usd to 50000usd")

        elif package == 'Calcite':
            if b_amount < 0.146 or b_amount > 2.19:
                raise forms.ValidationError("Calcite package require to deposit 2000usd to 30000usd")


        elif package == 'Sapphire':
            if b_amount < 0.073073 or b_amount > 0.73:
                raise forms.ValidationError("Sapphire package require to deposit 1001usd to 10000usd")

        elif package == 'Ruby':
            if b_amount < 1.460073 or b_amount > 3.65:
                raise forms.ValidationError("Ruby package require to deposit 20001usd to 50000usd")

        elif package == 'Amber':
            if b_amount < 0.00511 or b_amount > 0.073:
                raise forms.ValidationError("Amber package require to deposit 70usd to 1000usd")

        elif package == 'Agate':
            if b_amount < 0.073073 or b_amount > 0.73:
                raise forms.ValidationError("Agate package require to deposit 1001usd to 10000usd")

        elif package == 'Amazonnile':
            if b_amount < 0.730073 or b_amount > 3.65:
                raise forms.ValidationError("Amazonnile package require to deposit 10001usd to 50000usd")

        elif package == 'Beads':
            if b_amount < 0.02555 or b_amount > 0.0657:
                raise forms.ValidationError("Beads package require to deposit 350usd to 900usd")

        elif package == 'Beryl':
            if b_amount < 0.073073 or b_amount > 0.73:
                raise forms.ValidationError("Beryl package require to deposit 1001usd to 10000usd")

        elif package == 'Azuriite':
            if b_amount < 0.730073 or b_amount > 3.65:
                raise forms.ValidationError("Azuriite package require to deposit 10001usd to 50000usd")

        elif package == '':
            raise forms.ValidationError("You should choose a package")
        return super(BitcoinRedepositForm, self).clean(*args, **kwargs)





class WithdrawprocessorForm(forms.ModelForm):
    # package= forms.ChoiceField(choices=pack, label="", initial='', widget=forms.RadioSelect(attrs={'style': 'width: 100%', 'type':'radio', 'required':True }), )
    m_amount = forms.FloatField(label='', required="",min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Payeer amount', "maxlength":"35", "name" :"m_amount", "id":"id_m_amount", "type" :"number", 'style': 'width: 100%; padding-bottom: 3%;',"class":"textinput textInput form-control "}))
    # username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'username', 'style': 'width: 100%; padding-bottom: 3%'}))
    # processor = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'wallet', 'style': 'width: 100%; padding-bottom: 3%'}))
    #         PAYMENT_AMOUNT = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Depositing amount', 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = Withdrawprocessor
        fields = {
            "user",
            "full_name",
            "m_amount",
            "email",
            "account_number",
            "processor",
            "balance",
            "processor_acc_number",
            "m_amount",
            "status",

        }



class BitcoinWithdrawForm(forms.ModelForm):
    # package= forms.ChoiceField(choices=pack, label="", initial='', widget=forms.RadioSelect(attrs={'style': 'width: 100%', 'type':'radio', 'required':True }), )
    b_amount = forms.FloatField(label='', required="",min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Bitcoin amount', "maxlength":"35", "name" :"m_amount", "id":"id_m_amount", "type" :"number", 'style': 'width: 100%; padding-bottom: 3%;',"class":"textinput textInput form-control "}))
    # username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'username', 'style': 'width: 100%; padding-bottom: 3%'}))
    # processor = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'wallet', 'style': 'width: 100%; padding-bottom: 3%'}))
    #         PAYMENT_AMOUNT = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Depositing amount', 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = BitcoinWithdrawModel
        fields = {
            "user",
            "full_name",
            "b_amount",
            "email",
            "account_number",
            "processor",
            "balance",
            "processor_acc_number",
            "status",

        }



class BalanceTransactionForm(forms.ModelForm):
    currency_transfered = forms.ChoiceField(choices=ACCOUNT_TYPE_CHOICES, label="", initial='', widget=forms.RadioSelect(attrs={'style': 'width: 100%', 'type':'radio', 'required':True }), )
    # user = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'email', 'style': 'width: 100%; padding-bottom: 3%;'}))
    username_receiver = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Account number of receiver', 'style': 'width: 100%; padding-bottom: 3%;', "class":"textinput textInput form-control "}))
    amount_transfered = forms.FloatField(label='', min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Amount to be transfered', 'style': 'width: 100%; padding-bottom: 3%;', 'type':'number', "class":"textinput textInput form-control "}))
    security_code = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'security code', 'style': 'width: 100%; padding-bottom: 3%;', "class":"textinput textInput form-control "}))
    #         PAYMENT_AMOUNT = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Depositing amount', 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = BalanceTransaction
        fields = {
            "user",
            "currency_transfered",
            "from_account_no",
            "username_receiver",
            "amount_transfered",
            "security_code"
        }



class BalanceRedepositForm(forms.ModelForm):
    # package= forms.ChoiceField(choices=pack, label="", initial='', widget=forms.RadioSelect(attrs={'style': 'width: 100%', 'type':'radio', 'required':True }), )
    # user = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'email', 'style': 'width: 100%; padding-bottom: 3%;'}))
    amount_transfered = forms.FloatField(label='', min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Deposit', 'style': 'width: 100%; padding-bottom: 3%;', 'type':'number', "class":"textinput textInput form-control "}))
    # processor = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'wallet', 'style': 'width: 100%; padding-bottom: 3%'}))
    #         PAYMENT_AMOUNT = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Depositing amount', 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = BalanceRedeposit
        fields = {
            "user",
            "username",
            "processor",
            "package",
            "Xumpesa_account",
            "amount_transfered",
        }

    def clean(self, *args, **kwargs):
        amount_transfered = self.cleaned_data.get("amount_transfered")
        package = self.cleaned_data.get("package")
        if package == 'Silver':
            if amount_transfered < 10 or amount_transfered > 300:
                raise forms.ValidationError(" Silver package require to deposit 10usd to 300usd")

        elif package == 'Tarnish':
            if amount_transfered < 5001 or amount_transfered > 10000:
                raise forms.ValidationError("Tarnish package require to deposit 5001usd to 10000usd")

        elif package == 'Charoite':
            if amount_transfered < 10001 or amount_transfered > 50000:
                raise forms.ValidationError("Charoite package require to deposit 10001usd to 50000usd")

        elif package == 'TANZANITE':
            if amount_transfered < 10 or amount_transfered > 300:
                raise forms.ValidationError("Tanzanite package require to deposit 10usd to 300usd")

        elif package == 'Karat':
            if amount_transfered < 5001 or amount_transfered > 50000:
                raise forms.ValidationError(" Karat package require to deposit 5001usd to 50000usd")

        elif package == 'Corundum':
            if amount_transfered < 10001 or amount_transfered > 50000:
                raise forms.ValidationError("Corundum package require to deposit 10001usd to 50000usd")

        elif package == 'Charoite':
            if amount_transfered < 10001 or amount_transfered > 50000:
                raise forms.ValidationError("Charoite package require to deposit 10001usd to 50000usd")

        elif package == 'TITANIUM':
            if amount_transfered < 2000 or amount_transfered > 30000:
                raise forms.ValidationError("Titanium package require to deposit 2000usd to 30000usd")

        elif package == 'Niello':
            if amount_transfered < 1001 or amount_transfered > 10000:
                raise forms.ValidationError("Niello package require to deposit 1001usd to 10000usd")


        elif package == 'Zircorn':
            if amount_transfered < 20001 or amount_transfered > 50000:
                raise forms.ValidationError("Zircorn package require to deposit 20001usd to 50000usd")

        elif package == 'DIAMOND':
            if amount_transfered < 70 or amount_transfered > 1000:
                raise forms.ValidationError("Titanium package require to deposit 70usd to 1000usd")

        elif package == 'Quartz':
            if amount_transfered < 1001 or amount_transfered > 10000:
                raise forms.ValidationError("Quartz package require to deposit 10usd to 300usd")

        elif package == 'Carbon':
            if amount_transfered < 10001 or amount_transfered > 50000:
                raise forms.ValidationError("Carbon package require to deposit 5001usd to 50000usd")

        elif package == 'Gold':
            if amount_transfered < 350 or amount_transfered > 900:
                raise forms.ValidationError("Gold package require to deposit 350usd to 900usd")

        elif package == 'Platnum':
            if amount_transfered < 1001 or amount_transfered > 10000:
                raise forms.ValidationError("Platnum package require to deposit 1001usd to 10000usd")

        elif package == 'Pearl':
            if amount_transfered < 10001 or amount_transfered > 50000:
                raise forms.ValidationError("Pearl package require to deposit 2000usd to 30000usd")

        elif package == 'Copper':
            if amount_transfered < 10 or amount_transfered > 300:
                raise forms.ValidationError("Copper package require to deposit 10usd to 300usd")




        elif package == 'Lapls':
            if amount_transfered < 5001 or amount_transfered > 10000:
                raise forms.ValidationError("Lapls package require to deposit 5001usd to 10000usd")

        elif package == 'Emerald':
            if amount_transfered < 10001 or amount_transfered > 50000:
                raise forms.ValidationError(" Emerald package require to deposit 5001usd to 50000usd")

        elif package == 'Iron':
            if amount_transfered < 10001 or amount_transfered > 50000:
                raise forms.ValidationError("Iron package require to deposit 10001usd to 50000usd")

        elif package == 'Glass':
            if amount_transfered < 5001 or amount_transfered > 10000:
                raise forms.ValidationError("Glass package require to deposit 5001usd to 10000usd")

        elif package == 'Moisanite':
            if amount_transfered < 10001 or amount_transfered > 50000:
                raise forms.ValidationError("Moisanite package require to deposit 10001usd to 50000usd")

        elif package == 'Calcite':
            if amount_transfered < 2000 or amount_transfered > 30000:
                raise forms.ValidationError("Calcite package require to deposit 2000usd to 30000usd")


        elif package == 'Sapphire':
            if amount_transfered < 1001 or amount_transfered > 10000:
                raise forms.ValidationError("Sapphire package require to deposit 1001usd to 10000usd")

        elif package == 'Ruby':
            if amount_transfered < 20001 or amount_transfered > 50000:
                raise forms.ValidationError("Ruby package require to deposit 20001usd to 50000usd")

        elif package == 'Amber':
            if amount_transfered < 70 or amount_transfered > 1000:
                raise forms.ValidationError("Amber package require to deposit 70usd to 1000usd")

        elif package == 'Agate':
            if amount_transfered < 1001 or amount_transfered > 10000:
                raise forms.ValidationError("Agate package require to deposit 1001usd to 10000usd")

        elif package == 'Amazonnile':
            if amount_transfered < 10001 or amount_transfered > 50000:
                raise forms.ValidationError("Amazonnile package require to deposit 10001usd to 50000usd")

        elif package == 'Beads':
            if amount_transfered < 350 or amount_transfered > 900:
                raise forms.ValidationError("Beads package require to deposit 350usd to 900usd")

        elif package == 'Beryl':
            if amount_transfered < 1001 or amount_transfered > 10000:
                raise forms.ValidationError("Beryl package require to deposit 1001usd to 10000usd")

        elif package == 'Azuriite':
            if amount_transfered < 10001 or amount_transfered > 50000:
                raise forms.ValidationError("Azuriite package require to deposit 10001usd to 50000usd")

        elif package == '':
            raise forms.ValidationError("You should choose a package")
        return super(BalanceRedepositForm, self).clean(*args, **kwargs)



class OKpayDeoisitForm(forms.ModelForm):
    # package= forms.ChoiceField(choices=pack, label="", initial='', widget=forms.RadioSelect(attrs={'style': 'width: 100%', 'type':'radio', 'required':True }), )
    # user = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'email', 'style': 'width: 100%; padding-bottom: 3%;'}))
    o_amount = forms.FloatField(label='', min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Deposit', 'style': 'width: 100%; padding-bottom: 3%;', 'type':'number', "class":"textinput textInput form-control "}))
    # processor = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'wallet', 'style': 'width: 100%; padding-bottom: 3%'}))
    #         PAYMENT_AMOUNT = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Depositing amount', 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = OKpayDeoisitModel
        fields = {
            "user",
            "username",
            "processor",
            "package",
            "o_amount",
        }

    def clean(self, *args, **kwargs):
        o_amount = int(self.cleaned_data.get("o_amount"))
        package = self.cleaned_data.get("package")
        if package == 'Silver':
            if o_amount < 10 or o_amount > 300:
                raise forms.ValidationError(" Silver package require to deposit 10usd to 300usd")

        elif package == 'Tarnish':
            if o_amount < 5001 or o_amount > 10000:
                raise forms.ValidationError("Tarnish package require to deposit 5001usd to 10000usd")

        elif package == 'Charoite':
            if o_amount < 10001 or o_amount > 50000:
                raise forms.ValidationError("Charoite package require to deposit 10001usd to 50000usd")

        elif package == 'TANZANITE':
            if o_amount < 10 or o_amount > 300:
                raise forms.ValidationError("Tanzanite package require to deposit 10usd to 300usd")

        elif package == 'Karat':
            if o_amount < 5001 or o_amount > 50000:
                raise forms.ValidationError(" Karat package require to deposit 5001usd to 50000usd")

        elif package == 'Corundum':
            if o_amount < 10001 or o_amount > 50000:
                raise forms.ValidationError("Corundum package require to deposit 10001usd to 50000usd")

        elif package == 'Charoite':
            if o_amount < 10001 or o_amount > 50000:
                raise forms.ValidationError("Charoite package require to deposit 10001usd to 50000usd")

        elif package == 'TITANIUM':
            if o_amount < 2000 or o_amount > 30000:
                raise forms.ValidationError("Titanium package require to deposit 2000usd to 30000usd")

        elif package == 'Niello':
            if o_amount < 1001 or o_amount > 10000:
                raise forms.ValidationError("Niello package require to deposit 1001usd to 10000usd")


        elif package == 'Zircorn':
            if o_amount < 20001 or o_amount > 50000:
                raise forms.ValidationError("Zircorn package require to deposit 20001usd to 50000usd")

        elif package == 'DIAMOND':
            if o_amount < 70 or o_amount > 1000:
                raise forms.ValidationError("Titanium package require to deposit 70usd to 1000usd")

        elif package == 'Quartz':
            if o_amount < 1001 or o_amount > 10000:
                raise forms.ValidationError("Quartz package require to deposit 10usd to 300usd")

        elif package == 'Carbon':
            if o_amount < 10001 or o_amount > 50000:
                raise forms.ValidationError("Carbon package require to deposit 5001usd to 50000usd")

        elif package == 'Gold':
            if o_amount < 350 or o_amount > 900:
                raise forms.ValidationError("Gold package require to deposit 350usd to 900usd")

        elif package == 'Platnum':
            if o_amount < 1001 or o_amount > 10000:
                raise forms.ValidationError("Platnum package require to deposit 1001usd to 10000usd")

        elif package == 'Pearl':
            if o_amount < 10001 or o_amount > 50000:
                raise forms.ValidationError("Pearl package require to deposit 2000usd to 30000usd")

        elif package == 'Copper':
            if o_amount < 10 or o_amount > 300:
                raise forms.ValidationError("Copper package require to deposit 10usd to 300usd")




        elif package == 'Lapls':
            if o_amount < 5001 or o_amount > 10000:
                raise forms.ValidationError("Lapls package require to deposit 5001usd to 10000usd")

        elif package == 'Emerald':
            if o_amount < 10001 or o_amount > 50000:
                raise forms.ValidationError(" Emerald package require to deposit 5001usd to 50000usd")

        elif package == 'Iron':
            if o_amount < 10001 or o_amount > 50000:
                raise forms.ValidationError("Iron package require to deposit 10001usd to 50000usd")

        elif package == 'Glass':
            if o_amount < 5001 or o_amount > 10000:
                raise forms.ValidationError("Glass package require to deposit 5001usd to 10000usd")

        elif package == 'Moisanite':
            if o_amount < 10001 or o_amount > 50000:
                raise forms.ValidationError("Moisanite package require to deposit 10001usd to 50000usd")

        elif package == 'Calcite':
            if o_amount < 2000 or o_amount > 30000:
                raise forms.ValidationError("Calcite package require to deposit 2000usd to 30000usd")


        elif package == 'Sapphire':
            if o_amount < 1001 or o_amount > 10000:
                raise forms.ValidationError("Sapphire package require to deposit 1001usd to 10000usd")

        elif package == 'Ruby':
            if o_amount < 20001 or o_amount > 50000:
                raise forms.ValidationError("Ruby package require to deposit 20001usd to 50000usd")

        elif package == 'Amber':
            if o_amount < 70 or o_amount > 1000:
                raise forms.ValidationError("Amber package require to deposit 70usd to 1000usd")

        elif package == 'Agate':
            if o_amount < 1001 or o_amount > 10000:
                raise forms.ValidationError("Agate package require to deposit 1001usd to 10000usd")

        elif package == 'Amazonnile':
            if o_amount < 10001 or o_amount > 50000:
                raise forms.ValidationError("Amazonnile package require to deposit 10001usd to 50000usd")

        elif package == 'Beads':
            if o_amount < 350 or o_amount > 900:
                raise forms.ValidationError("Beads package require to deposit 350usd to 900usd")

        elif package == 'Beryl':
            if o_amount < 1001 or o_amount > 10000:
                raise forms.ValidationError("Beryl package require to deposit 1001usd to 10000usd")

        elif package == 'Azuriite':
            if o_amount < 10001 or o_amount > 50000:
                raise forms.ValidationError("Azuriite package require to deposit 10001usd to 50000usd")

        elif package == '':
            raise forms.ValidationError("You should choose a package")
        return super(OKpayDeoisitForm, self).clean(*args, **kwargs)




class AdvCashDepositForm(forms.ModelForm):
    # package= forms.ChoiceField(choices=pack, label="", initial='', widget=forms.RadioSelect(attrs={'style': 'width: 100%', 'type':'radio', 'required':True }), )
    # user = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'email', 'style': 'width: 100%; padding-bottom: 3%;'}))
    a_amount = forms.FloatField(label='', min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Deposit', 'style': 'width: 100%; padding-bottom: 3%;', 'type':'number', "class":"textinput textInput form-control "}))
    # processor = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'wallet', 'style': 'width: 100%; padding-bottom: 3%'}))
    #         PAYMENT_AMOUNT = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Depositing amount', 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = AdvCashDeposit
        fields = {
            "user",
            "username",
            "processor",
            "package",
            "a_amount",
        }

    def clean(self, *args, **kwargs):
        a_amount = int(self.cleaned_data.get("a_amount"))
        package = self.cleaned_data.get("package")
        if package == 'Silver':
            if a_amount < 10 or a_amount > 300:
                raise forms.ValidationError(" Silver package require to deposit 10usd to 300usd")

        elif package == 'Tarnish':
            if a_amount < 5001 or a_amount > 10000:
                raise forms.ValidationError("Tarnish package require to deposit 5001usd to 10000usd")

        elif package == 'Charoite':
            if a_amount < 10001 or a_amount > 50000:
                raise forms.ValidationError("Charoite package require to deposit 10001usd to 50000usd")

        elif package == 'TANZANITE':
            if a_amount < 10 or a_amount > 300:
                raise forms.ValidationError("Tanzanite package require to deposit 10usd to 300usd")

        elif package == 'Karat':
            if a_amount < 5001 or a_amount > 50000:
                raise forms.ValidationError(" Karat package require to deposit 5001usd to 50000usd")

        elif package == 'Corundum':
            if a_amount < 10001 or a_amount > 50000:
                raise forms.ValidationError("Corundum package require to deposit 10001usd to 50000usd")

        elif package == 'Charoite':
            if a_amount < 10001 or a_amount > 50000:
                raise forms.ValidationError("Charoite package require to deposit 10001usd to 50000usd")

        elif package == 'TITANIUM':
            if a_amount < 2000 or a_amount > 30000:
                raise forms.ValidationError("Titanium package require to deposit 2000usd to 30000usd")

        elif package == 'Niello':
            if a_amount < 1001 or a_amount > 10000:
                raise forms.ValidationError("Niello package require to deposit 1001usd to 10000usd")


        elif package == 'Zircorn':
            if a_amount < 20001 or a_amount > 50000:
                raise forms.ValidationError("Zircorn package require to deposit 20001usd to 50000usd")

        elif package == 'DIAMOND':
            if a_amount < 70 or a_amount > 1000:
                raise forms.ValidationError("Titanium package require to deposit 70usd to 1000usd")

        elif package == 'Quartz':
            if a_amount < 1001 or a_amount > 10000:
                raise forms.ValidationError("Quartz package require to deposit 10usd to 300usd")

        elif package == 'Carbon':
            if o_amount < 10001 or o_amount > 50000:
                raise forms.ValidationError("Carbon package require to deposit 5001usd to 50000usd")

        elif package == 'Gold':
            if a_amount < 350 or a_amount > 900:
                raise forms.ValidationError("Gold package require to deposit 350usd to 900usd")

        elif package == 'Platnum':
            if a_amount < 1001 or a_amount > 10000:
                raise forms.ValidationError("Platnum package require to deposit 1001usd to 10000usd")

        elif package == 'Pearl':
            if a_amount < 10001 or a_amount > 50000:
                raise forms.ValidationError("Pearl package require to deposit 2000usd to 30000usd")

        elif package == 'Copper':
            if a_amount < 10 or a_amount > 300:
                raise forms.ValidationError("Copper package require to deposit 10usd to 300usd")




        elif package == 'Lapls':
            if a_amount < 5001 or a_amount > 10000:
                raise forms.ValidationError("Lapls package require to deposit 5001usd to 10000usd")

        elif package == 'Emerald':
            if a_amount < 10001 or a_amount > 50000:
                raise forms.ValidationError(" Emerald package require to deposit 5001usd to 50000usd")

        elif package == 'Iron':
            if a_amount < 10001 or a_amount > 50000:
                raise forms.ValidationError("Iron package require to deposit 10001usd to 50000usd")

        elif package == 'Glass':
            if a_amount < 5001 or a_amount > 10000:
                raise forms.ValidationError("Glass package require to deposit 5001usd to 10000usd")

        elif package == 'Moisanite':
            if a_amount < 10001 or a_amount > 50000:
                raise forms.ValidationError("Moisanite package require to deposit 10001usd to 50000usd")

        elif package == 'Calcite':
            if a_amount < 2000 or a_amount > 30000:
                raise forms.ValidationError("Calcite package require to deposit 2000usd to 30000usd")


        elif package == 'Sapphire':
            if o_amount < 1001 or o_amount > 10000:
                raise forms.ValidationError("Sapphire package require to deposit 1001usd to 10000usd")

        elif package == 'Ruby':
            if a_amount < 20001 or a_amount > 50000:
                raise forms.ValidationError("Ruby package require to deposit 20001usd to 50000usd")

        elif package == 'Amber':
            if a_amount < 70 or a_amount > 1000:
                raise forms.ValidationError("Amber package require to deposit 70usd to 1000usd")

        elif package == 'Agate':
            if o_amount < 1001 or o_amount > 10000:
                raise forms.ValidationError("Agate package require to deposit 1001usd to 10000usd")

        elif package == 'Amazonnile':
            if a_amount < 10001 or a_amount > 50000:
                raise forms.ValidationError("Amazonnile package require to deposit 10001usd to 50000usd")

        elif package == 'Beads':
            if a_amount < 350 or a_amount > 900:
                raise forms.ValidationError("Beads package require to deposit 350usd to 900usd")

        elif package == 'Beryl':
            if a_amount < 1001 or a_amount > 10000:
                raise forms.ValidationError("Beryl package require to deposit 1001usd to 10000usd")

        elif package == 'Azuriite':
            if o_amount < 10001 or o_amount > 50000:
                raise forms.ValidationError("Azuriite package require to deposit 10001usd to 50000usd")

        elif package == '':
            raise forms.ValidationError("You should choose a package")
        return super(AdvCashDepositForm, self).clean(*args, **kwargs)


class VerificationForm(forms.ModelForm):
    # package= forms.ChoiceField(choices=pack, label="", initial='', widget=forms.RadioSelect(attrs={'style': 'width: 100%', 'type':'radio', 'required':True }), )
    # user = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'email', 'style': 'width: 100%; padding-bottom: 3%;'}))
    # user = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Deposit', 'style': 'width: 100%; padding-bottom: 3%;', "class":"textinput textInput form-control "}))
    # depositing_amount = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'wallet', 'style': 'width: 100%; padding-bottom: 3%'}))
    # kumbukumbu_no = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Depositing amount', 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = DepositsVerified
        fields = {
            "user",
            "username",
            "processor",
            "amount_deposited",
            "startdate",
            "enddate",
            "package",
            "sign",
            "hashid",
            "expected_income",
            "shortcode",

        }













class TigopesaWithdrawForm(forms.ModelForm):
    # name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'name', 'style': 'width: 100%; padding-bottom: 3%', "class": "textinput textInput form-control ",'required': True}))
    # account_number = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'account number', 'style': 'width: 100%; padding-bottom: 3%',"class": "textinput textInput form-control ", 'required': True}))
    withdrawing_amount = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'withdrawing amount', "class": "textinput textInput form-control ", 'style': 'width: 100%; padding-bottom: 3%'}))
    # balance = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'kumbukumbu number', "class": "textinput textInput form-control ", 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = Withdraw
        fields = {
            'user',
            'full_name',
            'processor',
            'tigopesa_number',
            'account_number',
            'withdrawing_amount',
            'balance'

        }


class MpesaWithdrawForm(forms.ModelForm):
    # name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'name', 'style': 'width: 100%; padding-bottom: 3%', "class": "textinput textInput form-control ",'required': True}))
    # account_number = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'account number', 'style': 'width: 100%; padding-bottom: 3%',"class": "textinput textInput form-control ", 'required': True}))
    withdrawing_amount = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'withdrawing amount', "class": "textinput textInput form-control ", 'style': 'width: 100%; padding-bottom: 3%'}))
    # balance = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'kumbukumbu number', "class": "textinput textInput form-control ", 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = Withdraw
        fields = {
            'user',
            'full_name',
            'processor',
            'tigopesa_number',
            'account_number',
            'withdrawing_amount',
            'balance'

        }

class AirtelWithdrawForm(forms.ModelForm):
    # name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'name', 'style': 'width: 100%; padding-bottom: 3%', "class": "textinput textInput form-control ",'required': True}))
    # account_number = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'account number', 'style': 'width: 100%; padding-bottom: 3%',"class": "textinput textInput form-control ", 'required': True}))
    withdrawing_amount = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'withdrawing amount', "class": "textinput textInput form-control ", 'style': 'width: 100%; padding-bottom: 3%'}))
    # balance = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'kumbukumbu number', "class": "textinput textInput form-control ", 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = Withdraw
        fields = {
            'user',
            'full_name',
            'processor',
            'tigopesa_number',
            'account_number',
            'withdrawing_amount',
            'balance'

        }






class bitcoinBalanceDepositForm(forms.ModelForm):
    b_amount = forms.FloatField(label='', required="", min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Bitcoin amount', "maxlength":"35", "name" :"m_amount", "id":"id_m_amount", "type" :"number", 'style': 'width: 100%; padding-bottom: 3%;',"class":"textinput textInput form-control "}))
    # username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'username', 'style': 'width: 100%; padding-bottom: 3%'}))
    # processor = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'wallet', 'style': 'width: 100%; padding-bottom: 3%'}))
    #         PAYMENT_AMOUNT = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Depositing amount', 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = bitcoinBalanceDeposit
        fields = {
            "user",
            "username",
            "processor",
            "b_amount",

        }




class AdvCashBalanceDepositForm(forms.ModelForm):
    a_amount = forms.FloatField(label='', required="", min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'AdvCash amount', "maxlength":"35", "name" :"m_amount", "id":"id_m_amount", "type" :"number", 'style': 'width: 100%; padding-bottom: 3%;',"class":"textinput textInput form-control "}))
    # username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'username', 'style': 'width: 100%; padding-bottom: 3%'}))
    # processor = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'wallet', 'style': 'width: 100%; padding-bottom: 3%'}))
    #         PAYMENT_AMOUNT = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Depositing amount', 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = AdvCashBalanceDeposit
        fields = {
            "user",
            "username",
            "processor",
            "a_amount",

        }


class OKPayBalanceDepositForm(forms.ModelForm):
    o_amount = forms.FloatField(label='', required="", min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Ok-pay amount', "maxlength":"35", "name" :"m_amount", "id":"id_m_amount", "type" :"number", 'style': 'width: 100%; padding-bottom: 3%;',"class":"textinput textInput form-control "}))
    # username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'username', 'style': 'width: 100%; padding-bottom: 3%'}))
    # processor = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'wallet', 'style': 'width: 100%; padding-bottom: 3%'}))
    #         PAYMENT_AMOUNT = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Depositing amount', 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = OKPayBalanceDeposit
        fields = {
            "user",
            "username",
            "processor",
            "o_amount",

        }

class PayeerBalanceDepositForm(forms.ModelForm):
    m_amount = forms.FloatField(label='', required="", min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Payeer amount', "maxlength":"35", "name" :"m_amount", "id":"id_m_amount", "type" :"number", 'style': 'width: 100%; padding-bottom: 3%;',"class":"textinput textInput form-control "}))
    # username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'username', 'style': 'width: 100%; padding-bottom: 3%'}))
    # processor = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'wallet', 'style': 'width: 100%; padding-bottom: 3%'}))
    #         PAYMENT_AMOUNT = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Depositing amount', 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = PayeerBalanceDeposit
        fields = {
            "user",
            "username",
            "processor",
            "m_amount",

        }



class PerfectMoneyrBalanceDepositForm(forms.ModelForm):
    p_amount = forms.FloatField(label='', required="", min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Perfect money amount', "maxlength":"35", "name" :"m_amount", "id":"id_m_amount", "type" :"number", 'style': 'width: 100%; padding-bottom: 3%;',"class":"textinput textInput form-control "}))
    # username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'username', 'style': 'width: 100%; padding-bottom: 3%'}))
    # processor = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'wallet', 'style': 'width: 100%; padding-bottom: 3%'}))
    #         PAYMENT_AMOUNT = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Depositing amount', 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = PerfectMoneyrBalanceDeposit
        fields = {
            "user",
            "username",
            "processor",
            "p_amount",

        }
