# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Tatyana'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'bribery_effort_base_RU'
    players_per_group = 3
    endowment = c(10)
    prize = c(10)
    num_rounds = 10
# c() necessary?
    task_time = 300
    max_task_amount = 10000000

    training_answer_A_correct = c(17)
    training_answer_B_correct = c(6)
    training_answer_C_correct = c(17)

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            paying_rounds = random.sample(range(1, Constants.num_rounds), 1)
            self.session.vars['paying_rounds'] = paying_rounds

        self.group_randomly(fixed_id_in_group=True)


class Group(BaseGroup):
    prize = models.StringField(
    choices=['игрок A', 'игрок B'],
    widget=widgets.RadioSelect())

    def get_winner_name(self):
        s = self.prize.replace('игрок', 'игрок{}')
        return {'nominative': s.format(''),
                'genitive': s.format('а'),
                'dative': s.format('у'),
                'accusative': s.format('а'),
                'instrumental': s.format('ом'),
                'prepositional': s.format('е'),
                }

    contribution_A = models.IntegerField(
        min=0, max=Constants.endowment,
        doc="""The amount contributed by the player""",
    )

    contribution_B = models.IntegerField(
        min=0, max=Constants.endowment,
        doc="""The amount contributed by the player""",
    )

    task_corrects_A = models.IntegerField(default=0)
    task_corrects_B = models.IntegerField(default=0)

    def set_pay(self):
        if self.prize=='игрок A':
            for p in self.get_players():
                if p.role() == "игрок A":
                    p.pay= (Constants.endowment  - self.contribution_A + Constants.prize)
                elif p.role() == "игрок B":
                    p.pay= (Constants.endowment  - self.contribution_B)
                elif p.role() == "судья":
                    p.pay= (Constants.endowment + self.contribution_A + self.contribution_B)

        else:
            for p in self.get_players():
                if p.role() == "игрок A":
                    p.pay= (Constants.endowment  - self.contribution_A)
                elif p.role() == "игрок B":
                    p.pay= (Constants.endowment  - self.contribution_B + Constants.prize)
                elif p.role() == "судья":
                    p.pay= (Constants.endowment + self.contribution_A + self.contribution_B)


    def set_payoff(self): # this is the payoff of the paid rounds
        for player in self.get_players():
            for rounds in self.session.vars['paying_rounds']:
                if player.round_number == rounds:
                    player.payoff = player.pay


class Player(BasePlayer):
    def role(self):
        if self.id_in_group==1:
            return "игрок A"
        elif self.id_in_group==2:
            return "игрок B"
        else:
            return "судья"

    last_correct_answer = models.IntegerField()
    tasks_correct = models.IntegerField(default=0)
    tasks_attempted = models.IntegerField(default=0)

    pay=models.CurrencyField()

    training_answer_A = models.IntegerField(verbose_name='Игрок A заработает')
    training_answer_B = models.IntegerField(verbose_name='Игрок B заработает')
    training_answer_C = models.IntegerField(verbose_name='Судья заработает')







