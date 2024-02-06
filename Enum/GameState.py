from enum import Enum


class GameState(Enum):
    Fighting = 1
    PlayerWon = 2
    EnemyWon = 3
    PlayerFled = 4
