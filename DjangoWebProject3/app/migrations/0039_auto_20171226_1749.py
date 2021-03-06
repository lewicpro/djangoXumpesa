# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-26 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_auto_20171225_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='bitcoin_last_withdrawn',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='bitcoin_profit',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='bitcoin_total_balance',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='bitcoin_total_deposited',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='statistics',
            name='bitcoin_total_withdrawn',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
