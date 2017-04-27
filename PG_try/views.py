from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Contribution(Page):
    form_model = models.Player
    form_fields = ['contribution']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        self.player.my_method()
        return {
            'my_payoff': sum([p.payoff for p in self.player.in_all_rounds()]),
            'me_in_all_rounds': self.player.get_others_in_group()
        }

#    def vars2_for_template(self):
#        self.player.my_method()
#        all_payoffs = []
#
#        for players_ind in self.player.get_others_in_group():
#            all_payoffs.append({
#                'others_payoff': players_ind.my_payoff
#            })
#        other_player_ids = [p.id_in_group for p in self.player.get_others_in_group()]
#        #     my_payoff = sum([p.payoff for p in self.player.in_all_rounds()]),
#        #     me_in_all_rounds = self.player.get_others_in_group(),
#        return {
#            'all_payoffs': all_payoffs,  # sum([p.payoff for p in self.player.in_all_rounds()]),
#            'other_player_ids': other_player_ids  # self.player.get_others_in_group(),
#        }
#
#
#
#class ChoiceOne(Page):
#    def is_displayed(self):
#        return self.player.id_in_group == 1

# def var1_for_template(self):
#        self.group.globcont
#        #return {
#        #    'global_contribution': sum([p.total_contribution for p in self.player.in_all_rounds()])
#        #}

page_sequence = [
    Contribution,
    ResultsWaitPage,
    Results
]
