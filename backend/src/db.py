from sqlmodel import create_engine, Session
# from models import SQLModel

DATABASE_URL = 'sqlite:///db.sqlite'

class DatabaseConnection:
    _engine = None

    @classmethod
    def init_db(cls):
        if cls._engine is None:
            cls._engine = create_engine(DATABASE_URL, echo=True)

    @classmethod
    def get_engine(cls):
        if cls._engine is None:
            cls._engine = create_engine(DATABASE_URL, echo=True)
        return cls._engine

    @classmethod
    def get_session(cls):
        engine = cls.get_engine()
        with Session(engine) as session:
            yield session