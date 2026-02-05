from sqlmodel import SQLModel, create_engine, Session # Use SQLModel's create_engine
from sqlalchemy.pool import QueuePool
from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager
import os
from dotenv import load_dotenv

load_dotenv()

# Database URL from environment variable
DATABASE_URL = os.getenv("database_url")

# Use SQLModel's engine
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,
    pool_recycle=300,
    echo=False
)

# --- ADD THIS FUNCTION HERE ---
def create_db_and_tables():
    """Initializes the database and creates all tables defined in models"""
    # This is what main.py was looking for!
    SQLModel.metadata.create_all(engine)
# ------------------------------

def get_session():
    """Yield a database session"""
    with Session(engine) as session:
        yield session

@contextmanager
def get_db_transaction():
    """Context manager for database transactions"""
    session = Session(engine)
    try:
        yield session
        session.commit()
    except SQLAlchemyError:
        session.rollback()
        raise
    finally:
        session.close()