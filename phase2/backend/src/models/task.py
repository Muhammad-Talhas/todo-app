from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING, Union
from datetime import datetime

# This block only runs for Pylance/VS Code, not at runtime
if TYPE_CHECKING:
    from .user import User

class TaskBase(SQLModel):
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None)
    completed: bool = Field(default=False)
    user_id: str 
    # Use 'nullable=True' and ensure the type is strictly Optional
    due_date: Optional[datetime] = Field(default=None, nullable=True)

class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: str = Field(foreign_key="user.id", index=True)
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Use the string "User" here so SQLModel knows what to link to 
    # even if the class isn't fully imported yet.
    user: Optional["User"] = Relationship(back_populates="tasks")

class TaskCreate(SQLModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    # If the frontend is stubborn, we allow it to be a string OR datetime
    due_date: Optional[Union[datetime, str]] = None

class TaskRead(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime
    # Add these two lines to explicitly allow None in the response
    description: Optional[str] = None
    due_date: Optional[datetime] = None

class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    # Use Union or just keep as Optional[datetime] but ensure frontend sends null, not ""
    due_date: Optional[datetime] = None

class TaskPatch(SQLModel):
    completed: Optional[bool] = None

