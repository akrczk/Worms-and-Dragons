from sqlalchemy.orm import Session

from Db.User import User
from Enum.GameState import GameState
from Enum.PlayerClass import PlayerClass
from .GameSession import GameSession
from Monsters.Monster import Monster
from Monsters.MonsterFactory import MonsterFactory
from Player.Classes.PlayerFactory import PlayerFactory
from Player.Player import Player
from UserPrompts.UserPrompts import get_user_input, UserPrompts


class Game:
    player: Player = None
    monster: Monster = None
    session: Session

    def __init__(self, session: Session, user: User):
        self.session = session
        self.user = user
        pass

    def start(self):
        if self.user.hero:
            while True:
                create_new = get_user_input(
                    "Do you want to create a new character? (yes/no): "
                ).lower()
                if create_new not in ["yes", "no"]:
                    print(
                        "Invalid choice. Please type 'yes' or 'no'."
                    )
                else:
                    break
            if create_new == "yes":
                self.create_player()
            else:
                self.player = self.user.hero
        else:
            self.create_player()
        self.create_monster()
        self.fight_monsters()

    def __save_player(self):
        self.session.refresh(self.user)
        self.user.hero = self.player
        self.session.add(self.user)
        self.session.commit()

    def create_player(self):
        player_name = self.select_player_name()
        self.player = PlayerFactory.create(player_name, self.select_player_class())
        self.user.hero = self.player
        self.__save_player()

    def select_player_name(self) -> str:
        while True:
            player_name = get_user_input("Choose your name: ", False)
            confirm_choice = get_user_input(
                f"Type 'A' to choose again or 'C' to confirm ({player_name}): "
            ).upper()
            if confirm_choice == "C":
                return player_name
            elif confirm_choice != "A":
                print(
                    "Invalid choice. Type 'A' to choose again or 'C' to confirm."
                )

    def select_player_class(self) -> PlayerClass:
        while True:
            options = [f"'{i.value}' for {i.name}" for i in PlayerClass]
            class_choice = get_user_input(
                f"Choose your class ({', '.join(options)}): "
            ).upper()
            if PlayerClass.has_value(class_choice):
                return PlayerClass(class_choice)
            else:
                print(
                    "Invalid class choice. Please choose 'W' or 'M'."
                )

    def display_player_info(self):
        print("Player")
        self.player.show_info()

    def display_monster_info(self):
        print("Monster")
        self.monster.show_info()

    def create_monster(self):
        self.monster = MonsterFactory.create_random_monster(5)

    def fight_monsters(self):
        self.display_player_info()
        print()
        self.display_monster_info()
        game_session = GameSession(self.player, self.monster)
        if not game_session.fight() is GameState.PlayerWon:
            print("Game over!")
            quit()
        user_input = get_user_input(
            "Do you want to continue fighting monsters? (yes/no): "
        ).lower()
        self.player.restore_health()
        if user_input == "yes":
            self.create_monster()
            self.fight_monsters()
        else:
            print("Goodbye!")
            self.__save_player()
            print("Progress saved!")
