# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-26 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0018_auto_20171226_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='currency',
            field=models.CharField(choices=[('$', '$'), ('BTC', 'BTC')], max_length=120, null=True),
        ),
    ]