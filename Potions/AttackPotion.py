from Potions.Potion import Potion
from UserPrompts.UserPrompts import UserPrompts


class AttackPotion(Potion):
    duration = 2
    statistic_field = "attack"

    def apply(self):
        return 20

    @staticmethod
    def get_display_name():
        return "Attack Potion"
