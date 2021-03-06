# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-23 18:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=250)),
                ('currently_location', models.CharField(max_length=30, null=True)),
                ('country', models.CharField(default='', max_length=25)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_id', models.CharField(max_length=120, null=True)),
                ('username', models.CharField(max_length=120, null=True)),
                ('category', models.CharField(choices=[('Computers & office', 'Computers & office'), ('office & school supply', 'office & school supplys'), ("Hair extension's & wigs", "Hair extension's & wigs"), ('Phones & accessories', 'office & school supply'), ('Security & protection', 'Security & protection'), ('Electronics & supplies', 'Electronics & supplies'), ("Furniture's", "Furniture's"), ('Lights & Lighting', 'Lights & Lighting'), ('Automobiles & motorcycles', 'Automobiles & motorcycles'), ('Wedding & events', 'Wedding & events'), ('Toys and Hobbies', 'Toys and Hobbies'), ('Home & garden', 'Home & garden'), ('Bags & Luggage', 'Bags & Luggage'), ('Men clothes & accessories', 'Men clothes & accessories'), ('Women clothes & accessories', 'Women clothes & accessories'), ('Phones & accessories', 'Phones & accessories'), ('Health & Beauty', 'Health & Beauty'), ('jewery & watches', 'Clothing'), ('Home improvement', 'jewelry & watches'), (' shoes', 'Home improvement'), ('Sports & Outdoors', 'Sports & Outdoors'), ('others', 'others')], max_length=120)),
                ('country', models.CharField(max_length=120, null=True)),
                ('title', models.CharField(max_length=120, null=True)),
                ('currency', models.CharField(choices=[('$', '$'), ('tsh', 'tsh'), ('ksh', 'ksh'), ('BTC', 'BTC')], default='tsh', max_length=5)),
                ('color', models.CharField(blank=True, max_length=120, null=True)),
                ('image', models.CharField(max_length=120)),
                ('image1', models.CharField(max_length=120, null=True)),
                ('image2', models.CharField(blank=True, max_length=120, null=True)),
                ('image3', models.CharField(blank=True, max_length=120, null=True)),
                ('image4', models.CharField(blank=True, max_length=120, null=True)),
                ('image5', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.CharField(default='', max_length=400)),
                ('Price', models.CharField(default='', max_length=12)),
                ('Price_sold', models.CharField(max_length=12, null=True)),
                ('condition', models.CharField(max_length=120, null=True)),
                ('Receive_acc', models.CharField(max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=4, null=True)),
                ('username', models.CharField(max_length=35, null=True)),
                ('Card_holder_name', models.CharField(max_length=120, null=True)),
                ('Card_number', models.CharField(max_length=14, null=True)),
                ('Passport_id', models.CharField(max_length=7, null=True)),
                ('Expirity_month', models.IntegerField(null=True)),
                ('Expirity_year', models.IntegerField(null=True)),
                ('Security_code_CVV', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='FinishedTransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=120, null=True)),
                ('user', models.CharField(max_length=120, null=True)),
                ('Price_sold', models.FloatField(null=True)),
                ('Price', models.FloatField(null=True)),
                ('product_id', models.CharField(max_length=120, null=True)),
                ('purchase_id', models.CharField(max_length=120, null=True)),
                ('product_title', models.CharField(max_length=120, null=True)),
                ('quantity', models.CharField(max_length=120, null=True)),
                ('currency', models.CharField(max_length=120, null=True)),
                ('product_owner', models.CharField(max_length=120, null=True)),
                ('name_of_receiver', models.CharField(max_length=120, null=True)),
                ('country', models.CharField(max_length=120, null=True)),
                ('Region', models.CharField(max_length=120, null=True)),
                ('Street', models.CharField(max_length=120, null=True)),
                ('processor', models.CharField(max_length=128, null=True)),
                ('phone_no', models.CharField(max_length=120, null=True)),
                ('Receive_acc', models.CharField(max_length=120, null=True)),
                ('status', models.CharField(default='unprocessed', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Mpesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_balance', models.CharField(max_length=12)),
                ('order_no', models.CharField(max_length=120)),
                ('username', models.CharField(max_length=120)),
                ('mpesa_Name', models.CharField(max_length=120)),
                ('phone_no', models.IntegerField()),
                ('amount_sent', models.CharField(max_length=25)),
                ('kumbukumbu_no', models.CharField(max_length=125)),
                ('Admin_kumbukumbu_no', models.CharField(blank=True, max_length=125, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Mpesa transactions',
            },
        ),
        migrations.CreateModel(
            name='PaidProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120, null=True)),
                ('category', models.CharField(choices=[('Computers & office', 'Computers & office'), ('office & school supply', 'office & school supplys'), ("Hair extension's & wigs", "Hair extension's & wigs"), ('Phones & accessories', 'office & school supply'), ('Security & protection', 'Security & protection'), ('Electronics & supplies', 'Electronics & supplies'), ("Furniture's", "Furniture's"), ('Lights & Lighting', 'Lights & Lighting'), ('Automobiles & motorcycles', 'Automobiles & motorcycles'), ('Wedding & events', 'Wedding & events'), ('Toys and Hobbies', 'Toys and Hobbies'), ('Home & garden', 'Home & garden'), ('Bags & Luggage', 'Bags & Luggage'), ('Men clothes & accessories', 'Men clothes & accessories'), ('Women clothes & accessories', 'Women clothes & accessories'), ('Phones & accessories', 'Phones & accessories'), ('Health & Beauty', 'Health & Beauty'), ('jewery & watches', 'Clothing'), ('Home improvement', 'jewelry & watches'), (' shoes', 'Home improvement'), ('Sports & Outdoors', 'Sports & Outdoors'), ('others', 'others')], max_length=120)),
                ('country', models.CharField(max_length=120, null=True)),
                ('stock_products', models.PositiveIntegerField(null=True)),
                ('title', models.CharField(max_length=120, null=True)),
                ('currency', models.CharField(choices=[('$', '$'), ('tsh', 'tsh'), ('ksh', 'ksh'), ('BTC', 'BTC')], default='tsh', max_length=5)),
                ('color', models.CharField(blank=True, max_length=125, null=True)),
                ('Youremail', models.CharField(blank=True, max_length=125, null=True)),
                ('Phone_numbers', models.CharField(blank=True, max_length=125, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('image1', models.ImageField(null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField()),
                ('Price', models.CharField(default='', max_length=12)),
                ('Price_sold', models.CharField(max_length=12, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('condition', models.CharField(max_length=120, null=True)),
                ('Receive_acc', models.CharField(max_length=120, null=True)),
            ],
            options={
                'verbose_name_plural': 'Paid Products in the Market',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Prepurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=13, null=True)),
                ('user', models.CharField(max_length=120, null=True)),
                ('Price_sold', models.FloatField(null=True)),
                ('Price', models.FloatField(null=True)),
                ('product_id', models.CharField(max_length=120, null=True)),
                ('purchase_id', models.CharField(max_length=120, null=True)),
                ('product_title', models.CharField(max_length=120, null=True)),
                ('quantity', models.PositiveIntegerField(default=10, null=True)),
                ('shortcode', models.CharField(blank=True, default=10, max_length=120, null=True)),
                ('currency', models.CharField(max_length=120, null=True)),
                ('product_owner', models.CharField(max_length=120, null=True)),
                ('name_of_receiver', models.CharField(max_length=120, null=True)),
                ('country', models.CharField(max_length=120, null=True)),
                ('Region', models.CharField(max_length=120, null=True)),
                ('orderdate', models.CharField(max_length=120, null=True)),
                ('lastdate', models.CharField(max_length=120, null=True)),
                ('Street', models.CharField(max_length=120, null=True)),
                ('processor', models.CharField(choices=[('Account balance', 'Account balance'), ('tIGoPesa', 'tIGoPesa'), ('Mpesa', 'Mpesa'), ('AirtelMoney', 'AirtelMoney'), ('Bitcoin', 'Bitcoin')], default='Not received', max_length=128)),
                ('phone_no', models.CharField(max_length=120, null=True)),
                ('Receive_acc', models.CharField(max_length=120, null=True)),
                ('status', models.CharField(max_length=120, null=True)),
                ('veried', models.CharField(max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120, null=True)),
                ('category', models.CharField(choices=[('Computers & office', 'Computers & office'), ('office & school supply', 'office & school supplys'), ("Hair extension's & wigs", "Hair extension's & wigs"), ('Phones & accessories', 'office & school supply'), ('Security & protection', 'Security & protection'), ('Electronics & supplies', 'Electronics & supplies'), ("Furniture's", "Furniture's"), ('Lights & Lighting', 'Lights & Lighting'), ('Automobiles & motorcycles', 'Automobiles & motorcycles'), ('Wedding & events', 'Wedding & events'), ('Toys and Hobbies', 'Toys and Hobbies'), ('Home & garden', 'Home & garden'), ('Bags & Luggage', 'Bags & Luggage'), ('Men clothes & accessories', 'Men clothes & accessories'), ('Women clothes & accessories', 'Women clothes & accessories'), ('Phones & accessories', 'Phones & accessories'), ('Health & Beauty', 'Health & Beauty'), ('jewery & watches', 'Clothing'), ('Home improvement', 'jewelry & watches'), (' shoes', 'Home improvement'), ('Sports & Outdoors', 'Sports & Outdoors'), ('others', 'others')], max_length=120)),
                ('country', models.CharField(max_length=120, null=True)),
                ('stock_products', models.PositiveIntegerField(null=True)),
                ('title', models.CharField(max_length=120, null=True)),
                ('currency', models.CharField(choices=[('$', '$'), ('tsh', 'tsh'), ('ksh', 'ksh'), ('BTC', 'BTC')], default='tsh', max_length=5)),
                ('color', models.CharField(blank=True, max_length=125, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('image1', models.ImageField(null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField()),
                ('Price', models.CharField(default='', max_length=12)),
                ('Price_sold', models.CharField(max_length=12, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('condition', models.CharField(max_length=120, null=True)),
                ('Receive_acc', models.CharField(max_length=120, null=True)),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products in the Market',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=13, null=True)),
                ('user', models.CharField(max_length=120, null=True)),
                ('Price_sold', models.FloatField(null=True)),
                ('Price', models.FloatField(null=True)),
                ('product_id', models.CharField(max_length=120, null=True)),
                ('product_title', models.CharField(max_length=120, null=True)),
                ('quantity', models.PositiveIntegerField(default=10, null=True)),
                ('currency', models.CharField(max_length=120, null=True)),
                ('product_owner', models.CharField(max_length=120, null=True)),
                ('name_of_receiver', models.CharField(max_length=120, null=True)),
                ('country', models.CharField(max_length=120, null=True)),
                ('Region', models.CharField(max_length=120, null=True)),
                ('orderdate', models.DateTimeField(blank=True, null=True)),
                ('lastdate', models.DateTimeField(blank=True, null=True)),
                ('Street', models.CharField(max_length=120, null=True)),
                ('processor', models.CharField(choices=[('Account balance', 'Account balance'), ('tIGoPesa', 'tIGoPesa'), ('Mpesa', 'Mpesa'), ('AirtelMoney', 'AirtelMoney'), ('Bitcoin', 'Bitcoin')], default='Not received', max_length=128)),
                ('phone_no', models.CharField(max_length=120, null=True)),
                ('order_actions', models.CharField(blank=True, choices=[('on going', 'on going'), ('Cancelled', 'Cancelled')], default='on going', max_length=120)),
                ('Receive_acc', models.CharField(max_length=120, null=True)),
                ('status', models.CharField(choices=[('Received', 'Received'), ('Not received', 'Not received'), ('canceled', 'canceled')], default='Not received', max_length=120)),
                ('customers_status', models.CharField(choices=[('Delayed (Canceled)', 'Delayed (Canceled)'), ('On the way', 'On the way'), ('Waiting', 'Waiting')], default='Waiting', max_length=120)),
                ('sellers_status', models.CharField(choices=[('Delayed (Canceled)', 'Delayed (Canceled)'), ('On the way', 'On the way'), ('Order is processing', 'Order is processing')], default='Order is processing', max_length=120)),
                ('shortcode', models.CharField(max_length=120, null=True, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Purchases details:',
            },
        ),
        migrations.CreateModel(
            name='ReturnedPurchases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=120, null=True)),
                ('sellers_name', models.CharField(max_length=120, null=True)),
                ('Price_sold', models.FloatField(null=True)),
                ('Price', models.FloatField(null=True)),
                ('product_id', models.CharField(max_length=120, null=True)),
                ('product_title', models.CharField(max_length=120, null=True)),
                ('quantity', models.CharField(max_length=120, null=True)),
                ('currency', models.CharField(max_length=120, null=True)),
                ('product_owner', models.CharField(max_length=120, null=True)),
                ('buyers_name', models.CharField(max_length=120, null=True)),
                ('country', models.CharField(max_length=120, null=True)),
                ('Region', models.CharField(max_length=120, null=True)),
                ('orderdate', models.CharField(blank=True, max_length=120, null=True)),
                ('Time_cancelled', models.DateTimeField(auto_now_add=True)),
                ('Street', models.CharField(max_length=120, null=True)),
                ('processor', models.CharField(max_length=120, null=True)),
                ('phone_no', models.CharField(max_length=120, null=True)),
                ('order_actions', models.CharField(max_length=120, null=True)),
                ('Receive_acc', models.CharField(max_length=120, null=True)),
                ('status', models.CharField(max_length=120, null=True)),
                ('customers_status', models.CharField(max_length=120, null=True)),
                ('sellers_status', models.CharField(max_length=120, null=True)),
                ('shortcode', models.CharField(max_length=120, null=True)),
            ],
            options={
                'verbose_name_plural': 'Returned Purchases',
            },
        ),
        migrations.AddField(
            model_name='creditcard',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='market.Products'),
        ),
    ]
