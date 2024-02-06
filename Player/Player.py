from Potions.Potion import Potion
from .Creature import Creature
from UserPrompts.UserPrompts import UserPrompts, get_user_input
from collections import Counter


class Player(Creature):
    potions: list[Potion] = []
    active_buffs: list = []

    def __init__(self, name, attack, health, defense, potions=None):
        super().__init__(name, attack, health, defense)
        self.potions = potions or []

    def drink_potion(self) -> bool | None:
        print("Available potions:")

        potions_counter = Counter([i.__class__ for i in self.potions])
        for potion, count in potions_counter.items():
            print(
                f"{potion.get_display_name()}: {count}, press {list(potions_counter.keys()).index(potion)} to use."
            )

        print("Press any other non integer key to cancel.")

        try:
            potion_choice = int(get_user_input("Choose a potion: "))
        except ValueError:
            return False

        if 0 <= potion_choice <= len(list(potions_counter.keys())) - 1:
            self._apply_potion(list(potions_counter.keys())[potion_choice])
        else:
            print("Invalid potion choice. Try again.")
            self.drink_potion()

    def _apply_potion(self, potion_class) -> None:
        potion = next((p for p in self.potions if isinstance(p, potion_class)), None)
        effect_value = potion.apply()
        if potion.statistic_field == "health":
            self.heal(effect_value)
        else:
            setattr(
                self,
                potion.statistic_field,
                getattr(self, potion.statistic_field) + effect_value,
            )
        self.potions.remove(potion)
        if potion.duration:
            self.active_buffs.append(
                (
                    {"field": potion.statistic_field, "value": effect_value},
                    potion.duration,
                )
            )

    def update_buffs(self):
        expired_buffs = []
        for buff, duration in self.active_buffs:
            duration -= 1
            if duration <= 0:
                expired_buffs.append(buff)

        for buff in expired_buffs:
            self._revert_buff(buff)
            self.active_buffs.pop(0)

    def _revert_buff(self, buff: dict):
        setattr(self, buff["field"], getattr(self, buff["field"]) - buff["value"])

    def restore_health(self) -> None:
        self.health = self.max_health
        print(f"{self.name} has restored full health.")

    def talk(self) -> str:
        return "You will never defeat me!"
