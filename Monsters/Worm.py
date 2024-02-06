import random
from Monsters.Monster import (
    Monster,
)  # Assuming this is the correct import for your Monster class


class Worm(Monster):

    def use_special_attack(self) -> float:
        return int(2.0 * self.attack)

    def _special_attack_probability(self) -> bool:
        return random.random() < 0.3
