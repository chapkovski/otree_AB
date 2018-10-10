from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Contribution(Page):
    form_model = models.Player
    form_fields = ['contribution']
    def vars_for_template(self):
        return {
           'current_round': self.subsession.round_number
        }

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

#    wait_for_all_groups=True

class Results0(Page):
    wait_for_all_players=True
    def vars_for_template(self):
        self.player.my_method()

class PunPage(Page):
    form_model = models.Player
#    form_fields = ['pun_{}'.format(i) for i in range(1, 6)]
    def vars_for_template(self):
        self.group.set_payoffs() # group.set_payoffs() # my_method()
        return {
#            'my_payoff': sum([p.profit for p in self.in_all_rounds()]),
            'me_in_all_rounds_1': self.group.get_player_by_id(1).payoff,
            'me_in_all_rounds_2': self.group.get_player_by_id(2).payoff,
            'me_in_all_rounds_3': self.group.get_player_by_id(3).payoff,
            'me_in_all_rounds_4': self.group.get_player_by_id(4).payoff,
            'me_in_all_rounds_5': self.group.get_player_by_id(5).payoff,
            'p1_contr': self.group.get_player_by_id(1).contribution,
            'p2_contr': self.group.get_player_by_id(2).contribution,
            'p3_contr': self.group.get_player_by_id(3).contribution,
            'p4_contr': self.group.get_player_by_id(4).contribution,
            'p5_contr': self.group.get_player_by_id(5).contribution,
            # 'pun_1': self.group.get_player_by_id(1).pun,
            # 'pun_2': self.group.get_player_by_id(2).pun,
            # 'pun_3': self.group.get_player_by_id(3).pun,
            # 'pun_4': self.group.get_player_by_id(4).pun,
            # 'pun_5': self.group.get_player_by_id(5).pun,
            'current_round': self.subsession.round_number
         }
    def get_form_fields(self):
        # pun_i is punishment by some player to player i
        if self.player.id_in_group == 1:
            return ['pun_2', 'pun_3', 'pun_4', 'pun_5']
        if self.player.id_in_group == 2:
            return ['pun_1', 'pun_3', 'pun_4', 'pun_5']
        if self.player.id_in_group == 3:
            return ['pun_1', 'pun_2', 'pun_4', 'pun_5']
        if self.player.id_in_group == 4:
            return ['pun_1', 'pun_2', 'pun_3', 'pun_5']
        if self.player.id_in_group == 5:
            return ['pun_1', 'pun_2', 'pun_3', 'pun_4']

class ResultsWaitPage1(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_pun()

# class Results(Page):
#     wait_for_all_players=True
#     def vars_for_template(self):
#         self.player.set_punpay()

# class ResultsWaitPage1(WaitPage):
#     def after_all_players_arrive(self):
#         self.group.set_punpay()
#         return {
#             'me_in_all_rounds_1': self.group.get_player_by_id(1).my_payoff,
#             'me_in_all_rounds_2': self.group.get_player_by_id(2).my_payoff,
#             'me_in_all_rounds_3': self.group.get_player_by_id(3).my_payoff,
#             'me_in_all_rounds_4': self.group.get_player_by_id(4).my_payoff,
#             'me_in_all_rounds_5': self.group.get_player_by_id(5).my_payoff,
#             'p1_contr': self.group.get_player_by_id(1).my_contribution,
#             'p2_contr': self.group.get_player_by_id(2).my_contribution,
#             'p3_contr': self.group.get_player_by_id(3).my_contribution,
#             'p4_contr': self.group.get_player_by_id(4).my_contribution,
#             'p5_contr': self.group.get_player_by_id(5).my_contribution,
#             'current_round': self.subsession.round_number,
#         }



class Results1(Page):
    wait_for_all_players=True
    def vars_for_template(self):
        self.player.set_punpay()


class Results(Page):
    wait_for_all_players=True
    form_model = models.Player
#    form_fields = ['pun_{}'.format(i) for i in range(1, 6)]
    def vars_for_template(self):
        self.player.set_punpay()
        return {
        #    'my_profit': sum([p.my_profit for p in self.player.in_all_rounds()]),
            'my_in_all_rounds_1': self.group.get_player_by_id(1).my_profit,
            'my_in_all_rounds_2': self.group.get_player_by_id(2).my_profit,
            'my_in_all_rounds_3': self.group.get_player_by_id(3).my_profit,
            'my_in_all_rounds_4': self.group.get_player_by_id(4).my_profit,
            'my_in_all_rounds_5': self.group.get_player_by_id(5).my_profit,
            'p1_sumcontr': self.group.get_player_by_id(1).contribution,
            'p2_sumcontr': self.group.get_player_by_id(2).contribution,
            'p3_sumcontr': self.group.get_player_by_id(3).contribution,
            'p4_sumcontr': self.group.get_player_by_id(4).contribution,
            'p5_sumcontr': self.group.get_player_by_id(5).contribution,
            'current_round': self.subsession.round_number,
        }

class ResultsSummary(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'total_payoff': sum([p.payoff for p in self.player.in_all_rounds()]),
            'player_in_all_rounds': self.player.in_all_rounds(),
            'total_contribution': sum([p.contribution for p in self.player.in_all_rounds()]),
            'total_punishment': sum([p.pun for p in self.player.in_all_rounds()]),
            'total_puncost': sum([p.puncost for p in self.player.in_all_rounds()]),
            'total_profit': sum([p.profit for p in self.player.in_all_rounds()]),

        }


page_sequence = [
    Contribution,
    ResultsWaitPage,
    Results0,
    PunPage,
    ResultsWaitPage1,
    Results1,
    Results,
    ResultsSummary
]
