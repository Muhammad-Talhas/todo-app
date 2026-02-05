"""Unit tests for Task class"""

import pytest
import sys
import os
from datetime import datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from task import Task, Priority


def test_task_creation():
    """Test creating a task with valid parameters."""
    task = Task(
        id=1,
        title="Test Task",
        description="Test Description",
        completed=False,
        priority=Priority.HIGH,
        tags=["work", "urgent"],
        due_date=datetime(2026, 12, 31, 23, 59)
    )
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed is False
    assert task.priority == Priority.HIGH
    assert "work" in task.tags
    assert "urgent" in task.tags
    assert task.due_date == datetime(2026, 12, 31, 23, 59)


def test_task_default_values():
    """Test task creation with default values."""
    task = Task(id=1, title="Test Task")
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == ""
    assert task.completed is False
    assert task.priority == Priority.MEDIUM
    assert task.tags == []
    assert task.due_date is None
    assert task.recurring is False
    assert task.recurrence_pattern is None
    assert task.created_at is not None


def test_task_mark_complete():
    """Test marking task as complete."""
    task = Task(id=1, title="Test Task")
    task.mark_complete()
    assert task.completed is True


def test_task_mark_incomplete():
    """Test marking task as incomplete."""
    task = Task(id=1, title="Test Task", completed=True)
    task.mark_incomplete()
    assert task.completed is False


def test_task_toggle_completion():
    """Test toggling task completion status."""
    task = Task(id=1, title="Test Task", completed=False)
    task.toggle_completion()
    assert task.completed is True
    task.toggle_completion()
    assert task.completed is False


def test_task_validation():
    """Test task validation."""
    # Test valid task
    task = Task(id=1, title="Valid Task")
    assert task.id == 1
    assert task.title == "Valid Task"

    # Test invalid ID
    try:
        Task(id=-1, title="Invalid ID")
        assert False, "Should raise ValueError for negative ID"
    except ValueError:
        pass

    # Test empty title
    try:
        Task(id=1, title="")
        assert False, "Should raise ValueError for empty title"
    except ValueError:
        pass

    # Test invalid priority
    try:
        Task(id=1, title="Test", priority="invalid_priority")
        assert False, "Should raise ValueError for invalid priority"
    except ValueError:
        pass


def test_task_str_representation():
    """Test string representation of task."""
    task = Task(
        id=1,
        title="Test Task",
        description="Test Desc",
        completed=True,
        priority=Priority.HIGH,
        tags=["work"],
        due_date=datetime(2026, 12, 31, 10, 30)
    )
    str_repr = str(task)
    assert "[1]" in str_repr
    assert "✓" in str_repr
    assert "🔴" in str_repr  # High priority
    assert "Test Task" in str_repr
    assert "Test Desc" in str_repr
    assert "Due: 31-12-2026 10:30" in str_repr
    assert "Tags: work" in str_repr


def test_add_and_remove_tags():
    """Test adding and removing tags."""
    task = Task(id=1, title="Test Task", tags=[])

    # Add tag
    task.add_tag("work")
    assert "work" in task.tags

    # Add duplicate tag (should not add)
    original_count = len(task.tags)
    task.add_tag("work")
    assert len(task.tags) == original_count  # Count should not change

    # Remove tag
    task.remove_tag("work")
    assert "work" not in task.tags


def test_set_due_date():
    """Test setting due date."""
    task = Task(id=1, title="Test Task")
    new_date = datetime(2026, 12, 31, 15, 30)
    task.set_due_date(new_date)
    assert task.due_date == new_date


def test_is_overdue():
    """Test checking if task is overdue."""
    from datetime import datetime, timedelta

    # Task with due date in past
    past_date = datetime.now() - timedelta(days=1)
    task_past = Task(
        id=1,
        title="Past Task",
        due_date=past_date,
        completed=False
    )
    assert task_past.is_overdue() is True

    # Task with due date in future
    future_date = datetime.now() + timedelta(days=1)
    task_future = Task(
        id=2,
        title="Future Task",
        due_date=future_date,
        completed=False
    )
    assert task_future.is_overdue() is False

    # Completed task with past due date
    task_completed = Task(
        id=3,
        title="Completed Task",
        due_date=past_date,
        completed=True
    )
    assert task_completed.is_overdue() is False  # Completed tasks are not overdue

    # Task without due date
    task_no_due = Task(id=4, title="No Due Date Task", due_date=None)
    assert task_no_due.is_overdue() is False
