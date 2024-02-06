from abc import ABC

from UserPrompts.UserPrompts import UserPrompts


class Creature(ABC):
    stats: dict[str, int]
    name: str
    health: float
    max_health: float
    attack: float
    defense: float

    def __init__(self, name, attack, health, defense):
        self.name = name
        self.max_health = self.health = health
        self.attack = float(attack)
        self.defense = defense

    def take_damage(self, damage: float) -> None:
        damage_dealt = max(0.0, damage - self.defense)
        self.health -= damage_dealt
        self.health = round(max(0.0, self.health), 1)

    def heal(self, amount: float) -> None:
        self.health = round(min(self.max_health, self.health + amount), 1)

    def base_attack(self) -> float:
        return self.attack

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def use_special_attack(self) -> float:
        pass

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
