"""Task entity class for Phase I Todo Application"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


class Priority:
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class Task:
    """Represents a todo item with unique ID, title, description, and completion status."""
    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: str = Priority.MEDIUM  # low, medium, high
    tags: list = None  # list of category labels
    due_date: Optional[datetime] = None  # deadline for the task
    recurring: bool = False  # whether task repeats
    recurrence_pattern: Optional[str] = None  # e.g., "daily", "weekly", "monthly"
    created_at: datetime = None  # timestamp when task was created

    def __post_init__(self):
        """Validate task fields after initialization."""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("Task ID must be a positive integer")
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("Task title must be a non-empty string")
        if not isinstance(self.description, str):
            raise ValueError("Task description must be a string")
        if not isinstance(self.completed, bool):
            raise ValueError("Task completed status must be a boolean")
        if self.priority not in [Priority.LOW, Priority.MEDIUM, Priority.HIGH]:
            raise ValueError(f"Priority must be one of: {Priority.LOW}, {Priority.MEDIUM}, {Priority.HIGH}")
        if self.tags is None:
            self.tags = []
        if not isinstance(self.tags, list):
            raise ValueError("Tags must be a list")
        if self.created_at is None:
            self.created_at = datetime.now()

    def mark_complete(self) -> None:
        """Mark task as completed."""
        self.completed = True

    def mark_incomplete(self) -> None:
        """Mark task as incomplete."""
        self.completed = False

    def toggle_completion(self) -> None:
        """Toggle completion status between True and False."""
        self.completed = not self.completed

    def add_tag(self, tag: str) -> None:
        """Add a tag to the task."""
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str) -> None:
        """Remove a tag from the task."""
        if tag in self.tags:
            self.tags.remove(tag)

    def set_due_date(self, due_date: datetime) -> None:
        """Set the due date for the task."""
        self.due_date = due_date

    def is_overdue(self) -> bool:
        """Check if the task is overdue."""
        if self.due_date is None or self.completed:
            return False
        return self.due_date < datetime.now()

    def __str__(self) -> str:
        """Return human-readable string representation of task."""
        status = "✓" if self.completed else "○"
        priority_symbol = {"high": "🔴", "medium": "🟡", "low": "🟢"}[self.priority]
        desc = self.description if self.description else "(no description)"

        # Format due date if present
        due_str = ""
        if self.due_date:
            due_str = f" [Due: {self.due_date.strftime('%d-%m-%Y %H:%M')}]"

        # Format tags if present
        tags_str = ""
        if self.tags:
            tags_str = f" [Tags: {', '.join(self.tags)}]"

        # Format recurring if applicable
        recur_str = " [🔄]" if self.recurring else ""

        return f"[{self.id}] {status} {priority_symbol} {self.title} - {desc}{due_str}{tags_str}{recur_str}"