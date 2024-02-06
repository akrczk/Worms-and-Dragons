import random
from time import sleep

from Enum.GameState import GameState
from Monsters.Monster import Monster
from Player.Player import Player
from Enum.PlayerAction import PlayerAction


class GameSession:
    player: Player
    enemy: Monster
    direction: bool = True
    game_state: GameState

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def player_turn(self) -> None:
        action = self.__player_action()
        if isinstance(action, float):
            self.enemy.take_damage(action)
            print(f"{self.enemy.name} has taken {action} damage.")
            print(f"{self.enemy.name} has {self.enemy.health} health remaining.")
        elif action is PlayerAction.Run:
            self.game_state = GameState.PlayerFled
        elif action is PlayerAction.Talk:
            print(f'{self.player.name} says: "{self.player.talk()}"')
            self.player_turn()
        elif action is None:
            self.player_turn()
        self.player.update_buffs()

    def monster_turn(self):
        self.player.take_damage(self.enemy.attack_action())
        print(f"{self.player.name} has taken {self.enemy.attack_action()} damage.")
        print(f"You have {self.player.health} health remaining.")

    def fight(self) -> GameState:
        self.game_state = GameState.Fighting
        while self.game_state is GameState.Fighting:
            self.fight_action()
            self._check_health()

        if self.game_state is GameState.PlayerWon:
            print(f"{self.enemy.name} has died!")
            print(f"{self.player.name} has won!")
        elif self.game_state is GameState.EnemyWon:
            print(f"{self.player.name} has died!")
            print(f"{self.enemy.name} has won!")
        elif self.game_state is GameState.PlayerFled:
            print(f"{self.player.name} has fled the battle!")
        return self.game_state

    def fight_action(self):
        if self.direction:
            print("Player's turn")
            self.player_turn()
        else:
            print()
            sleep(1)
            print("Monster's turn")
            self.monster_turn()

        self.direction = not self.direction

    def _check_health(self) -> None:
        if self.player.health <= 0:
            self.game_state = GameState.EnemyWon
        elif self.enemy.health <= 0:
            self.game_state = GameState.PlayerWon

    def __player_action(self) -> None | float | PlayerAction:
        action = input(
            f"{self.player.name},"
            f" choose your action (A for normal attack, SA for special attack, P for potions, R to run, T to talk): "
        ).upper()
        match action:
            case PlayerAction.Attack.value:
                return self.player.base_attack()
            case PlayerAction.SpecialAttack.value:
                return self.player.use_special_attack()
            case PlayerAction.DrinkPotion.value:
                if self.player.drink_potion() is not False:
                    return False
            case PlayerAction.Run.value:
                if random.random() < 0.25:
                    print("You have successfully fled the battle!")
                    return PlayerAction.Run
                print("You failed to flee the battle!")
                return False
            case PlayerAction.Talk.value:
                return PlayerAction.Talk
            case _:
                print("Invalid action. Please choose A, SA, P, R or T.")
