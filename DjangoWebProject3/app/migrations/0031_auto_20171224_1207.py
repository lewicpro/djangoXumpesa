# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-24 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_advcashbalancedeposit_bitcoinbalancedeposit_okpaybalancedeposit_payeerbalancedeposit_perfectmoneyrba'),
    ]

    operations = [
        migrations.CreateModel(
            name='OKpayDeoisitModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=125, null=True)),
                ('username', models.CharField(max_length=125, null=True)),
                ('processor', models.CharField(max_length=125, null=True)),
                ('package', models.CharField(choices=[('Silver', 'Silver'), ('Tarnish', 'Tarnish'), ('Charoite', 'Charoite'), ('TANZANITE', 'TANZANITE'), ('DIAMOND', 'DIAMOND'), ('Karat', 'Karat'), ('Corundum', 'Corundum'), ('Gold', 'Gold'), ('TITANIUM', 'TITANIUM'), ('Niello', 'Niello'), ('Quartz', 'Quartz'), ('Copper', 'Copper'), ('Carbon', 'Carbon'), ('Pearl', 'Pearl'), ('Lapls', 'Lapls'), ('Iron', 'Iron'), ('Emerald', 'Emerald'), ('Glass', 'Glass'), ('Moisanite', 'Moisanite'), ('Calcite', 'Calcite'), ('Sapphire', 'Sapphire'), ('Ruby', 'Ruby'), ('Amber', 'Amber'), ('Agate', 'Agate'), ('Amazonnile', 'Amazonnile'), ('Beads', 'Beads'), ('Beryl', 'Beryl'), ('Azuriite with Malanche', 'Azuriite with Malanche'), ('Zircorn', 'Zircorn'), ('Aluminium', 'Aluminium'), ('Gold', 'Gold'), ('Platnum', 'Platnum')], max_length=125, null=True)),
                ('o_amount', models.FloatField(default=0, null=True)),
                ('opens', models.DateTimeField(blank=True, null=True)),
                ('closes', models.DateTimeField(blank=True, null=True)),
                ('actualDeposit', models.CharField(default=0, max_length=120)),
                ('sign', models.CharField(choices=[('Confirmed', 'Confirmed'), ('Unconfirmed', 'Unconfirmed')], default='Unconfirmed', max_length=120)),
                ('Plan', models.CharField(blank=True, max_length=120, null=True)),
                ('expectedIncome', models.FloatField(default=0)),
                ('hashid', models.CharField(blank=True, max_length=120, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'OK payTransactions',
            },
        ),
        migrations.AddField(
            model_name='processors',
            name='okpay',
            field=models.FloatField(blank=True, default=0),
        ),
    ]