# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-26 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0012_purchases_currency_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paidproducts',
            name='Price',
            field=models.FloatField(default=''),
        ),
    ]
