from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
from sqlmodel import Session
from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager
import os
from dotenv import load_dotenv

load_dotenv()

# Database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine with connection pooling settings appropriate for Neon
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,  # Verify connections before use
    pool_recycle=300,    # Recycle connections every 5 minutes
    echo=False           # Set to True for SQL debugging
)

def get_session():
    """Yield a database session"""
    with Session(engine) as session:
        yield session

@contextmanager
def get_db_transaction():
    """Context manager for database transactions with automatic rollback on exception."""
    session = Session(engine)
    try:
        yield session
        session.commit()
    except SQLAlchemyError:
        session.rollback()
        raise
    finally:
        session.close()

def execute_in_transaction(func, *args, **kwargs):
    """Execute a function within a database transaction."""
    with get_db_transaction() as session:
        return func(session, *args, **kwargs)