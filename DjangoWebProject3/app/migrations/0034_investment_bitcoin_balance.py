# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-24 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0033_auto_20171224_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='Bitcoin_balance',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
