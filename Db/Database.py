from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Db.Base import Base


class Database:
    DATABASE_URL = "sqlite:///base.db"

    def __init__(self):
        self.engine = create_engine(self.DATABASE_URL)
        self.Session = sessionmaker(bind=self.engine)()

    def get_session(self):
        return self.Session

    def create_tables(self):
        Base.metadata.create_all(self.engine)
