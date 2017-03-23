# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_ecommerceuser_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecommerceuser',
            name='company',
            field=models.CharField(default='', help_text='Company info added by user upon registration', max_length=255),
        ),
    ]
