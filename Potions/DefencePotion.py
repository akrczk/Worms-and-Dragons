from Potions.Potion import Potion
from UserPrompts.UserPrompts import UserPrompts


class DefencePotion(Potion):
    duration = 2
    statistic_field = "defense"

    def apply(self) -> float:
        return 10

    @staticmethod
    def get_display_name():
        return "Defense Potion"
