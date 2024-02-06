import random
from Monsters.Monster import Monster


class Dragon(Monster):
    def __init__(self, name, attack, health, defense):
        super().__init__(name, attack, health, defense)
        self.extra_damage_counter = 2

    def use_special_attack(self) -> float:
        if self.extra_damage_counter > 0:
            self.extra_damage_counter -= 1
            return int(1.75 * self.attack)
        else:
            return int(1.3 * self.attack)

    def _special_attack_probability(self) -> bool:
        return random.random() < 0.25
