"""In-memory task storage and CRUD operations for Phase I Todo Application"""

from typing import List, Optional
from task import Task


class TaskManager:
    """Manages in-memory storage and CRUD operations for Task objects."""

    def __init__(self) -> None:
        """Initialize empty task collection and ID counter."""
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """Add a new task with auto-generated ID.

        Args:
            title: Non-empty string for task title
            description: Optional string for task description

        Returns:
            Task object with unique ID

        Raises:
            ValueError: If title is empty or whitespace only
        """
        task = Task(
            id=self.next_id,
            title=title,
            description=description,
            completed=False
        )
        self.tasks.append(task)
        self.next_id += 1
        return task

    def view_all_tasks(self) -> List[Task]:
        """Return all tasks in insertion order.

        Returns:
            Copy of tasks list (prevents external modification)
        """
        return list(self.tasks)

    def view_tasks_by_status(self, completed: bool) -> List[Task]:
        """Return tasks filtered by completion status.

        Args:
            completed: True for completed tasks, False for pending tasks

        Returns:
            List of tasks matching completion status
        """
        return [task for task in self.tasks if task.completed == completed]

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Find task by unique ID.

        Args:
            task_id: Positive integer task ID

        Returns:
            Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None
    ) -> Task:
        """Update task title and/or description.

        Args:
            task_id: Positive integer task ID
            title: Optional new title string
            description: Optional new description string

        Returns:
            Updated Task object

        Raises:
            ValueError: If task ID not found or no fields provided
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found")

        if title is None and description is None:
            raise ValueError("At least one field (title or description) must be provided")

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description

        return task

    def delete_task(self, task_id: int) -> None:
        """Delete task by unique ID.

        Args:
            task_id: Positive integer task ID

        Raises:
            ValueError: If task ID not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found")

        self.tasks.remove(task)

    def mark_task_completion(self, task_id: int, completed: bool) -> Task:
        """Update task completion status.

        Args:
            task_id: Positive integer task ID
            completed: True for complete, False for incomplete

        Returns:
            Updated Task object

        Raises:
            ValueError: If task ID not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found")

        task.completed = completed
        return task
