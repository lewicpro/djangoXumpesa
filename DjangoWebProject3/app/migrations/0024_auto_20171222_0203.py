# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-21 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20171222_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='last_withdrawal',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='investment',
            name='pending_withdrawal',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='verifiedwithdrawals',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]