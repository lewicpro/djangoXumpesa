# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-03 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_purchases_buyers_acc'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchases',
            name='complete',
            field=models.CharField(choices=[('Uncompleted', 'Uncompleted'), ('completed', 'completed')], default='Uncompleted', max_length=120),
        ),
    ]
