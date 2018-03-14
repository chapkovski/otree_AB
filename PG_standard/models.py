from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
# from tables import group

#import random

from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree.db import models
#from otree import widgets
from otree.common import Currency as c, currency_range, safe_json

author = 'Alexis Belianin'

doc = """
PG game for EDots
"""


class Constants(BaseConstants):
    name_in_url = 'PG_standard'
    players_per_group = 5
    num_rounds = 8
    endowment = c(100)
    lumpsum = c(160)
    efficiency_factor = 2
    contribution_limits = currency_range(0, endowment, 1) #define range of contribs


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    round_num=models.IntegerField()

    # def __init__(self):
    #    self.group = None
    def round_number(self):
        return self.subsession.round_number

    def set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.individual_share = self.total_contribution * Constants.efficiency_factor / Constants.players_per_group
#        self.global_contribution = sum([p.total_contribution for p in self.in_all_rounds()])
        for p in self.get_players():
            p.payoff = Constants.endowment - p.contribution + self.individual_share
            # p1 = self.get_player_by_id(1)
            # p2 = self.get_player_by_id(2)
            # p3 = self.get_player_by_id(3)
            # p1_payoff = sum([p.payoff for p in self.in_previous_rounds() if p.p1 == 1])
            # p2_payoff = sum([p.payoff for p in self.in_previous_rounds() if p.p2 == 2])
            # p3_payoff = sum([p.payoff for p in self.in_previous_rounds() if p.p3 == 3])  # in_all_rounds
            print('p.payoff_is', p.payoff)

class Player(BasePlayer):
    contribution = models.CurrencyField(doc="""The amount contributed by the player""", min=0,max=100) # choices=Constants.contribution_limits) #add this to see schedule of contribs
    payoff = models.CurrencyField()
    total_contribution = models.CurrencyField()
    my_contribution = models.CurrencyField(doc="""The amount contributed by the player""", )
    my_payoff = models.CurrencyField()

    def my_method(self):
        self.my_contribution = sum([p.contribution for p in self.in_all_rounds()])
        self.my_payoff = sum([p.payoff for p in self.in_all_rounds()])

                # def role(self):
                #    if self.id_in_group == 1:
                #        self.idind = 1
                #        self.par1 = self.my_payoff(1)
                #    if self.id_in_group == 2:
                #        self.idind = 2
                #        self.par2 = self.my_payoff(2)
                #    if self.id_in_group == 3:
                #        self.idind = 3
                #        self.par3 = self.my_payoff(3)


                #def role(self):
    #    if self.id_in_group == 1:
    #        self.idind = 1
    #        self.par1 = self.my_payoff(1)
    #    if self.id_in_group == 2:
    #        self.idind = 2
    #        self.par2 = self.my_payoff(2)
    #    if self.id_in_group == 3:
    #        self.idind = 3
    #        self.par3 = self.my_payoff(3)
