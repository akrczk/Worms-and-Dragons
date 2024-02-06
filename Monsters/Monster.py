from abc import ABC, abstractmethod

from Player.Creature import Creature


class Monster(Creature):
    def _special_attack_probability(self) -> bool:
        return False

    def attack_action(self) -> float:
        return (
            self.use_special_attack()
            if self._special_attack_probability()
            else self.base_attack()
        )
