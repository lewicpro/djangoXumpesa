# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-20 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='application_deadline',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
