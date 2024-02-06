import bcrypt
import getpass
from sqlalchemy.orm import Session

from Db.User import User
from UserPrompts.UserPrompts import get_user_input


class Auth:
    db: Session

    def __init__(self, db: Session):
        self.db = db

    def __get_valid_input(self, prompt: str, is_hidden: bool = False) -> str:
        if is_hidden:
            input_value = getpass.getpass(prompt)
        else:
            input_value = get_user_input(prompt, False)
        while not input_value.strip():
            print("This field cannot be blank. Please try again.")
            input_value = get_user_input(prompt, is_hidden)
        return input_value

    def handle(self) -> User:
        while True:
            action = get_user_input("Login or register (login/register): ").lower()
            if action == "login":
                username = self.__get_valid_input("Username: ")
                password = self.__get_valid_input("Password: ", True)
                user = self.__login(username, password)
                if user:
                    print("Login successful!")
                    return user
                else:
                    print(
                        "Incorrect username or password. Try again or switch to register."
                    )
            elif action == "register":
                username = get_user_input("Username: ")
                password = self.__get_valid_input("Password: ", True)
                password_repeat = self.__get_valid_input("Repeat password: ", True)
                if password == password_repeat:
                    user = self.__register(username, password)
                    if user:
                        print("Registration successful! You can now login.")
                        return user
                else:
                    print("Passwords do not match. Try again.")
            else:
                print("Invalid action. Please choose 'login' or 'register'.")

    def __login(self, username, password) -> User | bool:
        user = self.db.query(User).filter(User.username == username).first()
        if user and bcrypt.checkpw(password.encode("utf-8"), user.password):
            return user
        return False

    def __register(self, username, password) -> User | bool:
        if self.db.query(User).filter(User.username == username).first():
            print(
                f"Username '{username}' is already taken. Please choose a different one."
            )
            return False
        user = User(username=username, password=password)
        self.db.add(user)
        self.db.commit()
        return user
