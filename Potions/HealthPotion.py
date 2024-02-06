from Potions.Potion import Potion
from UserPrompts.UserPrompts import UserPrompts


class HealthPotion(Potion):
    statistic_field = "health"

    def apply(self) -> float:
        return 50

    @staticmethod
    def get_display_name():
        return "Health Potion"
