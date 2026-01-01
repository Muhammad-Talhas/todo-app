"""Task entity class for Phase I Todo Application"""

from dataclasses import dataclass


@dataclass
class Task:
    """Represents a todo item with unique ID, title, description, and completion status."""
    id: int
    title: str
    description: str = ""
    completed: bool = False

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

    def mark_complete(self) -> None:
        """Mark task as completed."""
        self.completed = True

    def mark_incomplete(self) -> None:
        """Mark task as incomplete."""
        self.completed = False

    def toggle_completion(self) -> None:
        """Toggle completion status between True and False."""
        self.completed = not self.completed

    def __str__(self) -> str:
        """Return human-readable string representation of task."""
        status = "✓" if self.completed else "○"
        desc = self.description if self.description else "(no description)"
        return f"[{self.id}] {status} {self.title} - {desc}"
