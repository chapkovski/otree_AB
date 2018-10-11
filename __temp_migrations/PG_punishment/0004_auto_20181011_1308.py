# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-10-11 10:08
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('PG_punishment', '0003_auto_20181011_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='payoff',
        ),
        migrations.RemoveField(
            model_name='group',
            name='profit',
        ),
        migrations.RemoveField(
            model_name='group',
            name='punall',
        ),
        migrations.RemoveField(
            model_name='group',
            name='puncost',
        ),
        migrations.RemoveField(
            model_name='group',
            name='punishment',
        ),
        migrations.RemoveField(
            model_name='group',
            name='round_num',
        ),
        migrations.AddField(
            model_name='player',
            name='pgg_payoff',
            field=otree.db.models.CurrencyField(default=0, null=True),
        ),
    ]
