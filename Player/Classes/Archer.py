from Player.Player import Player


class Archer(Player):
    def __init__(self, name, attack, health, defense, potions, weapon_damage):
        super().__init__(name, attack, health, defense, potions)
        self.weapon_damage = weapon_damage

    def use_special_attack(self):
        print(f"{self.name} used a Before Christ Cross-bow!")
        return self.weapon_damage * 1.5

    def talk(self) -> str:
        return "My arrow will be as true as my heart is pure!"
