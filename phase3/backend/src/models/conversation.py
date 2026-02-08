from typing import Optional
from datetime import datetime, timezone
from sqlmodel import Field, SQLModel
import uuid

class Conversation(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: uuid.UUID = Field(index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

