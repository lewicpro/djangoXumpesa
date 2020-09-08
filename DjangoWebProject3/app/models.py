from django.db import models
import time, datetime
from django.core.mail import send_mail
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.core.validators import MinValueValidator
import string
from django.utils import timezone
from django.conf import settings
import schedule
import random, string
from django.db.models.signals import post_save
from django.urls import reverse
from django.db.models import signals
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
# import uuid


def code_generator(size=18, chars=string.ascii_lowercase + string.digits ):
    new_code = ''
    for _ in range(size):
        new_code += random.choice(chars)
    return new_code


def account_generator(size=8, chars=string.digits):
    account = 'X' + ''
    for _ in range(size):
        account += random.choice(chars)

    return account

COUNTRIES = (
    ('AD',('Andorra')),
    ('AE', ('United Arab Emirates')),
    ('AF', ('Afghanistan')),
    ('AG', ('Antigua & Barbuda')),
    ('AI', ('Anguilla')),
    ('AL', ('Albania')),
    ('AM', ('Armenia')),
    ('AN', ('Netherlands Antilles')),
    ('AO', ('Angola')),
    ('AQ', ('Antarctica')),
    ('AR', ('Argentina')),
    ('AS', ('American Samoa')),
    ('AT', ('Austria')),
    ('AU', ('Australia')),
    ('AW', ('Aruba')),
    ('AZ', ('Azerbaijan')),
    ('BA', ('Bosnia and Herzegovina')),
    ('BB', ('Barbados')),
    ('BD', ('Bangladesh')),
    ('BE', ('Belgium')),
    ('BF', ('Burkina Faso')),
    ('BG', ('Bulgaria')),
    ('BH', ('Bahrain')),
    ('BI', ('Burundi')),
    ('BJ', ('Benin')),
    ('BM', ('Bermuda')),
    ('BN', ('Brunei Darussalam')),
    ('BO', ('Bolivia')),
    ('BR', ('Brazil')),
    ('BS', ('Bahama')),
    ('BT', ('Bhutan')),
    ('BV', ('Bouvet Island')),
    ('BW', ('Botswana')),
    ('BY', ('Belarus')),
    ('BZ', ('Belize')),
    ('CA', ('Canada')),
    ('CC', ('Cocos (Keeling) Islands')),
    ('CF', ('Central African Republic')),
    ('CG', ('Congo')),
    ('CH', ('Switzerland')),
    ('CI', ('Ivory Coast')),
    ('CK', ('Cook Iislands')),
    ('CL', ('Chile')),
    ('CM', ('Cameroon')),
    ('CN', ('China')),
    ('CO', ('Colombia')),
    ('CR', ('Costa Rica')),
    ('CU', ('Cuba')),
    ('CV', ('Cape Verde')),
    ('CX', ('Christmas Island')),
    ('CY', ('Cyprus')),
    ('CZ', ('Czech Republic')),
    ('DE', ('Germany')),
    ('DJ', ('Djibouti')),
    ('DK', ('Denmark')),
    ('DM', ('Dominica')),
    ('DO', ('Dominican Republic')),
    ('DZ', ('Algeria')),
    ('EC', ('Ecuador')),
    ('EE', ('Estonia')),
    ('EG', ('Egypt')),
    ('EH', ('Western Sahara')),
    ('ER', ('Eritrea')),
    ('ES', ('Spain')),
    ('ET', ('Ethiopia')),
    ('FI', ('Finland')),
    ('FJ', ('Fiji')),
    ('FK', ('Falkland Islands (Malvinas)')),
    ('FM', ('Micronesia')),
    ('FO', ('Faroe Islands')),
    ('FR', ('France')),
    ('FX', ('France, Metropolitan')),
    ('GA', ('Gabon')),
    ('GB', ('United Kingdom (Great Britain)')),
    ('GD', ('Grenada')),
    ('GE', ('Georgia')),
    ('GF', ('French Guiana')),
    ('GH', ('Ghana')),
    ('GI', ('Gibraltar')),
    ('GL', ('Greenland')),
    ('GM', ('Gambia')),
    ('GN', ('Guinea')),
    ('GP', ('Guadeloupe')),
    ('GQ', ('Equatorial Guinea')),
    ('GR', ('Greece')),
    ('GS', ('South Georgia and the South Sandwich Islands')),
    ('GT', ('Guatemala')),
    ('GU', ('Guam')),
    ('GW', ('Guinea-Bissau')),
    ('GY', ('Guyana')),
    ('HK', ('Hong Kong')),
    ('HM', ('Heard & McDonald Islands')),
    ('HN', ('Honduras')),
    ('HR', ('Croatia')),
    ('HT', ('Haiti')),
    ('HU', ('Hungary')),
    ('ID', ('Indonesia')),
    ('IE', ('Ireland')),
    ('IL', ('Israel')),
    ('IN', ('India')),
    ('IO', ('British Indian Ocean Territory')),
    ('IQ', ('Iraq')),
    ('IR', ('Islamic Republic of Iran')),
    ('IS', ('Iceland')),
    ('IT', ('Italy')),
    ('JM', ('Jamaica')),
    ('JO', ('Jordan')),
    ('JP', ('Japan')),
    ('KE', ('Kenya')),
    ('KG', ('Kyrgyzstan')),
    ('KH', ('Cambodia')),
    ('KI', ('Kiribati')),
    ('KM', ('Comoros')),
    ('KN', ('St. Kitts and Nevis')),
    ('KP', ('Korea, Democratic People\'s Republic of')),
    ('KR', ('Korea, Republic of')),
    ('KW', ('Kuwait')),
    ('KY', ('Cayman Islands')),
    ('KZ', ('Kazakhstan')),
    ('LA', ('Lao People\'s Democratic Republic')),
    ('LB', ('Lebanon')),
    ('LC', ('Saint Lucia')),
    ('LI', ('Liechtenstein')),
    ('LK', ('Sri Lanka')),
    ('LR', ('Liberia')),
    ('LS', ('Lesotho')),
    ('LT', ('Lithuania')),
    ('LU', ('Luxembourg')),
    ('LV', ('Latvia')),
    ('LY', ('Libyan Arab Jamahiriya')),
    ('MA', ('Morocco')),
    ('MC', ('Monaco')),
    ('MD', ('Moldova, Republic of')),
    ('MG', ('Madagascar')),
    ('MH', ('Marshall Islands')),
    ('ML', ('Mali')),
    ('MN', ('Mongolia')),
    ('MM', ('Myanmar')),
    ('MO', ('Macau')),
    ('MP', ('Northern Mariana Islands')),
    ('MQ', ('Martinique')),
    ('MR', ('Mauritania')),
    ('MS', ('Monserrat')),
    ('MT', ('Malta')),
    ('MU', ('Mauritius')),
    ('MV', ('Maldives')),
    ('MW', ('Malawi')),
    ('MX', ('Mexico')),
    ('MY', ('Malaysia')),
    ('MZ', ('Mozambique')),
    ('NA', ('Namibia')),
    ('NC', ('New Caledonia')),
    ('NE', ('Niger')),
    ('NF', ('Norfolk Island')),
    ('NG', ('Nigeria')),
    ('NI', ('Nicaragua')),
    ('NL', ('Netherlands')),
    ('NO', ('Norway')),
    ('NP', ('Nepal')),
    ('NR', ('Nauru')),
    ('NU', ('Niue')),
    ('NZ', ('New Zealand')),
    ('OM', ('Oman')),
    ('PA', ('Panama')),
    ('PE', ('Peru')),
    ('PF', ('French Polynesia')),
    ('PG', ('Papua New Guinea')),
    ('PH', ('Philippines')),
    ('PK', ('Pakistan')),
    ('PL', ('Poland')),
    ('PM', ('St. Pierre & Miquelon')),
    ('PN', ('Pitcairn')),
    ('PR', ('Puerto Rico')),
    ('PT', ('Portugal')),
    ('PW', ('Palau')),
    ('PY', ('Paraguay')),
    ('QA', ('Qatar')),
    ('RE', ('Reunion')),
    ('RO', ('Romania')),
    ('RU', ('Russian Federation')),
    ('RW', ('Rwanda')),
    ('SA', ('Saudi Arabia')),
    ('SB', ('Solomon Islands')),
    ('SC', ('Seychelles')),
    ('SD', ('Sudan')),
    ('SE', ('Sweden')),
    ('SG', ('Singapore')),
    ('SH', ('St. Helena')),
    ('SI', ('Slovenia')),
    ('SJ', ('Svalbard & Jan Mayen Islands')),
    ('SK', ('Slovakia')),
    ('SL', ('Sierra Leone')),
    ('SM', ('San Marino')),
    ('SN', ('Senegal')),
    ('SO', ('Somalia')),
    ('SR', ('Suriname')),
    ('ST', ('Sao Tome & Principe')),
    ('SV', ('El Salvador')),
    ('SY', ('Syrian Arab Republic')),
    ('SZ', ('Swaziland')),
    ('TC', ('Turks & Caicos Islands')),
    ('TD', ('Chad')),
    ('TF', ('French Southern Territories')),
    ('TG', ('Togo')),
    ('TH', ('Thailand')),
    ('TJ', ('Tajikistan')),
    ('TK', ('Tokelau')),
    ('TM', ('Turkmenistan')),
    ('TN', ('Tunisia')),
    ('TO', ('Tonga')),
    ('TP', ('East Timor')),
    ('TR', ('Turkey')),
    ('TT', ('Trinidad & Tobago')),
    ('TV', ('Tuvalu')),
    ('TW', ('Taiwan, Province of China')),
    ('TZ', ('Tanzania, United Republic of')),
    ('UA', ('Ukraine')),
    ('UG', ('Uganda')),
    ('UM', ('United States Minor Outlying Islands')),
    ('US', ('United States of America')),
    ('UY', ('Uruguay')),
    ('UZ', ('Uzbekistan')),
    ('VA', ('Vatican City State (Holy See)')),
    ('VC', ('St. Vincent & the Grenadines')),
    ('VE', ('Venezuela')),
    ('VG', ('British Virgin Islands')),
    ('VI', ('United States Virgin Islands')),
    ('VN', ('Viet Nam')),
    ('VU', ('Vanuatu')),
    ('WF', ('Wallis & Futuna Islands')),
    ('WS', ('Samoa')),
    ('YE', ('Yemen')),
    ('YT', ('Mayotte')),
    ('YU', ('Yugoslavia')),
    ('ZA', ('South Africa')),
    ('ZM', ('Zambia')),
    ('ZR', ('Zaire')),
    ('ZW', ('Zimbabwe')),
    ('ZZ', ('Unknown or unspecified country')),
)





Aluminium = 'Aluminium'
DIAMOND = 'DIAMOND'
Azuriite = 'Azuriite with Malanche'
Beryl = 'Beryl'
Beads = 'Beads'
Amazonnile = 'Amazonnile'
Agate = 'Agate'
Amber = 'Amber'
Ruby = 'Ruby'
Sapphire = 'Sapphire'
Calcite = 'Calcite'
Iron = 'Iron'
Moisanite = 'Moisanite'
Glass = 'Glass'
Emerald = 'Emerald'
Lapls = 'Lapls'
Pearl = 'Pearl'
Carbon = 'Carbon'
Quartz = 'Quartz'
Zircorn = 'Zircorn'
Niello = 'Niello'
TITANIUM = 'TITANIUM'
Corundum = 'Corundum'
Karat = 'Karat'
TANZANITE = 'TANZANITE'
Charoite = 'Charoite'
Tarnish = 'Tarnish'
Copper = 'Copper'
Silver = 'Silver'
Gold = 'Gold'
Platnum = 'Platnum'
pack = (
    (Silver, 'Silver'),
    (Tarnish, 'Tarnish'),
    (Charoite, 'Charoite'),
    (TANZANITE, 'TANZANITE'),
    (DIAMOND, 'DIAMOND'),
    (Karat, 'Karat'),
    (Corundum, 'Corundum'),
    (Gold, 'Gold'),
    (TITANIUM, 'TITANIUM'),
    (Niello, 'Niello'),
    (Quartz, 'Quartz'),
    (Copper, 'Copper'),
    (Carbon, 'Carbon'),
    (Pearl, 'Pearl'),
    (Lapls, 'Lapls'),
    (Iron, 'Iron'),
    (Emerald, 'Emerald'),
    (Glass, 'Glass'),
    (Moisanite, 'Moisanite'),
    (Calcite, 'Calcite'),
    (Sapphire, 'Sapphire'),
    (Ruby, 'Ruby'),
    (Amber, 'Amber'),
    (Agate, 'Agate'),
    (Amazonnile, 'Amazonnile'),
    (Beads, 'Beads'),
    (Beryl, 'Beryl'),
    (Azuriite, 'Azuriite with Malanche'),
    (Zircorn, 'Zircorn'),
    (Aluminium, 'Aluminium'),
    (Gold, 'Gold'),
    (Platnum, 'Platnum'),
    )
class UserInfo(models.Model):
    user = models.OneToOneField(User, null=True)
    full_name = models.CharField(max_length=120, blank=True, default='')
    amount = models.FloatField(blank=False, validators=[MinValueValidator(0)], default=0.00)
    bitcoin_amount = models.FloatField(blank=False, validators=[MinValueValidator(0)], default=0.00)
    Perfect_money = models.CharField(max_length=14, blank=True, default='')
    Bitcoin = models.CharField(max_length=120, blank=True, default='')
    Payeer = models.CharField(max_length=35, blank=True, default='')
    advcash = models.CharField(max_length=35, blank=True, default='')
    Phone_no = models.CharField(max_length=14, default='')
    country = models.CharField(max_length=120, blank=False, choices=COUNTRIES, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    Bio = models.CharField(max_length=120, blank=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    total_deposit = models.FloatField(blank=False, default=0)
    total_bitcoin_deposit = models.FloatField(blank=False, default=0)
    shortcode = models.CharField(max_length=15, unique=True, null=False, blank=True)
    verification_code = models.CharField(max_length=6, default='')
    security_code = models.CharField(max_length=4, blank=False, null=True)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = code_generator()
        super(UserInfo, self).save(*args, **kwargs)



    def send_activation_email(self):
        if not self.activated:
            self.shortcode = code_generator()
            self.save()
            path_ = reverse('activate', kwargs={"code": self.code})
            subject = 'some activation'
            from_email = settings.DEFAULT_FROM_EMAIL
            message = "This is your activation key: {path_}"
            recipient_list = [self.user.email]
            html_message = '<p>Activate your email here: {path_}<p>'
            sent_email = send_mail(subject, message, from_email, recipient_list, fail_silently=False, html_message=html_message )
            return sent_email


# class TaskManager(models.Manager):
#     # def all(self, *args, **kwargs):
#     #     qs_main = super(TaskManager, self).all(*args, **kwargs)
#     #     qs = qs_main.filter(active=True)
#     #     return qs
#     def recurence(self, *args, **kwargs):
#         wamba = UserInfo.objects.all()
#         wolt = Investment.objects.all()
#         for w in wamba:
#             if w.amount >= 10000:
#                 wolt.balance = w.amount * 0.75 / 100
#             elif w.amount >= 100000:
#                 wolt.balance = w.amount * 1 / 100
#             elif w.amount >= 500000:
#                 wolt.balance = w.amount * 1.1 / 100
#                 wolt.save()


    # def acc(self, *args, **kwargs):
    #     if self.Account_no is None or self.Account_no == "":
    #         self.Account_no = account_generator()
    #     super(UserInfo, self).save(*args, **kwargs)






# class walt(AbstractBaseUser, PermissionsMixin):
#     REQUIRED_FIELDS = []
#     USERNAME_FIELD = 'email'
#
#     email = models.EmailField('email', unique=True, blank=False, null=False)
#     full_name = models.CharField('full name', blank=True, null=True, max_length=400)
#     is_staff = models.BooleanField('staff status', default=False)
#     is_active = models.BooleanField('active', default=True)
#     is_verified = models.BooleanField('verified', default=False) # Add the `is_verified` flag
#     verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)

    # def get_short_name(self):
    #     return self.email

    # def get_full_name(self):
    #     return self.email
Usd = 'Usd'
Bitcoin = 'Bitcoin'
ACCOUNT_TYPE_CHOICES = (
    (Usd, 'Usd'),
    (Bitcoin, 'Bitcoin'),

    )

class Investment(models.Model):


    user = models.OneToOneField(User, null=True)
    balance = models.FloatField(blank=False, default=0.00)
    Bitcoin_balance = models.FloatField(blank=True, validators=[MinValueValidator(0)], default=0.00)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE_CHOICES, default='', blank=False)
    requested_amount = models.FloatField(blank=False, validators=[MinValueValidator(0)], default=0.00)
    account_no = models.CharField(max_length=120, blank=False, null=True)
    last_withdrawal = models.FloatField(blank=False, default=0.0)
    pending_withdrawal = models.FloatField(blank=False, default=0.00)


    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):

        if self.account_no is None or self.account_no == "":
            self.account_no = account_generator()
        super(Investment, self).save(*args, **kwargs)

# Or, if we wish to be able to store "(800) 555-1212 x123" as "8005551212x123" and perhaps vanity numbers like "(888) 4-VANITY" as "8884VANITY," then:


# class PhoneNumber(models.TextField):
#     def clean(self):
#         return re.sub(r'\W', '', str(self))



Unconfirmed = 'Unconfirmed'
Confirmed = 'Confirmed'
sign = (
    (Confirmed, 'Confirmed'),
    (Unconfirmed, 'Unconfirmed'),


)


class Statistics(models.Model):
    user = models.CharField(max_length=25, default='lewicpro')
    profit = models.FloatField(blank=True, default=0)
    total_deposited = models.FloatField(blank=True, default=0)
    bitcoin_profit = models.FloatField(blank=True, default=0)
    total_withdrawn = models.FloatField(blank=True, default=0)
    last_withdrawn = models.FloatField(blank=True, default=0)
    total_balance = models.FloatField(blank=True, default=0)
    bitcoin_total_deposited = models.FloatField(blank=True, default=0)
    bitcoin_total_withdrawn = models.FloatField(blank=True, default=0)
    bitcoin_last_withdrawn = models.FloatField(blank=True, default=0)
    bitcoin_total_balance = models.FloatField(blank=True, default=0)

    def __str__(self):
        return self.user


class TransactionPerfectMoney (models.Model):
    user = models.CharField(max_length=125, blank=False, null=True)
    username = models.CharField(max_length=125, blank=False, null=True)
    processor = models.CharField(max_length=125, blank=False, null=True)
    package = models.CharField(max_length=125, blank=False, null=True, choices=pack)
    PAYMENT_AMOUNT = models.FloatField(max_length=35, validators=[MinValueValidator(0)], blank=False, null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    Plan = models.CharField(max_length=120, null=True, blank=True)
    opens = models.DateTimeField( null=True, blank=True)
    closes = models.DateTimeField(null=True, blank=True)
    expectedIncome = models.FloatField(blank=False, default=0)
    actualDeposit = models.CharField(max_length=120, null=True, blank=False)
    sign = models.CharField(max_length=120, default=Unconfirmed, blank=False, choices=sign)
    hashid = models.CharField(max_length=120, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.closes is None or self.closes == "":
            if self.package == Silver:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Tarnish:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Charoite:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == TANZANITE:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Karat:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Corundum:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == TITANIUM:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Niello:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Zircorn:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == DIAMOND:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Quartz:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Carbon:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Gold:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Aluminium:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Pearl:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Platnum:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()




            elif self.package == Copper:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.PAYMENT_AMOUNT + self.PAYMENT_AMOUNT * 125 / 100
                self.opens = timezone.now()

            elif self.package == Lapls:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.PAYMENT_AMOUNT + self.PAYMENT_AMOUNT * 135 / 100
                self.opens = timezone.now()

            elif self.package == Emerald:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.PAYMENT_AMOUNT + self.PAYMENT_AMOUNT * 150 / 100
                self.opens = timezone.now()

            elif self.package == Iron:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.PAYMENT_AMOUNT + self.PAYMENT_AMOUNT * 150 / 100
                self.opens = timezone.now()

            elif self.package == Glass:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.PAYMENT_AMOUNT + self.PAYMENT_AMOUNT * 170 / 100
                self.opens = timezone.now()

            elif self.package == Moisanite:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.PAYMENT_AMOUNT + self.PAYMENT_AMOUNT * 200 / 100
                self.opens = timezone.now()

            elif self.package == Calcite:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.PAYMENT_AMOUNT + self.PAYMENT_AMOUNT * 250 / 100
                self.opens = timezone.now()

            elif self.package == Sapphire:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.PAYMENT_AMOUNT + self.PAYMENT_AMOUNT * 300 / 100
                self.opens = timezone.now()

            elif self.package == Ruby:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.PAYMENT_AMOUNT + self.PAYMENT_AMOUNT * 385 / 100
                self.opens = timezone.now()

            elif self.package == Amber:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.PAYMENT_AMOUNT + self.PAYMENT_AMOUNT * 700 / 100
                self.opens = timezone.now()

            elif self.package == Agate:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.PAYMENT_AMOUNT + self.PAYMENT_AMOUNT * 1200 / 100
                self.opens = timezone.now()

            elif self.package == Amazonnile:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.PAYMENT_AMOUNT + self.PAYMENT_AMOUNT * 1700 / 100
                self.opens = timezone.now()

            elif self.package == Beads:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.PAYMENT_AMOUNT + self.PAYMENT_AMOUNT * 1200 / 100
                self.opens = timezone.now()

            elif self.package == Beryl:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.PAYMENT_AMOUNT + self.PAYMENT_AMOUNT * 1500 / 100
                self.opens = timezone.now()

            elif self.package == Azuriite:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.PAYMENT_AMOUNT + self.PAYMENT_AMOUNT * 2000 / 100
                self.opens = timezone.now()
        super(TransactionPerfectMoney, self).save(*args, **kwargs)

    # def got(self, *args, **kwargs):
    #     if self.title is None or self.title == "":
    #         self.title = 3 * 14
    #     super(TransactionPerfectMoney, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     if self.shortcode is None or self.shortcode == "":
    #         self.shortcode = code_generator()
    #     super(UserInfo, self).save(*args, **kwargs)



            #
            # >>> from app.models import TransactionPerfectMoney
            # >>> import datetime
            # >>> sd = datetime.date(2009, 12, 28)
            # >>> t = "New Year's Resolutions"
            # >>> s =TransactionPerfectMoney.objects.create(processor=t, opens=sd)
            # >>> s
            # <Survey: New Year's Resolutions (Opens 2009-12-28, closes 2010-01-04)>

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Perfect Money Transactions"


class BalanceTransaction(models.Model):
    user = models.CharField(max_length=125, blank=True, null=True)
    from_account_no = models.CharField(max_length=125, blank=True, null=True)
    currency_transfered = models.CharField(max_length=120, choices=ACCOUNT_TYPE_CHOICES, blank=False, null=True)
    username_receiver = models.CharField(max_length=120, blank=False, null=True)
    security_code = models.CharField(max_length=120, blank=False, null=True)
    amount_transfered = models.FloatField(blank=False, null=True)
    date_stamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Account Balance Transactions"


class BalanceRedeposit(models.Model):
    user = models.CharField(max_length=125, blank=True, null=True)
    username = models.CharField(max_length=120, blank=True, null=True)
    processor = models.CharField(max_length=120, blank=True, null=True)
    Xumpesa_account = models.CharField(max_length=120, blank=False, null=True)
    package = models.CharField(max_length=125, blank=False, null=True, choices=pack)
    amount_transfered = models.FloatField(blank=False, validators=[MinValueValidator(0)], null=True)
    date_stamp = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    Plan = models.CharField(max_length=120, null=True, blank=True)
    opens = models.DateTimeField(null=True, blank=True)
    expectedIncome = models.FloatField(blank=False, default=0)
    hashid = models.CharField(max_length=120, null=True, blank=True)
    closes = models.DateTimeField(null=True, blank=True)
    actualDeposit = models.CharField(max_length=120, null=True, blank=False)
    sign = models.CharField(max_length=120, default=Unconfirmed, blank=False, choices=sign)

    def save(self, *args, **kwargs):
        if self.closes is None or self.closes == "":
            if self.package == Silver:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Tarnish:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Charoite:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == TANZANITE:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Karat:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Corundum:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == TITANIUM:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Niello:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Zircorn:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == DIAMOND:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Quartz:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Carbon:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Gold:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Aluminium:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Pearl:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Platnum:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()




            elif self.package == Copper:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.amount_transfered + self.amount_transfered * 125 / 100
                self.opens = timezone.now()

            elif self.package == Lapls:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.amount_transfered + self.amount_transfered * 135 / 100
                self.opens = timezone.now()

            elif self.package == Emerald:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.amount_transfered + self.amount_transfered * 150 / 100
                self.opens = timezone.now()

            elif self.package == Iron:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.amount_transfered + self.amount_transfered * 150 / 100
                self.opens = timezone.now()

            elif self.package == Glass:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.amount_transfered + self.amount_transfered * 170 / 100
                self.opens = timezone.now()

            elif self.package == Moisanite:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.amount_transfered + self.amount_transfered * 200 / 100
                self.opens = timezone.now()

            elif self.package == Calcite:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.amount_transfered + self.amount_transfered * 250 / 100
                self.opens = timezone.now()

            elif self.package == Sapphire:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.amount_transfered + self.amount_transfered * 300 / 100
                self.opens = timezone.now()

            elif self.package == Ruby:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.amount_transfered + self.amount_transfered * 385 / 100
                self.opens = timezone.now()

            elif self.package == Amber:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.amount_transfered + self.amount_transfered * 700 / 100
                self.opens = timezone.now()

            elif self.package == Agate:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.amount_transfered + self.amount_transfered * 1200 / 100
                self.opens = timezone.now()

            elif self.package == Amazonnile:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.amount_transfered + self.amount_transfered * 1700 / 100
                self.opens = timezone.now()

            elif self.package == Beads:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.amount_transfered + self.amount_transfered * 1200 / 100
                self.opens = timezone.now()

            elif self.package == Beryl:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.amount_transfered + self.amount_transfered * 1500 / 100
                self.opens = timezone.now()

            elif self.package == Azuriite:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.amount_transfered + self.amount_transfered * 2000 / 100
                self.opens = timezone.now()
            super(BalanceRedeposit, self).save(*args, **kwargs)






    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = "Redeposit Transactions"


class TransactionPayeer (models.Model):
    user = models.CharField(max_length=125, blank=False, null=True)
    username = models.CharField(max_length=125, blank=False, null=True)
    processor = models.CharField(max_length=125, blank=False, null=True)
    package = models.CharField(max_length=125, blank=False, null=True, choices=pack)
    m_amount = models.FloatField( blank=False, validators=[MinValueValidator(0)], null=True)
    opens = models.DateTimeField(null=True, blank=True)
    closes = models.DateTimeField(null=True, blank=True)


    m_shop =models.CharField(max_length=185, blank=False, null=True)
    m_orderid=models.CharField(max_length=185, blank=False, null=True)
    m_curr = models.CharField(max_length=185, blank=False, null=True)
    m_desc = models.CharField(max_length=185, blank=False, null=True)
    description = models.CharField(max_length=185, blank=False, null=True)
    m_key =models.CharField(max_length=185, blank=False, null=True)
    actualDeposit = models.CharField(max_length=180, null=True, blank=False)
    m_sign = models.CharField(max_length=185, blank=False, null=True)

    sign = models.CharField(max_length=120, default=Unconfirmed, blank=False, choices=sign)
    Plan = models.CharField(max_length=120, null=True, blank=True)
    expectedIncome = models.FloatField(blank=False, default=0)
    hashid = models.CharField(max_length=120, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def save(self, *args, **kwargs):
        if self.closes is None or self.closes == "":
            if self.package == Silver:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()


            elif self.package == Tarnish:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Charoite:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == TANZANITE:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Karat:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Corundum:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == TITANIUM:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Niello:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Zircorn:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == DIAMOND:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Quartz:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Carbon:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.opens = timezone.now()

            elif self.package == Gold:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Aluminium:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Pearl:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Platnum:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()




            elif self.package == Copper:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.expectedIncome = self.m_amount + self.m_amount * 125 /100
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Lapls:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.m_amount + self.m_amount * 135 / 100
                self.opens = timezone.now()

            elif self.package == Emerald:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.m_amount + self.m_amount * 150 / 100
                self.opens = timezone.now()

            elif self.package == Iron:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.m_amount + self.m_amount * 150 / 100
                self.opens = timezone.now()

            elif self.package == Glass:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.m_amount + self.m_amount * 170 / 100
                self.opens = timezone.now()

            elif self.package == Moisanite:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.m_amount + self.m_amount * 200 / 100
                self.opens = timezone.now()


            elif self.package == Calcite:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.m_amount + self.m_amount * 250 / 100
                self.opens = timezone.now()

            elif self.package == Sapphire:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.m_amount + self.m_amount * 300 / 100
                self.opens = timezone.now()

            elif self.package == Ruby:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.m_amount + self.m_amount * 385 / 100
                self.opens = timezone.now()

            elif self.package == Amber:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.m_amount + self.m_amount * 700 / 100
                self.opens = timezone.now()

            elif self.package == Agate:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.m_amount + self.m_amount * 1200 / 100
                self.opens = timezone.now()

            elif self.package == Amazonnile:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.m_amount + self.m_amount * 1700 / 100
                self.opens = timezone.now()

            elif self.package == Beads:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.m_amount + self.m_amount * 1200 / 100
                self.opens = timezone.now()

            elif self.package == Beryl:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.m_amount + self.m_amount * 1500 / 100
                self.opens = timezone.now()

            elif self.package == Azuriite:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.m_amount + self.m_amount * 2000 / 100
                self.opens = timezone.now()
        super(TransactionPayeer, self).save(*args, **kwargs)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = "Payeer Transactions"



class TransactionBitcoin(models.Model):
    user = models.CharField(max_length=125, blank=False, null=True)
    username = models.CharField(max_length=125, blank=False, null=True)
    processor = models.CharField(max_length=125, blank=False, null=True)
    package = models.CharField(max_length=125, blank=False, null=True, choices=pack)
    b_amount = models.FloatField(blank=False, null=True, validators=[MinValueValidator(0)], default=0)
    opens = models.DateTimeField(null=True, blank=True)
    closes = models.DateTimeField(null=True, blank=True)
    actualDeposit = models.CharField(max_length=120, default=0, blank=False)
    sign = models.CharField(max_length=120, default=Unconfirmed, blank=False, choices=sign)
    Plan = models.CharField(max_length=120, null=True, blank=True)
    expectedIncome = models.FloatField(blank=False, default=0)
    hashid = models.CharField(max_length=120, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def save(self, *args, **kwargs):
        if self.closes is None or self.closes == "":
            if self.package == Silver:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()


            elif self.package == Tarnish:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Charoite:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == TANZANITE:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Karat:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Corundum:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == TITANIUM:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Niello:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Zircorn:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == DIAMOND:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Quartz:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Carbon:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.opens = timezone.now()

            elif self.package == Gold:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Aluminium:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Pearl:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Platnum:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()




            elif self.package == Copper:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.expectedIncome = self.b_amount + self.b_amount * 125 /100
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Lapls:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 135 / 100
                self.opens = timezone.now()

            elif self.package == Emerald:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 150 / 100
                self.opens = timezone.now()

            elif self.package == Iron:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 150 / 100
                self.opens = timezone.now()

            elif self.package == Glass:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 170 / 100
                self.opens = timezone.now()

            elif self.package == Moisanite:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 200 / 100
                self.opens = timezone.now()


            elif self.package == Calcite:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 250 / 100
                self.opens = timezone.now()

            elif self.package == Sapphire:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 300 / 100
                self.opens = timezone.now()

            elif self.package == Ruby:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 385 / 100
                self.opens = timezone.now()

            elif self.package == Amber:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 700 / 100
                self.opens = timezone.now()

            elif self.package == Agate:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 1200 / 100
                self.opens = timezone.now()

            elif self.package == Amazonnile:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 1700 / 100
                self.opens = timezone.now()

            elif self.package == Beads:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 1200 / 100
                self.opens = timezone.now()

            elif self.package == Beryl:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 1500 / 100
                self.opens = timezone.now()

            elif self.package == Azuriite:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 2000 / 100
                self.opens = timezone.now()
        super(TransactionBitcoin, self).save(*args, **kwargs)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = "Bitcoin Transactions"



class BitcoinRedepositModels(models.Model):
    user = models.CharField(max_length=125, blank=False, null=True)
    username = models.CharField(max_length=125, blank=False, null=True)
    processor = models.CharField(max_length=125, blank=False, null=True)
    package = models.CharField(max_length=125, blank=False, null=True, choices=pack)
    b_amount = models.FloatField(blank=False, validators=[MinValueValidator(0)], null=True, default=0)
    opens = models.DateTimeField(null=True, blank=True)
    closes = models.DateTimeField(null=True, blank=True)
    actualDeposit = models.CharField(max_length=120, default=0, blank=False)
    sign = models.CharField(max_length=120, default=Unconfirmed, blank=False, choices=sign)
    Plan = models.CharField(max_length=120, null=True, blank=True)
    expectedIncome = models.FloatField(blank=False, default=0)
    hashid = models.CharField(max_length=120, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def save(self, *args, **kwargs):
        if self.closes is None or self.closes == "":
            if self.package == Silver:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()


            elif self.package == Tarnish:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Charoite:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == TANZANITE:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Karat:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Corundum:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == TITANIUM:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Niello:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Zircorn:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == DIAMOND:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Quartz:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Carbon:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.opens = timezone.now()

            elif self.package == Gold:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Aluminium:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Pearl:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Platnum:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()




            elif self.package == Copper:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.expectedIncome = self.b_amount + self.b_amount * 125 /100
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Lapls:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 135 / 100
                self.opens = timezone.now()

            elif self.package == Emerald:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 150 / 100
                self.opens = timezone.now()

            elif self.package == Iron:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 150 / 100
                self.opens = timezone.now()

            elif self.package == Glass:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 170 / 100
                self.opens = timezone.now()

            elif self.package == Moisanite:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 200 / 100
                self.opens = timezone.now()


            elif self.package == Calcite:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 250 / 100
                self.opens = timezone.now()

            elif self.package == Sapphire:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 300 / 100
                self.opens = timezone.now()

            elif self.package == Ruby:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 385 / 100
                self.opens = timezone.now()

            elif self.package == Amber:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 700 / 100
                self.opens = timezone.now()

            elif self.package == Agate:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 1200 / 100
                self.opens = timezone.now()

            elif self.package == Amazonnile:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 1700 / 100
                self.opens = timezone.now()

            elif self.package == Beads:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 1200 / 100
                self.opens = timezone.now()

            elif self.package == Beryl:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 1500 / 100
                self.opens = timezone.now()

            elif self.package == Azuriite:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.b_amount + self.b_amount * 2000 / 100
                self.opens = timezone.now()
        super(BitcoinRedepositModels, self).save(*args, **kwargs)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = "Bitcoin Redeposit transaction"




class OKpayDeoisitModel(models.Model):
    user = models.CharField(max_length=125, blank=False, null=True)
    username = models.CharField(max_length=125, blank=False, null=True)
    processor = models.CharField(max_length=125, blank=False, null=True)
    package = models.CharField(max_length=125, blank=False, null=True, choices=pack)
    o_amount = models.FloatField(blank=False, validators=[MinValueValidator(0)], null=True, default=0)
    opens = models.DateTimeField(null=True, blank=True)
    closes = models.DateTimeField(null=True, blank=True)
    actualDeposit = models.CharField(max_length=120, default=0, blank=False)
    sign = models.CharField(max_length=120, default=Unconfirmed, blank=False, choices=sign)
    Plan = models.CharField(max_length=120, null=True, blank=True)
    expectedIncome = models.FloatField(blank=False, default=0)
    hashid = models.CharField(max_length=120, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def save(self, *args, **kwargs):
        if self.closes is None or self.closes == "":
            if self.package == Silver:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()


            elif self.package == Tarnish:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Charoite:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == TANZANITE:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Karat:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Corundum:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == TITANIUM:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Niello:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Zircorn:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == DIAMOND:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Quartz:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Carbon:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.opens = timezone.now()

            elif self.package == Gold:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Aluminium:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Pearl:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Platnum:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()




            elif self.package == Copper:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.expectedIncome = self.o_amount + self.o_amount * 125 /100
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Lapls:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.o_amount + self.o_amount * 135 / 100
                self.opens = timezone.now()

            elif self.package == Emerald:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.o_amount + self.o_amount * 150 / 100
                self.opens = timezone.now()

            elif self.package == Iron:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.o_amount + self.o_amount * 150 / 100
                self.opens = timezone.now()

            elif self.package == Glass:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.o_amount + self.o_amount * 170 / 100
                self.opens = timezone.now()

            elif self.package == Moisanite:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.o_amount + self.o_amount * 200 / 100
                self.opens = timezone.now()


            elif self.package == Calcite:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.o_amount + self.o_amount * 250 / 100
                self.opens = timezone.now()

            elif self.package == Sapphire:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.o_amount + self.o_amount * 300 / 100
                self.opens = timezone.now()

            elif self.package == Ruby:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.o_amount + self.o_amount * 385 / 100
                self.opens = timezone.now()

            elif self.package == Amber:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.o_amount + self.o_amount * 700 / 100
                self.opens = timezone.now()

            elif self.package == Agate:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.o_amount + self.o_amount * 1200 / 100
                self.opens = timezone.now()

            elif self.package == Amazonnile:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.o_amount + self.o_amount * 1700 / 100
                self.opens = timezone.now()

            elif self.package == Beads:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.o_amount + self.o_amount * 1200 / 100
                self.opens = timezone.now()

            elif self.package == Beryl:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.o_amount + self.o_amount * 1500 / 100
                self.opens = timezone.now()

            elif self.package == Azuriite:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.o_amount + self.o_amount * 2000 / 100
                self.opens = timezone.now()
        super(OKpayDeoisitModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = "OK payTransactions"



class AdvCashDeposit(models.Model):
    user = models.CharField(max_length=125, blank=False, null=True)
    username = models.CharField(max_length=125, blank=False, null=True)
    processor = models.CharField(max_length=125, blank=False, null=True)
    package = models.CharField(max_length=125, blank=False, null=True, choices=pack)
    a_amount = models.FloatField(blank=False, validators=[MinValueValidator(0)], null=True, default=0)
    opens = models.DateTimeField(null=True, blank=True)
    closes = models.DateTimeField(null=True, blank=True)
    actualDeposit = models.CharField(max_length=120, default=0, blank=False)
    sign = models.CharField(max_length=120, default=Unconfirmed, blank=False, choices=sign)
    Plan = models.CharField(max_length=120, null=True, blank=True)
    expectedIncome = models.FloatField(blank=False, default=0)
    hashid = models.CharField(max_length=120, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def save(self, *args, **kwargs):
        if self.closes is None or self.closes == "":
            if self.package == Silver:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()


            elif self.package == Tarnish:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Charoite:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == TANZANITE:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Karat:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Corundum:
                self.closes = timezone.now() + timedelta(60)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == TITANIUM:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Niello:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Zircorn:
                self.closes = timezone.now() + timedelta(90)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == DIAMOND:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Quartz:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Carbon:
                self.closes = timezone.now() + timedelta(100)
                self.Plan = 'Daily Plan'
                self.opens = timezone.now()

            elif self.package == Gold:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Aluminium:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Pearl:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Platnum:
                self.closes = timezone.now() + timedelta(125)
                self.Plan = 'Daily Plan'
                self.hashid = code_generator()
                self.opens = timezone.now()




            elif self.package == Copper:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.expectedIncome = self.a_amount + self.a_amount * 125 /100
                self.hashid = code_generator()
                self.opens = timezone.now()

            elif self.package == Lapls:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.a_amount + self.a_amount * 135 / 100
                self.opens = timezone.now()

            elif self.package == Emerald:
                self.closes = timezone.now() + timedelta(5)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.a_amount + self.a_amount * 150 / 100
                self.opens = timezone.now()

            elif self.package == Iron:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.a_amount + self.a_amount * 150 / 100
                self.opens = timezone.now()

            elif self.package == Glass:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.a_amount + self.a_amount * 170 / 100
                self.opens = timezone.now()

            elif self.package == Moisanite:
                self.closes = timezone.now() + timedelta(7)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.a_amount + self.a_amount * 200 / 100
                self.opens = timezone.now()


            elif self.package == Calcite:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.a_amount + self.a_amount * 250 / 100
                self.opens = timezone.now()

            elif self.package == Sapphire:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.a_amount + self.a_amount * 300 / 100
                self.opens = timezone.now()

            elif self.package == Ruby:
                self.closes = timezone.now() + timedelta(15)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.a_amount + self.a_amount * 385 / 100
                self.opens = timezone.now()

            elif self.package == Amber:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.a_amount + self.a_amount * 700 / 100
                self.opens = timezone.now()

            elif self.package == Agate:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.a_amount + self.a_amount * 1200 / 100
                self.opens = timezone.now()

            elif self.package == Amazonnile:
                self.closes = timezone.now() + timedelta(30)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.a_amount + self.a_amount * 1700 / 100
                self.opens = timezone.now()

            elif self.package == Beads:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.a_amount + self.a_amount * 1200 / 100
                self.opens = timezone.now()

            elif self.package == Beryl:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.a_amount + self.a_amount * 1500 / 100
                self.opens = timezone.now()

            elif self.package == Azuriite:
                self.closes = timezone.now() + timedelta(50)
                self.Plan = 'After Plan'
                self.hashid = code_generator()
                self.expectedIncome = self.a_amount + self.a_amount * 2000 / 100
                self.opens = timezone.now()
        super(AdvCashDeposit, self).save(*args, **kwargs)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = "adv Deposit table"




Verified = 'Verified'
Not_verified = 'not verified'
Account_types = (
    (Verified, 'Verified'),
    (Not_verified, 'Not verified'),
)


class Deposits(models.Model):
    user = models.CharField(max_length=120, null=True)
    depositing_amount = models.PositiveIntegerField(blank=False, null=True)
    name = models.CharField(max_length=120, blank=False, null=True)
    account_number = models.CharField(max_length=120, blank=False, null=True)
    processor = models.CharField(max_length=120, blank=False, null=True)
    kumbukumbu_no = models.CharField(max_length=120, default='')
    package = models.CharField(max_length=125, blank=False, null=True, choices=pack)
    opens = models.DateField(null=True, blank=True)
    closes = models.DateField(null=True, blank=True)
    shortcode = models.CharField(max_length=15, null=True, blank=True)
    status = models.CharField(max_length=120, blank=False, choices=Account_types, default=Not_verified)
    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = code_generator()
            if self.closes is None or self.closes == "":
                if self.package == Silver:
                    self.closes = timezone.now() + timedelta(10)
                    self.opens = timezone.now()

                elif self.package == Gold:
                    self.closes = timezone.now() + timedelta(20)
                    self.opens = timezone.now()

                elif self.package == Platnum:
                    self.closes = timezone.now() + timedelta(30)
                    self.opens = timezone.now()
        super(Deposits, self).save(*args, **kwargs)



class DepositsVerified(models.Model):
    user = models.CharField(max_length=120, null=True)
    username = models.CharField(max_length=120, null=True)
    processor = models.CharField(max_length=120, null=True)
    amount_deposited = models.CharField(max_length=120, validators=[MinValueValidator(0)], blank=False, null=True)
    startdate = models.DateTimeField(blank=False, null=True)
    enddate = models.DateTimeField(blank=False, null=True)
    # processor = models.CharField(max_length=120, blank=False, null=True)
    package = models.CharField(max_length=120, blank=True, null=True)
    sign = models.CharField(max_length=120, blank=False, default='Confirmed')
    hashid = models.CharField(max_length=120, blank=True, null=True)
    expected_income = models.DateField(null=True, blank=True)
    shortcode = models.CharField(max_length=15, null=True, blank=True)


    def __str__(self):
        return self.user





# def duration():
#     oneMinutes = datetime.timedelta(minutes=1)
#     start = datetime.datetime.now() + oneMinutes
#     while datetime.datetime.now() < start:
#         time.sleep(1)
#     Investment.balance = Investment.amount * 0.02 + Investment.amount
#     Investment.save()




# def user_post_save(sender, instance, signal, *args, **kwargs):
#     if not instance.is_verified:
#         # Send verification email
#         send_mail(
#             'Verify your QuickPublisher account',
#             'Follow this link to verify your account: '
#                 'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(instance.verification_uuid)}),
#             'from@quickpublisher.dev',
#             [instance.email],
#             fail_silently=False,
#         )
#
# signals.post_save.connect(user_post_save, sender=User)




#overriding dates

# def save(self, **kwargs):
#     if not self.pk and self.opens and not self.closes:
#         self.closes = self.opens + datetime.timedelta(7)
#     super(Survey, self).save(**kwargs)


class Withdraw(models.Model):
    user = models.CharField(max_length=120, blank=False, null=True)
    full_name = models.CharField(max_length=120, blank=False, null=True)
    balance = models.CharField(max_length=120, blank=False, null=True)
    processor = models.CharField(max_length=120, blank=False, null=True)
    tigopesa_number = models.CharField(max_length=120, blank=False, null=True)
    withdrawing_amount = models.PositiveIntegerField(blank=False, null=True)
    account_number = models.CharField(max_length=120, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=15, null=True, blank=True)


class Withdrawprocessor(models.Model):
    user = models.CharField(max_length=120, blank=False, null=True)
    full_name = models.CharField(max_length=120, blank=False, null=True)
    balance = models.CharField(max_length=120, blank=False, null=True)
    processor = models.CharField(max_length=120, blank=False, null=True)
    processor_acc_number = models.CharField(max_length=120, blank=False, null=True)
    m_amount = models.PositiveIntegerField(blank=False, null=True)
    account_number = models.CharField(max_length=120, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    email = models.CharField(max_length=120, blank=False, null=True)
    status = models.CharField(max_length=15, null=True, blank=True)



class VerifiedWithdrawals(models.Model):
    user = models.CharField(max_length=120, blank=False, null=True)
    full_name = models.CharField(max_length=120, blank=False, null=True)
    balance = models.CharField(max_length=120, blank=False, null=True)
    processor = models.CharField(max_length=120, blank=False, null=True)
    processor_account_number = models.CharField(max_length=120, blank=True, null=True)
    m_amount = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    Status = models.CharField(max_length=120, blank=True, null=True)




class Processors(models.Model):
    user = models.OneToOneField(User, null=True)
    perfectmoney = models.FloatField(blank=True, validators=[MinValueValidator(0)], default=0)
    payeer = models.FloatField(blank=True, validators=[MinValueValidator(0)], default=0)
    bitcoin = models.FloatField(blank=True, validators=[MinValueValidator(0)], default=0)
    adcash = models.FloatField(blank=True, validators=[MinValueValidator(0)], default=0)
    okpay =models.FloatField(blank=True, validators=[MinValueValidator(0)], default=0)
    Etherium = models.FloatField(blank=True, validators=[MinValueValidator(0)], default=0)
    XamCoin = models.FloatField(blank=True, validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return self.user.username



class bitcoinBalanceDeposit(models.Model):
    user = models.CharField(max_length=125, blank=False, null=True)
    username = models.CharField(max_length=125, blank=False, null=True)
    processor = models.CharField(max_length=125, blank=False, null=True)
    b_amount = models.FloatField(blank=False, validators=[MinValueValidator(0)], null=True, default=0)
    actualDeposit = models.CharField(max_length=120, default=0, blank=False)
    sign = models.CharField(max_length=120, default=Unconfirmed, blank=False, choices=sign)
    hashid = models.CharField(max_length=120, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def save(self, *args, **kwargs):
        if self.hashid is None or self.hashid == "":
            self.hashid = code_generator()
            super(bitcoinBalanceDeposit, self).save(*args, **kwargs)



class AdvCashBalanceDeposit(models.Model):
    user = models.CharField(max_length=125, blank=False, null=True)
    username = models.CharField(max_length=125, blank=False, null=True)
    processor = models.CharField(max_length=125, blank=False, null=True)
    a_amount = models.FloatField(blank=False, validators=[MinValueValidator(0)], null=True, default=0)
    actualDeposit = models.CharField(max_length=120, default=0, blank=False)
    sign = models.CharField(max_length=120, default=Unconfirmed, blank=False, choices=sign)
    hashid = models.CharField(max_length=120, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def save(self, *args, **kwargs):
        if self.hashid is None or self.hashid == "":
            self.hashid = code_generator()
            super(AdvCashBalanceDeposit, self).save(*args, **kwargs)




class OKPayBalanceDeposit(models.Model):
    user = models.CharField(max_length=125, blank=False, null=True)
    username = models.CharField(max_length=125, blank=False, null=True)
    processor = models.CharField(max_length=125, blank=False, null=True)
    o_amount = models.FloatField(blank=False , validators=[MinValueValidator(0)], null=True, default=0)
    actualDeposit = models.CharField(max_length=120, default=0, blank=False)
    sign = models.CharField(max_length=120, default=Unconfirmed, blank=False, choices=sign)
    hashid = models.CharField(max_length=120, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def save(self, *args, **kwargs):
        if self.hashid is None or self.hashid == "":
            self.hashid = code_generator()
            super(OKPayBalanceDeposit, self).save(*args, **kwargs)

class PayeerBalanceDeposit(models.Model):
    user = models.CharField(max_length=125, blank=False, null=True)
    username = models.CharField(max_length=125, blank=False, null=True)
    processor = models.CharField(max_length=125, blank=False, null=True)
    m_amount = models.FloatField(blank=False, null=True, validators=[MinValueValidator(0)], default=0)
    actualDeposit = models.CharField(max_length=120, default=0, blank=False)
    sign = models.CharField(max_length=120, default=Unconfirmed, blank=False, choices=sign)
    hashid = models.CharField(max_length=120, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def save(self, *args, **kwargs):
        if self.hashid is None or self.hashid == "":
            self.hashid = code_generator()
            super(PayeerBalanceDeposit, self).save(*args, **kwargs)


class PerfectMoneyrBalanceDeposit(models.Model):
    user = models.CharField(max_length=125, blank=False, null=True)
    username = models.CharField(max_length=125, blank=False, null=True)
    processor = models.CharField(max_length=125, blank=False, null=True)
    p_amount = models.FloatField(blank=False, validators=[MinValueValidator(0)], null=True, default=0)
    actualDeposit = models.CharField(max_length=120, default=0, blank=False)
    sign = models.CharField(max_length=120, default=Unconfirmed, blank=False, choices=sign)
    hashid = models.CharField(max_length=120, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def save(self, *args, **kwargs):
        if self.hashid is None or self.hashid == "":
            self.hashid = code_generator()
            super(PerfectMoneyrBalanceDeposit, self).save(*args, **kwargs)



class BitcoinWithdrawModel(models.Model):
    user = models.CharField(max_length=120, blank=False, null=True)
    full_name = models.CharField(max_length=120, blank=False, null=True)
    balance = models.CharField(max_length=120, blank=False, null=True)
    processor = models.CharField(max_length=120, blank=False, null=True)
    processor_acc_number = models.CharField(max_length=120, blank=False, null=True)
    b_amount = models.PositiveIntegerField(blank=False, null=True)
    account_number = models.CharField(max_length=120, blank=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    email = models.CharField(max_length=120, blank=False, null=True)
    status = models.CharField(max_length=15, null=True, blank=True)



def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs['created']:
        user_profile = UserInfo(user=user)
        user_profile.save()
        invest = Investment(user=user)
        invest.save()

        cash = Deposits(user=user)
        cash.save()

        Stats = Statistics(user='xampesa')
        Stats.save()

        processor = Processors(user=user)
        processor.save()

post_save.connect(create_profile, sender=User)