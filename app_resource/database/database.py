from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from core.config import settings


engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_pre_ping=True
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False
)


def get_db_sessionMB():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def test_database_connectionMB() -> bool:

    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return True
