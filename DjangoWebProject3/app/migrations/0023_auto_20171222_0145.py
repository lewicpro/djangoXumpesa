# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-21 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20171222_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='last_withdrawal',
            field=models.PositiveIntegerField(default=0.0),
        ),
    ]