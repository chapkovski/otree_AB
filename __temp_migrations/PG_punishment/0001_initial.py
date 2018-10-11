# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-10-11 09:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('total_contribution', otree.db.models.CurrencyField(null=True)),
                ('individual_share', otree.db.models.CurrencyField(null=True)),
                ('round_num', otree.db.models.IntegerField(null=True)),
                ('payoff', otree.db.models.CurrencyField(null=True)),
                ('profit', otree.db.models.CurrencyField(null=True)),
                ('puncost', otree.db.models.CurrencyField(null=True)),
                ('punall', otree.db.models.CurrencyField(null=True)),
                ('punishment', otree.db.models.CurrencyField(null=True, verbose_name='Вычет у участника')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pg_punishment_group', to='otree.Session')),
            ],
            options={
                'db_table': 'PG_punishment_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('contribution', otree.db.models.CurrencyField(null=True)),
                ('pun_1', otree.db.models.CurrencyField(null=True, verbose_name='Вычет у участника 1')),
                ('pun_2', otree.db.models.CurrencyField(null=True, verbose_name='Вычет у участника 2')),
                ('pun_3', otree.db.models.CurrencyField(null=True, verbose_name='Вычет у участника 3')),
                ('pun_4', otree.db.models.CurrencyField(null=True, verbose_name='Вычет у участника 4')),
                ('pun_5', otree.db.models.CurrencyField(null=True, verbose_name='Вычет у участника 5')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='PG_punishment.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pg_punishment_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pg_punishment_player', to='otree.Session')),
            ],
            options={
                'db_table': 'PG_punishment_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pg_punishment_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'PG_punishment_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PG_punishment.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PG_punishment.Subsession'),
        ),
    ]
