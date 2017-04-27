from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from tables import group

author = 'Alexis Belianin'

doc = """
PG game for EDots
"""


class Constants(BaseConstants):
    name_in_url = 'PG_try'
    players_per_group = 3
    num_rounds = 8
    endowment = c(100)
    efficiency_factor = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()
    p1 = models.IntegerField()
    p2 = models.IntegerField()
    p3 = models.IntegerField()
    p1_payoff = models.CurrencyField()
    p2_payoff = models.CurrencyField()
    p3_payoff = models.CurrencyField()

    # def __init__(self):
    #    self.group = None

    def set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.individual_share = self.total_contribution * Constants.efficiency_factor / Constants.players_per_group
        self.global_contribution = sum([p.total_contribution for p in self.in_all_rounds()])
        for p in self.get_players():
            p.payoff = Constants.endowment - p.contribution + self.individual_share
            print('*******p.payoff is', p.payoff)

    def globcont(self):
        self.glob_contribution = sum([p.total_contribution for p in self.in_all_rounds()])
        for p in self.in_all_rounds():
            p.globcont = self.glob_contribution
            print('*******my_payoff is', p.globcont)

    def set_payoffs_all(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p3 = self.get_player_by_id(3)
        # p4 = self.get_player_by_id(4)
        # p5 = self.get_player_by_id(5)
        self.p1_payoff = sum([p.payoff for p in self.in_all_rounds() if p.id_in_group == 1])
        self.p2_payoff = sum([p.payoff for p in self.in_all_rounds() if p.id_in_group == 2])
        self.p3_payoff = sum([p.payoff for p in self.in_all_rounds() if p.id_in_group == 3])
        # p2.payoff = sum([p.payoff for p2 in self.in_all_rounds()])
        # p3.payoff = sum([p.payoff for p3 in self.in_all_rounds()])
        # p4.payoff = sum([p4.payoff for p4 in self.in_all_rounds()])
        # p5.payoff = sum([p5.payoff for p5 in self.in_all_rounds()])


class Player(BasePlayer):
    contribution = models.CurrencyField(doc="""The amount contributed by the player""", )
    payoff = models.CurrencyField()
    total_contribution=models.CurrencyField()
    par1 = models.FloatField()
    par2 = models.FloatField()
    par3 = models.FloatField()

    def my_method(self):
        self.my_contribution = sum([p.contribution for p in self.in_all_rounds()])
        self.my_payoff = sum([p.payoff for p in self.in_all_rounds()])
        # self.others_choice = self.get_others_in_group()[4].my_payoff
        for p in self.in_all_rounds():
            p.profit = self.my_payoff
            print('*******my_payoff is', p.profit)
            p.contr = self.my_contribution
            print('*******my_payoff is', p.contr)

#    def other_player(self):
#        return others_choice = self.get_others_in_group()[4].my_payoff
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
