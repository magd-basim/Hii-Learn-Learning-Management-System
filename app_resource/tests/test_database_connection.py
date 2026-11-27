from app_resource.database.database import (engine,SessionLocal,test_database_connectionMB)
from app_resource.database.database import get_db_sessionMB

def test_database_connection():

    assert test_database_connectionMB() is True


def test_database_session():

    db = SessionLocal()

    try:
        assert db.is_active is True
    finally:
        db.close()


def test_database_engine():

    assert engine is not None


def test_get_db_session_dependency():

    db_generator = get_db_sessionMB()

    db = next(db_generator)

    assert db.is_active is True

    db_generator.close()

    assert db.is_active is False
