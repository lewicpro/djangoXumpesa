# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-27 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_auto_20171226_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='total_bitcoin_deposit',
            field=models.FloatField(default=0),
        ),
    ]
