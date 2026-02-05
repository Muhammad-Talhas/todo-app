from sqlmodel import SQLModel, Field, Relationship # Added Relationship
from typing import Optional, List, TYPE_CHECKING # Added List, TYPE_CHECKING
from datetime import datetime

# This prevents the "Task is not defined" error and circular imports
if TYPE_CHECKING:
    from .task import Task

class UserBase(SQLModel):
    email: str = Field(unique=True, nullable=False)
    name: Optional[str] = Field(default=None)

class User(UserBase, table=True):
    # 1. Change to str to match Better Auth IDs and Task.user_id
    id: str = Field(primary_key=True) 
    
    password_hash: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True)

    # 2. THE MISSING LINK: Tell SQLAlchemy how to find this user's tasks
    tasks: List["Task"] = Relationship(back_populates="user")

# Update UserRead to match the new id type
class UserRead(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime
    is_active: bool