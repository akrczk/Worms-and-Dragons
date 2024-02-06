from Player.Player import Player


class Knight(Player):
    def __init__(self, name, attack, health, defense, potions, weapon_damage):
        super().__init__(name, attack, health, defense, potions)
        self.weapon_damage = weapon_damage

    def use_special_attack(self):
        print(f"{self.name} used a B.F. Sword!")
        return self.weapon_damage * 1.5

    def talk(self) -> str:
        return "FOR DEMACIA!!!"
