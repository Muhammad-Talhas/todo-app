"""In-memory task storage and CRUD operations for Phase I Todo Application"""

from typing import List, Optional
from datetime import datetime
from task import Task, Priority


class TaskManager:
    """Manages in-memory storage and CRUD operations for Task objects."""

    def __init__(self) -> None:
        """Initialize empty task collection and ID counter."""
        self.tasks: List[Task] = []
        self.next_id: int = 1

    def add_task(
        self,
        title: str,
        description: str = "",
        priority: str = Priority.MEDIUM,
        tags: List[str] = None,
        due_date: Optional[datetime] = None,
        recurring: bool = False,
        recurrence_pattern: Optional[str] = None
    ) -> Task:
        """Add a new task with auto-generated ID.

        Args:
            title: Non-empty string for task title
            description: Optional string for task description
            priority: Priority level (low, medium, high)
            tags: Optional list of tags/labels
            due_date: Optional due date for the task
            recurring: Whether the task repeats
            recurrence_pattern: Pattern for recurrence (e.g., daily, weekly)

        Returns:
            Task object with unique ID

        Raises:
            ValueError: If title is empty or whitespace only
        """
        if tags is None:
            tags = []

        task = Task(
            id=self.next_id,
            title=title,
            description=description,
            completed=False,
            priority=priority,
            tags=tags,
            due_date=due_date,
            recurring=recurring,
            recurrence_pattern=recurrence_pattern
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
        description: Optional[str] = None,
        priority: Optional[str] = None,
        tags: Optional[List[str]] = None,
        due_date: Optional[datetime] = None
    ) -> Task:
        """Update task fields.

        Args:
            task_id: Positive integer task ID
            title: Optional new title string
            description: Optional new description string
            priority: Optional new priority level
            tags: Optional new list of tags
            due_date: Optional new due date

        Returns:
            Updated Task object

        Raises:
            ValueError: If task ID not found or no fields provided
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found")

        # Track if any field was updated
        updated = False

        if title is not None:
            task.title = title
            updated = True
        if description is not None:
            task.description = description
            updated = True
        if priority is not None:
            task.priority = priority
            updated = True
        if tags is not None:
            task.tags = tags
            updated = True
        if due_date is not None:
            task.due_date = due_date
            updated = True

        if not updated:
            raise ValueError("At least one field must be provided for update")

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

    def add_tag_to_task(self, task_id: int, tag: str) -> Task:
        """Add a tag to a task.

        Args:
            task_id: Positive integer task ID
            tag: Tag to add to the task

        Returns:
            Updated Task object

        Raises:
            ValueError: If task ID not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found")

        task.add_tag(tag)
        return task

    def remove_tag_from_task(self, task_id: int, tag: str) -> Task:
        """Remove a tag from a task.

        Args:
            task_id: Positive integer task ID
            tag: Tag to remove from the task

        Returns:
            Updated Task object

        Raises:
            ValueError: If task ID not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            raise ValueError(f"Task with ID {task_id} not found")

        task.remove_tag(tag)
        return task

    def view_tasks_by_priority(self, priority: str) -> List[Task]:
        """Return tasks filtered by priority level.

        Args:
            priority: Priority level to filter by (low, medium, high)

        Returns:
            List of tasks with matching priority
        """
        return [task for task in self.tasks if task.priority == priority]

    def view_tasks_by_tag(self, tag: str) -> List[Task]:
        """Return tasks filtered by tag.

        Args:
            tag: Tag to filter tasks by

        Returns:
            List of tasks containing the specified tag
        """
        return [task for task in self.tasks if tag in task.tags]

    def view_overdue_tasks(self) -> List[Task]:
        """Return tasks that are past their due date and not completed.

        Returns:
            List of overdue tasks
        """
        return [task for task in self.tasks if task.is_overdue()]

    def search_tasks(self, keyword: str) -> List[Task]:
        """Search tasks by keyword in title or description.

        Args:
            keyword: Keyword to search for

        Returns:
            List of tasks matching the keyword
        """
        keyword_lower = keyword.lower()
        return [
            task for task in self.tasks
            if keyword_lower in task.title.lower() or
            keyword_lower in task.description.lower()
        ]

    def sort_tasks_by_priority(self) -> List[Task]:
        """Return tasks sorted by priority (high to low).

        Returns:
            List of tasks sorted by priority
        """
        priority_order = {Priority.HIGH: 0, Priority.MEDIUM: 1, Priority.LOW: 2}
        return sorted(self.tasks, key=lambda t: priority_order[t.priority])

    def sort_tasks_by_due_date(self) -> List[Task]:
        """Return tasks sorted by due date (earliest first).

        Returns:
            List of tasks sorted by due date
        """
        return sorted(
            self.tasks,
            key=lambda t: t.due_date if t.due_date else datetime.max
        )

    def sort_tasks_alphabetically(self) -> List[Task]:
        """Return tasks sorted alphabetically by title.

        Returns:
            List of tasks sorted alphabetically
        """
        return sorted(self.tasks, key=lambda t: t.title.lower())

    def get_task_statistics(self) -> dict:
        """Get statistics about tasks.

        Returns:
            Dictionary with task statistics
        """
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task.completed)
        pending = total - completed
        overdue = sum(1 for task in self.tasks if task.is_overdue())

        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "overdue": overdue
        }