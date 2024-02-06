from enum import Enum


class PlayerClass(Enum):
    Archer = "A"
    Mage = "M"
    Knight = "K"
    Barbarian = "B"

    @classmethod
    def has_value(cls, value):
        return any(value == item.value for item in cls)
