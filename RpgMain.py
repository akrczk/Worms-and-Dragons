from Db.Auth import Auth
from Db.Database import Database
from Game.Game import Game


def main():
    database = Database()
    database.create_tables()
    user = Auth(database.get_session()).handle()

    game = Game(database.get_session(), user)
    game.start()


if __name__ == "__main__":
    main()
