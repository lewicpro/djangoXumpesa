# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-19 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20171219_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionpayeer',
            name='actualDeposit',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
