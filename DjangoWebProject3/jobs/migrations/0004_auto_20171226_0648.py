# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-26 03:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20171221_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='application_deadline',
            field=models.DateField(blank=True, max_length=120, null=True),
        ),
    ]
