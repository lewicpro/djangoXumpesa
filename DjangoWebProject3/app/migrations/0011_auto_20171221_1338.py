# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-21 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20171221_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositsverified',
            name='hashid',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
