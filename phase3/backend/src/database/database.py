from sqlmodel import create_engine, Session, SQLModel
from src.config import DATABASE_URL

engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    # This will create tables for all SQLModel classes
    # TODO: This should be handled by Alembic in production
    # from src.models.conversation import Conversation
    # from src.models.message import Message
    # from src.models.task import Task
    SQLModel.metadata.create_all(engine) # This line is commented out as alembic will handle this.

def get_session():
    with Session(engine) as session:
        yield session
