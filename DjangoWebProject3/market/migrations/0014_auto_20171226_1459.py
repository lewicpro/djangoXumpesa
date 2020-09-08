# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-26 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0013_auto_20171226_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Price',
            field=models.FloatField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='products',
            name='Price_sold',
            field=models.FloatField(max_length=12, null=True),
        ),
    ]
