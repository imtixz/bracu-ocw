from sqlmodel import create_engine, Session

DATABASE_URL = "sqlite:///db.sqlite"


class DatabaseConnection:
    # singleton database connection because we want only one instance that is reused
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "engine"):
            self.engine = None

    def init_db(self):
        if self.engine is None:
            self.engine = create_engine(DATABASE_URL, echo=True)

    def get_session(self):
        engine = self.engine
        with Session(engine) as session:
            yield session
