from sqlalchemy import Column, Integer, String, PickleType
import bcrypt

from Db.Base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True)
    _password = Column(String, name="password")
    hero = Column(PickleType, name="hero")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(12))
