from django.db import models
from django.contrib.auth.models import User

from PIL import Image
from django.db.models.signals import post_save
from datetime import datetime, timedelta
from django.utils import timezone
from app.models import *
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.messages.views import messages
from django.core.validators import RegexValidator
import re
import random, string

officeschool = 'office & school supply'
hairextensions = "Hair extension's & wigs"
securityprotection = 'Security & protection'
electronicsupply = 'Electronics & supplies'
computers = 'Computers & office'
furnitures = "Furniture's"
lightslighting = 'Lights & Lighting'
automobilesmotorcycles = 'Automobiles & motorcycles'
weddingsevents = 'Wedding & events'
toyshobbies = 'Toys and Hobbies'
consumerelectronics = 'Consumer Electronics'
homegarden = 'Home & garden'
bagsluggage = 'Bags & Luggage'
menclothes = 'Men clothes & accessories'
womenclothes = 'Women clothes & accessories'
Aceassories = 'Phones & accessories'
Beauty = 'Health & Beauty'
Clothing = 'Clothing'
jewery = 'jewery & watches'
Home = 'Home improvement'
Shoes = ' shoes'
Sport = 'Sports & Outdoors'
others = 'others'
types = (
    (computers, 'Computers & office'),
    (officeschool, 'office & school supplys'),
    (hairextensions, "Hair extension's & wigs"),
    (Aceassories, "office & school supply"),
    (securityprotection, 'Security & protection'),
    (electronicsupply, 'Electronics & supplies'),
    (furnitures, "Furniture's"),
    (lightslighting, 'Lights & Lighting'),
    (automobilesmotorcycles, 'Automobiles & motorcycles'),
    (weddingsevents, 'Wedding & events'),
    (toyshobbies, 'Toys and Hobbies'),
    (homegarden, 'Home & garden'),
    (bagsluggage, 'Bags & Luggage'),
    (menclothes, 'Men clothes & accessories'),
    (womenclothes, 'Women clothes & accessories'),
    (Aceassories, 'Phones & accessories'),
    (Beauty, 'Health & Beauty'),
    (jewery, 'Clothing'),
    (Home, 'jewelry & watches'),
    (Shoes, 'Home improvement'),
    (Sport, 'Sports & Outdoors'),
    (others, 'others'),
)

class Album(models.Model):
    user = models.OneToOneField(User, null=True)
    Full_name = models.CharField(max_length=250, blank=False)
    currently_location =models.CharField(max_length=30, null=True, blank=False)
    country = models.CharField(max_length=25, blank=False, default='')

    def __str__(self):
        return self.Full_name

Usd = '$'
Bitcoin = 'BTC'
all_types = (
    (Usd, '$'),
    (Bitcoin, 'BTC'))


New = 'New'
Used = 'Used'
condition = (
    (New, 'New'),
    (Used, 'Used'))



class Products(models.Model):
    username = models.CharField(max_length=120, blank=False, null=True)
    category = models.CharField(max_length=120, blank=False, null=False, choices=types)
    country = models.CharField(max_length=120, blank=False, null=True)
    stock_products = models.PositiveIntegerField(blank=False, null=True)
    title = models.CharField(max_length=120, blank=False, null=True)
    currency = models.CharField(max_length=120, null=True, blank=False, choices=all_types)
    color = models.CharField(max_length=125, blank=True, null=True)
    image = models.ImageField(null=False, blank=False)
    image1 = models.ImageField(null=True, blank=False)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)
    description = models.TextField()
    currency_used = models.CharField(blank=True, null=True, max_length=120)
    Price = models.FloatField(null=False, blank=False, default='')
    Price_sold = models.FloatField(null=True, blank=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    condition = models.CharField(max_length=120, blank=False, choices=condition, null=True)
    Receive_acc = models.CharField(max_length=120, blank=False, null=True)

    def save(self, *args, **kwargs):
        if self.currency_used is None or self.currency_used == "":
            if self.currency == '$':
                print(self.currency)
                self.currency_used = 'usd'
            elif self.currency == 'BTC':
                self.currency_used = 'Bitcoin'
        super(Products, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('market:product-edit', kwargs={"pk": self.pk})

    def water(self):
        return reverse('market:Products', kwargs={"pk": self.pk})

    def secured(self):
        return reverse('market:secured', kwargs={"pk": self.pk})



    class Meta:
        verbose_name_plural = "Products in the Market"
        ordering = ['-timestamp']

    def __str__(self):
        return str(self.id)

    def get_description(self):
        return self.description.split(",")

# Usd = '$'
# Bitcoin = 'BTC'
# all_types = (
#     (Usd, '$'),
#     (Bitcoin, 'BTC'))


Month4Weeks2 = '3 Month 2 Weeks'
Month4 = 'Month4'
Month3Weeks2 = '3 Month 2 Weeks'
Month3 = '3 Months'
Month2Weeks2 = '2 Month 2 Weeks'
Month2 = '2 Months'
Month1Weeks2 = '1 Month 2 Weeks'
Month1 = '1 Month'
Weeks3 = '3 Weeks'
Weeks2 = '2 Weeks'
Week1 = '1 Week'
Adspack = (
    (Week1, '1 Week'),
    (Weeks2, '2 Weeks'),
    (Weeks3, '3 Weeks'),
    (Month1, '1 Month'),
    (Month1Weeks2, '1 Month 2 Weeks'),
    (Month2, '2 Months'),
    (Month2Weeks2, '2 Month 2 Weeks'),
    (Month3, '3 Months'),
    (Month3Weeks2, '3 Month 2 Weeks'),
    (Month4, '4 Months'),
    (Month4Weeks2, '3 Month 2 Weeks'))

class PaidProducts(models.Model):
    username = models.CharField(max_length=120, blank=False, null=True)
    category = models.CharField(max_length=120, blank=False, null=False, choices=types)
    country = models.CharField(max_length=120, blank=False, null=True)
    stock_products = models.PositiveIntegerField(blank=False, null=True)
    title = models.CharField(max_length=120, blank=False, null=True)
    currency = models.CharField(max_length=5, choices=all_types, default=Usd)
    color = models.CharField(max_length=125, blank=True, null=True)
    Youremail = models.CharField(max_length=125, blank=True, null=True)
    Phone_numbers = models.CharField(max_length=125, blank=True, null=True)
    AdsPackage = models.CharField(max_length=125, blank=True, null=True, choices=Adspack)
    image = models.ImageField(null=False, blank=False)
    image1 = models.ImageField(null=True, blank=False)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)
    description = models.TextField()
    Price = models.FloatField(null=False, blank=False, default='')
    Price_sold = models.CharField(max_length=12, null=True, blank=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    condition = models.CharField(max_length=120, blank=False, null=True)
    Receive_acc = models.CharField(max_length=120, blank=False, null=True)

    def get_absolute_url(self):
        return reverse('market:product-edit', kwargs={"pk": self.pk})

    def water(self):
        return reverse('market:Products', kwargs={"pk": self.pk})

    def secured(self):
        return reverse('market:secured', kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "Paid Products in the Market"
        ordering = ['-timestamp']

    def __str__(self):
        return str(self.id)

    def get_description(self):
        return self.description.split(",")


class Cart(models.Model):
    prod_id = models.CharField(max_length=120, blank=False, null=True)
    username = models.CharField(max_length=120, blank=False, null=True)
    category = models.CharField(max_length=120, blank=False, null=False, choices=types)
    country = models.CharField(max_length=120, blank=False, null=True)
    title = models.CharField(max_length=120, blank=False, null=True)
    currency = models.CharField(max_length=5, choices=all_types, default=Usd)
    color = models.CharField(max_length=120, blank=True, null=True)
    image = models.CharField(max_length=120, null=False, blank=False)
    image1 = models.CharField(max_length=120, null=True, blank=False)
    image2 = models.CharField(max_length=120, null=True, blank=True)
    image3 = models.CharField(max_length=120, null=True, blank=True)
    image4 = models.CharField(max_length=120, null=True, blank=True)
    image5 = models.CharField(max_length=120, null=True, blank=True)
    description = models.CharField(max_length=400, null=False, blank=False, default='')
    Price = models.CharField( max_length=12, null=False, blank=False, default='')
    Price_sold = models.CharField(max_length=12, null=True, blank=False)
    condition = models.CharField(max_length=120, blank=False, null=True)
    Receive_acc = models.CharField(max_length=120, blank=False, null=True)

    def __str__(self):
        return str(self.username)

MONTH = ((' ', ' '), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
         ('9', '9'), ('10','10'), ('11','11'), ('12', '12'))
YEAR = ((' ', ' '), ('1987', '1987'), ('1988', '1988'), ('1990', '1990'), ('1991', '1991'), ('1992', '1992'),
        ('1993', "1993"), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'),
        ('1999', '1999'), ('2000', '2000'))


class CreditCard(models.Model):
    user_id = models.CharField(max_length=4, blank=False, null=True)
    username = models.CharField(max_length=35, blank=False, null=True)
    products = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    Card_holder_name = models.CharField(max_length=120, blank=False, null=True)
    Card_number = models.CharField(max_length=14, blank=False, null=True)
    Passport_id = models.CharField(max_length=7, blank=False, null=True)
    Expirity_month = models.IntegerField(blank=False, null=True)
    Expirity_year = models.IntegerField(blank=False, null=True)
    Security_code_CVV = models.CharField(max_length=8, blank=False, null=False)

    def __str__(self):
        return self.Card_holder_name

    # class CreditCardNumber(models.TextField):

    def clean(self):
        return re.sub(r'\D', '', str(self))

Account_balance = 'Account balance'
Perfectmoney = 'Perfectmoney'
Payeer = 'Payeer'
Bitcoin = 'Bitcoin'
ACCOUNT_TYPE_CHOICES = (
    (Account_balance, 'Account balance'),
    (Perfectmoney, 'Perfectmoney'),
    (Payeer, 'Payeer'),
    (Bitcoin, 'Bitcoin'),

    )

received = 'Received'
not_received = 'Not received'
canceled = 'canceled'
choic = (

    (received, 'Received'),
    (not_received, 'Not received'),
    (canceled, 'canceled'))


def code_generator(size=18, chars=string.ascii_lowercase + string.digits ):
    new_code = ''
    for _ in range(size):
        new_code += random.choice(chars)
    return new_code

Delayed = 'Delayed (Canceled)'
Sent = 'On the way'
waiting = 'Waiting'
customer_status = (
    (Delayed, 'Delayed (Canceled)'),
    (Sent, 'On the way'),
    (waiting, 'Waiting'))


Uncompleted = 'Uncompleted'
completed = 'completed'
waiting = 'Waiting'
comp = (
    (Uncompleted, 'Uncompleted'),
    (completed, 'completed'))


Delayed = 'Delayed (Canceled)'
Sent = 'On the way'
Progressing = 'Order is processing'
seller_status = (
    (Delayed, 'Delayed (Canceled)'),
    (Sent, 'On the way'),
    (Progressing, 'Order is processing'))

Going = 'on going'
Cancelled = 'Cancelled'
actions = (
    (Going, 'on going'),
    (Cancelled, 'Cancelled'),
  )


class Purchases(models.Model):
    MEDIA_CHOICES = (
        ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
         ),
        ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
         ),
        ('unknown', 'Unknown'),
    )

    userid = models.CharField(max_length=13, null=True)
    user = models.CharField(max_length=120, null=True)
    Price_sold = models.FloatField(blank=False, null=True)
    Price = models.FloatField(blank=False, null=True)
    product_id = models.CharField(blank=False, null=True, max_length=120)
    product_title = models.CharField(blank=False, null=True, max_length=120)
    quantity = models.PositiveIntegerField(blank=False, null=True, default=10)
    currency = models.CharField(blank=False, null=True, max_length=120)
    product_owner = models.CharField(blank=False, null=True, max_length=120)
    name_of_receiver = models.CharField(max_length=120, blank=False, null=True)
    country = models.CharField(max_length=120, blank=False, choices=COUNTRIES, null=True)
    Region = models.CharField(max_length=120, blank=False, null=True)
    orderdate = models.DateTimeField(null=True, blank=True)
    currency_used = models.CharField(blank=False, null=True, max_length=120)
    lastdate = models.DateTimeField(null=True, blank=True)
    Street = models.CharField(max_length=120, blank=False, null=True)
    processor = models.CharField(max_length=128, blank=False, default=not_received, choices=ACCOUNT_TYPE_CHOICES)
    # Country_code = models.CharField(max_length=10, blank=False, null=True,
    #                                 error_messages={'incomplete': 'Enter a phone number.'},
    #                                 validators=[RegexValidator(r'^[+0-9]+$', 'Enter a valid code number.')],)

    phone_no = models.CharField(max_length=120, blank=False, null=True)
    order_actions = models.CharField(max_length=120, blank=True, choices=actions, default='on going')
    Receive_acc = models.CharField(max_length=120, blank=False, null=True)
    buyers_acc = models.CharField(max_length=120, blank=False, null=True)
    status= models.CharField(max_length=120, blank=False, default=not_received, choices=choic)
    customers_status= models.CharField(max_length=120, blank=False, default=waiting, choices=customer_status)
    sellers_status= models.CharField(max_length=120, blank=False, default=Progressing, choices=seller_status)
    shortcode = models.CharField(max_length=120, unique=True, null=True)
    complete = models.CharField(max_length=120, blank=False, choices=comp, default=Uncompleted)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if self.lastdate is None or self.lastdate == "":
            self.lastdate = timezone.now() + timedelta(days=10)
            self.orderdate = timezone.now()
            if self.currency == Usd:
                self.currency_used = 'usd'
            elif self.currency == Bitcoin:
                self.currency_used = 'Bitcoin'
            if self.shortcode is None or self.shortcode == "":
                self.shortcode = code_generator()
        super(Purchases, self).save(*args, **kwargs)



    class Meta:
        verbose_name_plural = "Purchases details:"


class ReturnedPurchases(models.Model):
    userid = models.CharField(max_length=120, blank=False, null=True)
    sellers_name = models.CharField(max_length=120, blank=False, null=True)
    Price_sold = models.FloatField(blank=False, null=True)
    Price = models.FloatField(blank=False, null=True)
    product_id = models.CharField(blank=False, null=True, max_length=120)
    product_title = models.CharField(blank=False, null=True, max_length=120)
    quantity = models.CharField(blank=False, null=True, max_length=120)
    currency = models.CharField(blank=False, null=True, max_length=120)
    product_owner = models.CharField(blank=False, null=True, max_length=120)
    buyers_name = models.CharField(max_length=120, blank=False, null=True)
    country = models.CharField(max_length=120, blank=False, null=True)
    Region = models.CharField(max_length=120, blank=False, null=True)
    orderdate = models.CharField(max_length=120, null=True, blank=True)
    Time_cancelled = models.DateTimeField(auto_now_add=True)
    lastdate = models.DateTimeField(null=True, blank=True)
    Street = models.CharField(max_length=120, blank=False, null=True)
    processor = models.CharField(blank=False, null=True, max_length=120)
    phone_no = models.CharField(max_length=120, blank=False, null=True)
    order_actions = models.CharField(blank=False, null=True, max_length=120)
    Receive_acc = models.CharField(max_length=120, blank=False, null=True)
    status = models.CharField(blank=False, null=True, max_length=120)
    customers_status = models.CharField(blank=False, null=True, max_length=120)
    sellers_status = models.CharField(blank=False, null=True, max_length=120)
    shortcode = models.CharField(blank=False, null=True, max_length=120)

    def __str__(self):
        return str(self.sellers_name)

    class Meta:
        verbose_name_plural = "Returned Purchases"




class FinishedTransactions(models.Model):
    userid = models.CharField(max_length=120, null=True)
    user = models.CharField(max_length=120, null=True)
    Price_sold = models.FloatField( blank=False, null=True)
    Price = models.FloatField(blank=False, null=True)
    product_id = models.CharField(blank=False, null=True, max_length=120)
    purchase_id = models.CharField(blank=False, null=True, max_length=120)
    product_title = models.CharField(blank=False, null=True, max_length=120)
    quantity = models.CharField(max_length=120, blank=False, null=True)
    currency = models.CharField(blank=False, null=True, max_length=120)
    product_owner = models.CharField(blank=False, null=True, max_length=120)
    name_of_receiver = models.CharField(max_length=120, blank=False, null=True)
    country = models.CharField(max_length=120, blank=False, null=True)
    Region = models.CharField(max_length=120, blank=False, null=True)
    # orderdate = models.CharField(max_length=120, blank=False, null=True)
    # lastdate = models.CharField(max_length=120, blank=False, null=True)
    Street = models.CharField(max_length=120, blank=False, null=True)
    processor = models.CharField(max_length=128, blank=False, null=True)
    phone_no = models.CharField(max_length=120, blank=False, null=True)
    Receive_acc = models.CharField(max_length=120, blank=False, null=True)
    status= models.CharField(max_length=120, blank=False, default="unprocessed" )

    def __str__(self):
        return str(self.user)


class Mpesa(models.Model):
    Account_balance = models.CharField(max_length=12, blank=False, null=False)
    order_no = models.CharField(max_length=120, blank=False, null=False)
    username = models.CharField(max_length=120, blank=False, null=False)
    mpesa_Name = models.CharField(max_length=120, blank=False, null=False)
    phone_no = models.IntegerField(blank=False, null=False)
    amount_sent = models.CharField(max_length=25, blank=False, null=False)
    kumbukumbu_no = models.CharField(max_length=125, blank=False, null=False)
    Admin_kumbukumbu_no = models.CharField(max_length=125, blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True, auto_now=False, null=False)

    class Meta:
        verbose_name_plural = "Mpesa transactions"






class Prepurchase(models.Model):
    userid = models.CharField(max_length=13, null=True)
    user = models.CharField(max_length=120, null=True)
    Price_sold = models.FloatField(blank=False, null=True)
    Price = models.FloatField(blank=False, null=True)
    product_id = models.CharField(blank=False, null=True, max_length=120)
    purchase_id = models.CharField(blank=False, null=True, max_length=120)
    product_title = models.CharField(blank=False, null=True, max_length=120)
    quantity = models.PositiveIntegerField(blank=False, null=True, default=10)
    shortcode = models.CharField(max_length=120, blank=True, null=True, default=10)
    currency = models.CharField(blank=False, null=True, max_length=120)
    product_owner = models.CharField(blank=False, null=True, max_length=120)
    name_of_receiver = models.CharField(max_length=120, blank=False, null=True)
    country = models.CharField(max_length=120, blank=False, null=True)
    Region = models.CharField(max_length=120, blank=False, null=True)
    orderdate = models.CharField(blank=False, null=True, max_length=120)
    lastdate = models.CharField(blank=False, null=True, max_length=120)
    Street = models.CharField(max_length=120, blank=False, null=True)
    processor = models.CharField(max_length=128, blank=False, default=not_received, choices=ACCOUNT_TYPE_CHOICES)
    phone_no = models.CharField(max_length=120, blank=False, null=True)
    Receive_acc = models.CharField(max_length=120, blank=False, null=True)
    status = models.CharField(max_length=120, blank=False, null=True )
    veried = models.CharField(max_length=120, blank=False, null=True)


            #
# instance = Products(album=album)
# def create_profile(sender, **kwargs):
#     user = kwargs["instance"]
#     if kwargs['created']:
#         user_profile = Album(user=user)
#         user_profile.save()
#         fob = Products(id=id)
#         fob.save()
#         production = Purchases(user=user)
#         production.save()
#         production = Purchases(user=user)
#         production.save()
#
#
# post_save.connect(create_profile, sender=User)