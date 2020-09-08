from django import forms
from .models import *
from app.models import *
from io import StringIO
from PIL import Image
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime


class AlbumForm(forms.ModelForm):
    Full_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Full name', 'style': 'width: 100%;'}))
    country = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'country', 'style': 'width: 100%'}))
    currently_location = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'currently location', 'style': 'width: 100%'}))

    class Meta:
        model = Album
        fields = [
            'Full_name',
            'country',
            'currently_location'
        ]


class BuyingForm(forms.ModelForm):
    user = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'user', 'style': 'width: 100%;', 'class':"textinput textInput form-control " }))
    quantity = forms.IntegerField(label='', min_value=1, widget=forms.TextInput(attrs={'placeholder': 'Quantity', 'style': 'width: 100%;', "type":"number", 'class':'textinput textInput form-control ' }))
    # date_of_delivery = forms.DateField(label='', widget=forms.DateInput(attrs={'placeholder': 'date of delivery', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    name_of_receiver = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'name of receiver', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    country = forms.ChoiceField(choices=COUNTRIES, label="", initial='', widget=forms.Select(attrs={'placeholder': 'country', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    Region = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Region', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    Street = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Street', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    processor = forms.ChoiceField(choices=ACCOUNT_TYPE_CHOICES, label="", initial='', widget=forms.Select(attrs={'placeholder': '', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    phone_no = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Phone number', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))

    class Meta:
        model = Purchases
        fields = [
            'userid',
            'user',
            'product_id',
            'product_title',
            'product_owner',
            'quantity',
            'name_of_receiver',
            'country',
            'currency',
            'Price_sold',
            'Price',
            'Region',
            'Street',
            'processor',
            'phone_no',
            'Receive_acc',
            'buyers_acc',

        ]

class ReturnedPurchaseForm(forms.ModelForm):
    class Meta:
        model = ReturnedPurchases
        fields = [
            'userid',
            'sellers_name',
            'product_id',
            'product_title',
            'product_owner',
            'quantity',
            'buyers_name',
            'country',
            'currency',
            'Price_sold',
            'Price',
            'Region',
            'Street',
            'processor',
            'phone_no',
            'Receive_acc',

        ]

class FinnishedForm(forms.ModelForm):
    class Meta:
        model = FinishedTransactions
        fields = [
            'userid',
            'user',
            'product_id',
            'purchase_id',
            'product_title',
            'product_owner',
            'quantity',
            'name_of_receiver',
            'country',
            'currency',
            'Price_sold',
            'Price',
            'Region',
            'Street',
            'processor',
            'phone_no',
            'Receive_acc',
            'status'

        ]

class PrepurchaseForm(forms.ModelForm):
    class Meta:
        model = Prepurchase
        fields = [
            'userid',
            'user',
            'product_id',
            'product_title',
            'product_owner',
            'quantity',
            'name_of_receiver',
            'country',
            'currency',
            'Price_sold',
            'Price',
            'Region',
            'Street',
            'processor',
            'phone_no',
            'Receive_acc',

        ]

    # def clean_date_of_delivery(self):
    #     date_of_delivery =self.cleaned_data.get("date_of_delivery")
    #
    #     if date_of_delivery < (datetime.date.today()):
    #         raise forms.ValidationError(('Invalid date'))


class ProductsForm(forms.ModelForm):
    CHOICES = (('1', 'First',), ('2', 'Second',))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'username', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    # album = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'album', 'style': 'width: 100%;'}))
    category = forms.ChoiceField(choices=types, label="", initial='', widget=forms.Select(attrs={'placeholder': '', 'style': 'width: 100%; padding-bottom: 3%', 'class':'textinput textInput form-control '}), required=True)
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'title', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    color = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'color', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    currency = forms.ChoiceField(choices=all_types, label="", initial='', widget=forms.Select(attrs={'placeholder': 'currency', 'style': 'width: 100%', 'class':'textinput textInput form-control '}), required=True)
    Price = forms.FloatField(label='', min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Price', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    stock_products = forms.IntegerField(label='', min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Available products', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    condition = forms.ChoiceField(choices=condition, label="", initial='', widget=forms.Select(attrs={'placeholder': 'condition', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'descriptions.. split items by comma(,)', 'style': 'width: 100%', 'class':'textinput text-center textInput form-control '}))
    image  = forms.ImageField(label='', widget=forms.FileInput(attrs={'type':'file', 'name':'image',  'class':'clearablefileinput', 'style': 'width: 100%'}), required=True,)
    image1 = forms.ImageField(label='', widget=forms.FileInput(attrs={'type':'file', 'name':'image1', 'class':'clearablefileinput', 'style': 'width: 100%'}), required=True)
    image2 = forms.ImageField(label='', widget=forms.FileInput(attrs={'type':'file', 'name':'image2', 'class':'clearablefileinput', 'style': 'width: 100%'}))
    image3 = forms.ImageField(label='', widget=forms.FileInput(attrs={'type':'file', 'name':'image3', 'class':'clearablefileinput', 'style': 'width: 100%'}))
    image4 = forms.ImageField(label='', widget=forms.FileInput(attrs={'type':'file', 'name':'image4', 'class':'clearablefileinput', 'style': 'width: 100%'}))
    image5 = forms.ImageField(label='', widget=forms.FileInput(attrs={'type':'file', 'name':'image5', 'class':'clearablefileinput', 'style': 'width: 100%'}))

    class Meta:
        model = Products
        fields = [
            'username',
            'category',
            'title',
            'currency',
            'Price',
            'condition',
            'stock_products',
            'color',
            'image',
            'image1',
            'image2',
            'image3',
            'image4',
            'image5',
            'Receive_acc',
            'description',

        ]

class PriceProductsForm(forms.ModelForm):
    CHOICES = (('1', 'First',), ('2', 'Second',))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'username', 'style': 'width: 100%'}))
    # album = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'album', 'style': 'width: 100%;'}))
    category = forms.ChoiceField(choices=types, label="", initial='', widget=forms.Select(attrs={'placeholder': '', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'title', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    color = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'color', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    Youremail = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your email', 'style': 'width: 100%'}))
    Phone_numbers = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Phone numbers', 'style': 'width: 100%'}))
    currency = forms.ChoiceField(label='', choices=all_types, widget=forms.Select(attrs={'placeholder': 'currency', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    AdsPackage = forms.ChoiceField(label='', choices=Adspack, widget=forms.Select(attrs={'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    Price = forms.IntegerField(label='', min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Price', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    stock_products = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'placeholder': 'Available products', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    condition = forms.ChoiceField(label='', choices=condition, widget=forms.Select(attrs={'placeholder': 'position type', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'descriptions.. split items by comma(,)', 'style': 'width: 100%', 'class':'textinput text-center textInput form-control '}))
    image  = forms.ImageField(label='', widget=forms.FileInput(attrs={'type':'file', 'name':'image',  'class':'clearablefileinput', 'style': 'width: 100%'}), required=True)
    image1 = forms.ImageField(label='', widget=forms.FileInput(attrs={'type':'file', 'name':'image1', 'class':'clearablefileinput', 'style': 'width: 100%'}), required=True)
    image2 = forms.ImageField(label='', widget=forms.FileInput(attrs={'type':'file', 'name':'image2', 'class':'clearablefileinput', 'style': 'width: 100%'}))
    image3 = forms.ImageField(label='', widget=forms.FileInput(attrs={'type':'file', 'name':'image3', 'class':'clearablefileinput', 'style': 'width: 100%'}))
    image4 = forms.ImageField(label='', widget=forms.FileInput(attrs={'type':'file', 'name':'image4', 'class':'clearablefileinput', 'style': 'width: 100%'}))
    image5 = forms.ImageField(label='', widget=forms.FileInput(attrs={'type':'file', 'name':'image5', 'class':'clearablefileinput', 'style': 'width: 100%'}))

    class Meta:
        model = PaidProducts
        fields = [
            'username',
            'category',
            'title',
            'country',
            'currency',
            'Price',
            'condition',
            'Youremail',
            'Phone_numbers',
            'AdsPackage',
            'stock_products',
            'color',
            'image',
            'image1',
            'image2',
            'image3',
            'image4',
            'image5',
            'Receive_acc',
            'description',

        ]

    # def imageclean(self):
    #     image = self.cleaned_data.get('image')
    #     image_file = StringIO.StringIO(image.read())
    #     imag = Image.open(image_file)
    #     w, h =imag.size
    #
    #     imag = imag.resize((w/2, h/2), Image.ANTIALIAS)
    #
    #     image_file = StringIO.StringIO()
    #     imag.save(image_file, 'JPEG', quality=90)
    #     image.file = image_file

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = [
            'prod_id',
            'username',
            'category',
            'title',
            'currency',
            'Price',
            'Price_sold',
            'condition',
            'color',
            'image',
            'image1',
            'image2',
            'image3',
            'image4',
            'image5',
            'Receive_acc',
            'description',

        ]


class CreditCardForm(forms.ModelForm):
    user_id = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 100%; padding-bottom: 100%;'}))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width: 100%; padding-bottom: 100%'}))
    # products = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Products', 'style': 'width: 100%; padding-bottom: 3%'}))
    Card_holder_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Card holder', 'style': 'width: 100%; padding-bottom: 3%'}))
    Card_number = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Card number', 'style': 'width: 100%; padding-bottom: 3%'}))
    Passport_id = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Identity number', 'style': 'width: 100%; padding-bottom: 3%'}))
    Expirity_month = forms.ChoiceField(choices = MONTH, label="", initial='', widget=forms.Select(attrs={'placeholder': '-', 'style': 'width: 100%; padding-bottom: 3%' }), required=True)
    Expirity_year = forms.ChoiceField(choices = YEAR, label="", initial='', widget=forms.Select(attrs={'placeholder': '-', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    Security_code_CVV = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'CVV', 'style': 'width: 100%; padding-bottom: 3%'}))

    class Meta:
        model = CreditCard
        fields = [

            "user_id",
            "username",
            # "products",
            "Card_holder_name",
            "Card_number",
            "Passport_id",
            "Expirity_month",
            "Expirity_year",
            "Security_code_CVV"
        ]
#
#
# class PurchasesForm(forms.ModelForm):
#     class Meta:
#         model = Purchases
#         fields = ["name_of_receiver",
#                   "quantity",
#                   "date_of_delivery",
#                   "place_of_delivery",
#                   "phone_no"
#                   ]


class MpesaForm(forms.ModelForm):
    # user_id = forms.CharField(label='', widget=forms.TextInput(
    #     attrs={'placeholder': '', 'style': 'width: 100%; padding-bottom: 100%;'}))
    # order_no = forms.CharField(label='', widget=forms.TextInput(
    #     attrs={'placeholder': 'order number', 'style': 'width: 100%; padding-bottom: 100%'}))
    # products = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Products', 'style': 'width: 100%; padding-bottom: 3%'}))
    username = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'username', 'style': 'width: 100%; padding-bottom: 3%'}))
    mpesa_Name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Mpesa name', 'style': 'width: 100%; padding-bottom: 3%'}))
    phone_no = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Mpesa number', 'style': 'width: 100%; padding-bottom: 3%'}))
    amount_sent = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'amount', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    kumbukumbu_no = forms.CharField(label="", widget=forms.TextInput(
        attrs={'placeholder': 'kumbukumbu number', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    Account_balance = forms.CharField(label='', widget=forms.TextInput(
        attrs={'placeholder': 'Account balance', 'style': 'width: 100%; padding-bottom: 3%'}))
    class Meta:
        model = Mpesa
        fields = [
            "Account_balance",
            # "order_no",
            "username",
            "mpesa_Name",
            "phone_no",
            "amount_sent",
            "kumbukumbu_no"
        ]




class AuthorInterestForm(forms.Form):
    message = forms.CharField()


