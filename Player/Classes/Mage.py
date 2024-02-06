from Player.Player import Player


class Mage(Player):
    def __init__(self, name, attack, health, defense, potions, magic_power):
        super().__init__(name, attack, health, defense, potions)
        self.magic_power = magic_power

    def use_special_attack(self) -> float:
        print(f"{self.name} used needlessly large rod!")
        return self.magic_power * 1.5

    def talk(self) -> str:
        return "t⍑╎ᓭ ╎ᓭ ᒷᔑᓭℸ ̣ᒷ∷-ᒷ ⊣ ⊣"
