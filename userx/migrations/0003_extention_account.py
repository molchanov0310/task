# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userx', '0002_extention_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='extention',
            name='account',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=32, verbose_name='\u0421\u0447\u0451\u0442'),
            preserve_default=False,
        ),
    ]
