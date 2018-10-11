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


class BeforePunWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_pgg_payoffs()


class Results0(Page):
    ...


class PunPage(Page):
    form_model = models.Player

    def vars_for_template(self):
        frm = self.get_form()
        others = self.player.get_others_in_group()
        return {
            'data': zip(frm, others)
        }

    def get_form_fields(self):
        return ['pun_{}'.format(i.id_in_group) for i in self.player.get_others_in_group()]


class ResultsWaitPage1(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_pun()
            p.set_final_payoff()


class Results1(Page):
    ...


class Results(Page):
    ...

class ResultsSummary(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'total_pgg_payoff': sum([p.pgg_payoff for p in self.player.in_all_rounds()]),
            'total_contribution': sum([p.contribution for p in self.player.in_all_rounds()]),
            'total_punishment_received': sum([p.punishment_received for p in self.player.in_all_rounds()]),
            'total_punishment_sent': sum([p.punishment_sent for p in self.player.in_all_rounds()]),
        }


page_sequence = [
    Contribution,
    BeforePunWP,
    Results0,
    PunPage,
    ResultsWaitPage1,
    Results1,
    Results,
    ResultsSummary
]
