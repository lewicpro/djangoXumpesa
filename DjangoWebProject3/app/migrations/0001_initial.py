# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-19 11:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceRedeposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=125, null=True)),
                ('Xumpesa_account', models.CharField(max_length=120, null=True)),
                ('package', models.CharField(choices=[('Silver', 'Silver'), ('Tarnish', 'Tarnish'), ('Charoite', 'Charoite'), ('TANZANITE', 'TANZANITE'), ('DIAMOND', 'DIAMOND'), ('Karat', 'Karat'), ('Corundum', 'Corundum'), ('Gold', 'Gold'), ('TITANIUM', 'TITANIUM'), ('Niello', 'Niello'), ('Quartz', 'Quartz'), ('Copper', 'Copper'), ('Carbon', 'Carbon'), ('Pearl', 'Pearl'), ('Lapls', 'Lapls'), ('Iron', 'Iron'), ('Emerald', 'Emerald'), ('Glass', 'Glass'), ('Moisanite', 'Moisanite'), ('Calcite', 'Calcite'), ('Sapphire', 'Sapphire'), ('Ruby', 'Ruby'), ('Amber', 'Amber'), ('Agate', 'Agate'), ('Amazonnile', 'Amazonnile'), ('Beads', 'Beads'), ('Beryl', 'Beryl'), ('Azuriite with Malanche', 'Azuriite with Malanche'), ('Zircorn', 'Zircorn'), ('Aluminium', 'Aluminium'), ('Gold', 'Gold'), ('Platnum', 'Platnum')], max_length=125, null=True)),
                ('amount_transfered', models.FloatField(null=True)),
                ('date_stamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('Plan', models.CharField(blank=True, max_length=120, null=True)),
                ('opens', models.DateTimeField(blank=True, null=True)),
                ('hashid', models.CharField(blank=True, max_length=120)),
                ('closes', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=126, null=True)),
            ],
            options={
                'verbose_name_plural': 'Redeposit Transactions',
            },
        ),
        migrations.CreateModel(
            name='BalanceTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=125, null=True)),
                ('from_account_no', models.CharField(blank=True, max_length=125, null=True)),
                ('username_receiver', models.CharField(max_length=120, null=True)),
                ('security_code', models.CharField(max_length=120, null=True)),
                ('amount_transfered', models.FloatField(null=True)),
                ('date_stamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Account Balance Transactions',
            },
        ),
        migrations.CreateModel(
            name='Deposits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120, null=True)),
                ('depositing_amount', models.PositiveIntegerField(null=True)),
                ('name', models.CharField(max_length=120, null=True)),
                ('account_number', models.CharField(max_length=120, null=True)),
                ('processor', models.CharField(max_length=120, null=True)),
                ('kumbukumbu_no', models.CharField(default='', max_length=120)),
                ('package', models.CharField(choices=[('Silver', 'Silver'), ('Tarnish', 'Tarnish'), ('Charoite', 'Charoite'), ('TANZANITE', 'TANZANITE'), ('DIAMOND', 'DIAMOND'), ('Karat', 'Karat'), ('Corundum', 'Corundum'), ('Gold', 'Gold'), ('TITANIUM', 'TITANIUM'), ('Niello', 'Niello'), ('Quartz', 'Quartz'), ('Copper', 'Copper'), ('Carbon', 'Carbon'), ('Pearl', 'Pearl'), ('Lapls', 'Lapls'), ('Iron', 'Iron'), ('Emerald', 'Emerald'), ('Glass', 'Glass'), ('Moisanite', 'Moisanite'), ('Calcite', 'Calcite'), ('Sapphire', 'Sapphire'), ('Ruby', 'Ruby'), ('Amber', 'Amber'), ('Agate', 'Agate'), ('Amazonnile', 'Amazonnile'), ('Beads', 'Beads'), ('Beryl', 'Beryl'), ('Azuriite with Malanche', 'Azuriite with Malanche'), ('Zircorn', 'Zircorn'), ('Aluminium', 'Aluminium'), ('Gold', 'Gold'), ('Platnum', 'Platnum')], max_length=125, null=True)),
                ('opens', models.DateField(blank=True, null=True)),
                ('closes', models.DateField(blank=True, null=True)),
                ('shortcode', models.CharField(blank=True, max_length=15, null=True)),
                ('status', models.CharField(choices=[('Verified', 'Verified'), ('not verified', 'Not verified')], default='not verified', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='DepositsVerified',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120, null=True)),
                ('depositing_amount', models.FloatField(null=True)),
                ('depositing_id', models.PositiveIntegerField(null=True)),
                ('name', models.CharField(max_length=120, null=True)),
                ('account_number', models.CharField(max_length=120, null=True)),
                ('kumbukumbu_no', models.CharField(default='', max_length=120)),
                ('verification_code', models.CharField(max_length=120, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Verified', 'Verified'), ('not verified', 'Not verified')], default='Verified', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(default=0.0)),
                ('account_type', models.CharField(choices=[('tIGoPesa', 'tIGoPesa'), ('Mpesa', 'Mpesa'), ('AirtelMoney', 'AirtelMoney'), ('Bitcoin', 'Bitcoin')], default='', max_length=20)),
                ('requested_amount', models.FloatField(default=0.0)),
                ('account_no', models.CharField(max_length=120, null=True)),
                ('pending_withdrawal', models.PositiveIntegerField(default=0.0)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='lewicpro', max_length=25)),
                ('profit', models.FloatField(blank=True, default=0)),
                ('total_deposited', models.FloatField(blank=True, default=0)),
                ('total_withdrawn', models.FloatField(blank=True, default=0)),
                ('last_withdrawn', models.FloatField(blank=True, default=0)),
                ('total_balance', models.FloatField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionPayeer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=125, null=True)),
                ('username', models.CharField(max_length=125, null=True)),
                ('processor', models.CharField(max_length=125, null=True)),
                ('package', models.CharField(choices=[('Silver', 'Silver'), ('Tarnish', 'Tarnish'), ('Charoite', 'Charoite'), ('TANZANITE', 'TANZANITE'), ('DIAMOND', 'DIAMOND'), ('Karat', 'Karat'), ('Corundum', 'Corundum'), ('Gold', 'Gold'), ('TITANIUM', 'TITANIUM'), ('Niello', 'Niello'), ('Quartz', 'Quartz'), ('Copper', 'Copper'), ('Carbon', 'Carbon'), ('Pearl', 'Pearl'), ('Lapls', 'Lapls'), ('Iron', 'Iron'), ('Emerald', 'Emerald'), ('Glass', 'Glass'), ('Moisanite', 'Moisanite'), ('Calcite', 'Calcite'), ('Sapphire', 'Sapphire'), ('Ruby', 'Ruby'), ('Amber', 'Amber'), ('Agate', 'Agate'), ('Amazonnile', 'Amazonnile'), ('Beads', 'Beads'), ('Beryl', 'Beryl'), ('Azuriite with Malanche', 'Azuriite with Malanche'), ('Zircorn', 'Zircorn'), ('Aluminium', 'Aluminium'), ('Gold', 'Gold'), ('Platnum', 'Platnum')], max_length=125, null=True)),
                ('m_amount', models.FloatField(max_length=35, null=True)),
                ('opens', models.DateTimeField(blank=True, null=True)),
                ('closes', models.DateTimeField(blank=True, null=True)),
                ('sign', models.CharField(choices=[('Confirmed', 'Confirmed'), ('Unconfirmed', 'Unconfirmed')], default='Unconfirmed', max_length=120)),
                ('Plan', models.CharField(blank=True, max_length=120, null=True)),
                ('hashid', models.CharField(blank=True, max_length=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Payeer Transactions',
            },
        ),
        migrations.CreateModel(
            name='TransactionPerfectMoney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=125, null=True)),
                ('username', models.CharField(max_length=125, null=True)),
                ('processor', models.CharField(max_length=125, null=True)),
                ('package', models.CharField(choices=[('Silver', 'Silver'), ('Tarnish', 'Tarnish'), ('Charoite', 'Charoite'), ('TANZANITE', 'TANZANITE'), ('DIAMOND', 'DIAMOND'), ('Karat', 'Karat'), ('Corundum', 'Corundum'), ('Gold', 'Gold'), ('TITANIUM', 'TITANIUM'), ('Niello', 'Niello'), ('Quartz', 'Quartz'), ('Copper', 'Copper'), ('Carbon', 'Carbon'), ('Pearl', 'Pearl'), ('Lapls', 'Lapls'), ('Iron', 'Iron'), ('Emerald', 'Emerald'), ('Glass', 'Glass'), ('Moisanite', 'Moisanite'), ('Calcite', 'Calcite'), ('Sapphire', 'Sapphire'), ('Ruby', 'Ruby'), ('Amber', 'Amber'), ('Agate', 'Agate'), ('Amazonnile', 'Amazonnile'), ('Beads', 'Beads'), ('Beryl', 'Beryl'), ('Azuriite with Malanche', 'Azuriite with Malanche'), ('Zircorn', 'Zircorn'), ('Aluminium', 'Aluminium'), ('Gold', 'Gold'), ('Platnum', 'Platnum')], max_length=125, null=True)),
                ('PAYMENT_AMOUNT', models.FloatField(max_length=35, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Plan', models.CharField(blank=True, max_length=120, null=True)),
                ('opens', models.DateTimeField(blank=True, null=True)),
                ('closes', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'verbose_name_plural': 'Perfect Money Transactions',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, default='', max_length=120)),
                ('amount', models.FloatField(default=0.0)),
                ('Perfect_money', models.CharField(blank=True, default='', max_length=14)),
                ('Bitcoin', models.CharField(blank=True, default='', max_length=120)),
                ('Payeer', models.CharField(blank=True, default='', max_length=35)),
                ('advcash', models.CharField(blank=True, default='', max_length=35)),
                ('Phone_no', models.CharField(default='', max_length=14)),
                ('country', models.CharField(choices=[('AD', 'Andorra'), ('AE', 'United Arab Emirates'), ('AF', 'Afghanistan'), ('AG', 'Antigua & Barbuda'), ('AI', 'Anguilla'), ('AL', 'Albania'), ('AM', 'Armenia'), ('AN', 'Netherlands Antilles'), ('AO', 'Angola'), ('AQ', 'Antarctica'), ('AR', 'Argentina'), ('AS', 'American Samoa'), ('AT', 'Austria'), ('AU', 'Australia'), ('AW', 'Aruba'), ('AZ', 'Azerbaijan'), ('BA', 'Bosnia and Herzegovina'), ('BB', 'Barbados'), ('BD', 'Bangladesh'), ('BE', 'Belgium'), ('BF', 'Burkina Faso'), ('BG', 'Bulgaria'), ('BH', 'Bahrain'), ('BI', 'Burundi'), ('BJ', 'Benin'), ('BM', 'Bermuda'), ('BN', 'Brunei Darussalam'), ('BO', 'Bolivia'), ('BR', 'Brazil'), ('BS', 'Bahama'), ('BT', 'Bhutan'), ('BV', 'Bouvet Island'), ('BW', 'Botswana'), ('BY', 'Belarus'), ('BZ', 'Belize'), ('CA', 'Canada'), ('CC', 'Cocos (Keeling) Islands'), ('CF', 'Central African Republic'), ('CG', 'Congo'), ('CH', 'Switzerland'), ('CI', 'Ivory Coast'), ('CK', 'Cook Iislands'), ('CL', 'Chile'), ('CM', 'Cameroon'), ('CN', 'China'), ('CO', 'Colombia'), ('CR', 'Costa Rica'), ('CU', 'Cuba'), ('CV', 'Cape Verde'), ('CX', 'Christmas Island'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DE', 'Germany'), ('DJ', 'Djibouti'), ('DK', 'Denmark'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'), ('DZ', 'Algeria'), ('EC', 'Ecuador'), ('EE', 'Estonia'), ('EG', 'Egypt'), ('EH', 'Western Sahara'), ('ER', 'Eritrea'), ('ES', 'Spain'), ('ET', 'Ethiopia'), ('FI', 'Finland'), ('FJ', 'Fiji'), ('FK', 'Falkland Islands (Malvinas)'), ('FM', 'Micronesia'), ('FO', 'Faroe Islands'), ('FR', 'France'), ('FX', 'France, Metropolitan'), ('GA', 'Gabon'), ('GB', 'United Kingdom (Great Britain)'), ('GD', 'Grenada'), ('GE', 'Georgia'), ('GF', 'French Guiana'), ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GL', 'Greenland'), ('GM', 'Gambia'), ('GN', 'Guinea'), ('GP', 'Guadeloupe'), ('GQ', 'Equatorial Guinea'), ('GR', 'Greece'), ('GS', 'South Georgia and the South Sandwich Islands'), ('GT', 'Guatemala'), ('GU', 'Guam'), ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HK', 'Hong Kong'), ('HM', 'Heard & McDonald Islands'), ('HN', 'Honduras'), ('HR', 'Croatia'), ('HT', 'Haiti'), ('HU', 'Hungary'), ('ID', 'Indonesia'), ('IE', 'Ireland'), ('IL', 'Israel'), ('IN', 'India'), ('IO', 'British Indian Ocean Territory'), ('IQ', 'Iraq'), ('IR', 'Islamic Republic of Iran'), ('IS', 'Iceland'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JO', 'Jordan'), ('JP', 'Japan'), ('KE', 'Kenya'), ('KG', 'Kyrgyzstan'), ('KH', 'Cambodia'), ('KI', 'Kiribati'), ('KM', 'Comoros'), ('KN', 'St. Kitts and Nevis'), ('KP', "Korea, Democratic People's Republic of"), ('KR', 'Korea, Republic of'), ('KW', 'Kuwait'), ('KY', 'Cayman Islands'), ('KZ', 'Kazakhstan'), ('LA', "Lao People's Democratic Republic"), ('LB', 'Lebanon'), ('LC', 'Saint Lucia'), ('LI', 'Liechtenstein'), ('LK', 'Sri Lanka'), ('LR', 'Liberia'), ('LS', 'Lesotho'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('LV', 'Latvia'), ('LY', 'Libyan Arab Jamahiriya'), ('MA', 'Morocco'), ('MC', 'Monaco'), ('MD', 'Moldova, Republic of'), ('MG', 'Madagascar'), ('MH', 'Marshall Islands'), ('ML', 'Mali'), ('MN', 'Mongolia'), ('MM', 'Myanmar'), ('MO', 'Macau'), ('MP', 'Northern Mariana Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MS', 'Monserrat'), ('MT', 'Malta'), ('MU', 'Mauritius'), ('MV', 'Maldives'), ('MW', 'Malawi'), ('MX', 'Mexico'), ('MY', 'Malaysia'), ('MZ', 'Mozambique'), ('NA', 'Namibia'), ('NC', 'New Caledonia'), ('NE', 'Niger'), ('NF', 'Norfolk Island'), ('NG', 'Nigeria'), ('NI', 'Nicaragua'), ('NL', 'Netherlands'), ('NO', 'Norway'), ('NP', 'Nepal'), ('NR', 'Nauru'), ('NU', 'Niue'), ('NZ', 'New Zealand'), ('OM', 'Oman'), ('PA', 'Panama'), ('PE', 'Peru'), ('PF', 'French Polynesia'), ('PG', 'Papua New Guinea'), ('PH', 'Philippines'), ('PK', 'Pakistan'), ('PL', 'Poland'), ('PM', 'St. Pierre & Miquelon'), ('PN', 'Pitcairn'), ('PR', 'Puerto Rico'), ('PT', 'Portugal'), ('PW', 'Palau'), ('PY', 'Paraguay'), ('QA', 'Qatar'), ('RE', 'Reunion'), ('RO', 'Romania'), ('RU', 'Russian Federation'), ('RW', 'Rwanda'), ('SA', 'Saudi Arabia'), ('SB', 'Solomon Islands'), ('SC', 'Seychelles'), ('SD', 'Sudan'), ('SE', 'Sweden'), ('SG', 'Singapore'), ('SH', 'St. Helena'), ('SI', 'Slovenia'), ('SJ', 'Svalbard & Jan Mayen Islands'), ('SK', 'Slovakia'), ('SL', 'Sierra Leone'), ('SM', 'San Marino'), ('SN', 'Senegal'), ('SO', 'Somalia'), ('SR', 'Suriname'), ('ST', 'Sao Tome & Principe'), ('SV', 'El Salvador'), ('SY', 'Syrian Arab Republic'), ('SZ', 'Swaziland'), ('TC', 'Turks & Caicos Islands'), ('TD', 'Chad'), ('TF', 'French Southern Territories'), ('TG', 'Togo'), ('TH', 'Thailand'), ('TJ', 'Tajikistan'), ('TK', 'Tokelau'), ('TM', 'Turkmenistan'), ('TN', 'Tunisia'), ('TO', 'Tonga'), ('TP', 'East Timor'), ('TR', 'Turkey'), ('TT', 'Trinidad & Tobago'), ('TV', 'Tuvalu'), ('TW', 'Taiwan, Province of China'), ('TZ', 'Tanzania, United Republic of'), ('UA', 'Ukraine'), ('UG', 'Uganda'), ('UM', 'United States Minor Outlying Islands'), ('US', 'United States of America'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VA', 'Vatican City State (Holy See)'), ('VC', 'St. Vincent & the Grenadines'), ('VE', 'Venezuela'), ('VG', 'British Virgin Islands'), ('VI', 'United States Virgin Islands'), ('VN', 'Viet Nam'), ('VU', 'Vanuatu'), ('WF', 'Wallis & Futuna Islands'), ('WS', 'Samoa'), ('YE', 'Yemen'), ('YT', 'Mayotte'), ('YU', 'Yugoslavia'), ('ZA', 'South Africa'), ('ZM', 'Zambia'), ('ZR', 'Zaire'), ('ZW', 'Zimbabwe'), ('ZZ', 'Unknown or unspecified country')], max_length=120, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('Bio', models.CharField(max_length=120, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('total_deposit', models.FloatField(default=0)),
                ('shortcode', models.CharField(blank=True, max_length=15, unique=True)),
                ('verification_code', models.CharField(default='', max_length=6)),
                ('security_code', models.CharField(max_length=4, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120, null=True)),
                ('full_name', models.CharField(max_length=120, null=True)),
                ('balance', models.CharField(max_length=120, null=True)),
                ('processor', models.CharField(max_length=120, null=True)),
                ('tigopesa_number', models.CharField(max_length=120, null=True)),
                ('withdrawing_amount', models.FloatField(null=True)),
                ('account_number', models.CharField(max_length=120, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Withdrawprocessor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120, null=True)),
                ('full_name', models.CharField(max_length=120, null=True)),
                ('balance', models.CharField(max_length=120, null=True)),
                ('processor', models.CharField(max_length=120, null=True)),
                ('processor_acc_number', models.CharField(max_length=120, null=True)),
                ('m_amount', models.FloatField(null=True)),
                ('account_number', models.CharField(max_length=120, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]