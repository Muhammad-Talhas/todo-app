from typing import Optional
from datetime import datetime, timezone
from sqlmodel import Field, SQLModel
import uuid

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    description: Optional[str] = None
    status: str = Field(default="pending") # e.g., "pending", "completed"
    user_id: uuid.UUID = Field(index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
