from Enum.PlayerClass import PlayerClass
from Player.Classes.Barbarian import Barbarian
from Player.Classes.Knight import Knight
from Player.Classes.Mage import Mage
from Player.Classes.Archer import Archer
from Player.Player import Player
from Potions.DefencePotion import DefencePotion
from Potions.AttackPotion import AttackPotion
from Potions.HealthPotion import HealthPotion


class PlayerFactory:

    @staticmethod
    def create(name: str, class_type: PlayerClass) -> Player:
        potions = (
            [HealthPotion() for i in range(20)]
            + [DefencePotion() for i in range(5)]
            + [AttackPotion() for i in range(5)]
        )

        if class_type is PlayerClass.Mage:
            return Mage(name, 40, 220, 40, potions, 50)
        elif class_type is PlayerClass.Archer:
            return Archer(name, 50, 250, 30, potions, 60)
        elif class_type is PlayerClass.Knight:
            return Knight(name, 60, 275, 30, potions, 70)
        elif class_type is PlayerClass.Barbarian:
            return Barbarian(name, 60, 350, 45, potions, 60)
        else:
            raise ValueError(f"Unknown class type: {class_type}")
