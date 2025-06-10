from sqlmodel import create_engine, Session
from redis import Redis

DATABASE_URL = "sqlite:///db.sqlite"
REDIS_HOST = "localhost"
REDIS_PORT = 6379


class DatabaseConnection:
    # singleton database connection because we want only one instance that is reused
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "db"):
            self.db = None

        if not hasattr(self, "redis"):
            self.redis = None

    def init_db(self):
        if self.db is None:
            self.db = create_engine(DATABASE_URL, echo=True)

        if self.redis is None:
            self.redis = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

    def get_session(self):
        engine = self.db
        with Session(engine) as session:
            yield session

    def close_db(self):
        if self.redis:
            self.redis.close()
