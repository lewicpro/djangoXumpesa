# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-21 15:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0016_balanceredeposit_processor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Processors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfectmoney', models.FloatField(blank=True, null=True)),
                ('payeer', models.FloatField(blank=True, null=True)),
                ('bitcoin', models.FloatField(blank=True, null=True)),
                ('adcash', models.FloatField(blank=True, null=True)),
                ('Etherium', models.FloatField(blank=True, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
