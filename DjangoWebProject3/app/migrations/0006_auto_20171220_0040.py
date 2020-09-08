# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-19 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_transactionperfectmoney_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='balanceredeposit',
            name='actualDeposit',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='balanceredeposit',
            name='sign',
            field=models.CharField(choices=[('Confirmed', 'Confirmed'), ('Unconfirmed', 'Unconfirmed')], default='Unconfirmed', max_length=120),
        ),
    ]