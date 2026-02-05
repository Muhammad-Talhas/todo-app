"""Unit tests for utility functions"""

import sys
import os
from datetime import datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from task import Task, Priority
from utils import (
    validate_title, validate_task_id, validate_priority, validate_datetime,
    format_task, format_task_list, format_task_statistics, format_priority, format_tags
)


def test_validate_title():
    """Test title validation."""
    # Valid titles
    assert validate_title("Valid Title") is True
    assert validate_title("  Valid Title With Spaces  ") is True

    # Invalid titles
    assert validate_title("") is False
    assert validate_title("   ") is False  # Only whitespace
    assert validate_title(None) is False  # Would cause TypeError in isinstance check


def test_validate_task_id():
    """Test task ID validation."""
    # Valid IDs
    assert validate_task_id(1) is True
    assert validate_task_id(100) is True
    assert validate_task_id(999999) is True

    # Invalid IDs
    assert validate_task_id(0) is False
    assert validate_task_id(-1) is False
    assert validate_task_id(-100) is False
    assert validate_task_id("1") is False  # String instead of int
    assert validate_task_id(1.5) is False  # Float instead of int


def test_validate_priority():
    """Test priority validation."""
    # Valid priorities
    assert validate_priority("low") is True
    assert validate_priority("medium") is True
    assert validate_priority("high") is True

    # Invalid priorities
    assert validate_priority("LOW") is False  # Case sensitive
    assert validate_priority("HIGH") is False  # Case sensitive
    assert validate_priority("invalid") is False
    assert validate_priority("") is False


def test_validate_datetime():
    """Test datetime validation."""
    # Valid datetime strings
    assert validate_datetime("01-01-2026 12:00") is True
    assert validate_datetime("31-12-2026 23:59") is True
    assert validate_datetime("28-02-2026 00:00") is True

    # Invalid datetime strings
    assert validate_datetime("01-13-2026 12:00") is False  # Invalid month
    assert validate_datetime("32-01-2026 12:00") is False  # Invalid day
    assert validate_datetime("01-01-2026 25:00") is False  # Invalid hour
    assert validate_datetime("01-01-2026 12:60") is False  # Invalid minute
    assert validate_datetime("invalid-format") is False
    assert validate_datetime("") is False


def test_format_task():
    """Test task formatting."""
    task = Task(
        id=1,
        title="Test Task",
        description="Test Description",
        completed=True,
        priority=Priority.HIGH,
        tags=["work", "urgent"],
        due_date=datetime(2026, 12, 31, 10, 30)
    )
    formatted = format_task(task)

    assert "[1]" in formatted
    assert "✓" in formatted
    assert "🔴" in formatted  # High priority
    assert "Test Task" in formatted
    assert "Test Description" in formatted
    assert "Due: 31-12-2026 10:30" in formatted
    assert "Tags: work, urgent" in formatted

    # Test with incomplete task
    task.completed = False
    formatted = format_task(task)
    assert "○" in formatted


def test_format_task_minimal():
    """Test task formatting with minimal information."""
    task = Task(id=1, title="Test Task", description="", completed=False, priority=Priority.LOW)
    formatted = format_task(task)

    assert "[1]" in formatted
    assert "○" in formatted
    assert "🟢" in formatted  # Low priority
    assert "Test Task" in formatted
    assert "(no description)" in formatted
    assert "Tags:" not in formatted  # No tags
    assert "Due:" not in formatted  # No due date


def test_format_task_list():
    """Test task list formatting."""
    # Test with empty list
    empty_list = format_task_list([])
    assert empty_list == "No tasks found"

    # Test with tasks
    task1 = Task(id=1, title="Task 1", description="Description 1", completed=True)
    task2 = Task(id=2, title="Task 2", description="Description 2", completed=False)
    tasks = [task1, task2]

    formatted_list = format_task_list(tasks)
    assert "[1]" in formatted_list
    assert "[2]" in formatted_list
    assert "✓" in formatted_list
    assert "○" in formatted_list
    assert "Task 1" in formatted_list
    assert "Task 2" in formatted_list


def test_format_task_statistics():
    """Test task statistics formatting."""
    stats = {
        "total": 10,
        "completed": 7,
        "pending": 3,
        "overdue": 2
    }
    formatted = format_task_statistics(stats)

    assert "Total tasks: 10" in formatted
    assert "Completed: 7" in formatted
    assert "Pending: 3" in formatted
    assert "Overdue: 2" in formatted
    assert "Completion Rate: 70.0%" in formatted

    # Test with no tasks
    empty_stats = {
        "total": 0,
        "completed": 0,
        "pending": 0,
        "overdue": 0
    }
    formatted_empty = format_task_statistics(empty_stats)
    assert "Completion Rate: 0.0%" in formatted_empty


def test_format_priority():
    """Test priority formatting."""
    assert "🔴 High" in format_priority(Priority.HIGH)
    assert "🟡 Medium" in format_priority(Priority.MEDIUM)
    assert "🟢 Low" in format_priority(Priority.LOW)

    # Test invalid priority
    assert "invalid_priority" in format_priority("invalid_priority")


def test_format_tags():
    """Test tags formatting."""
    # Test with tags
    assert format_tags(["work", "urgent"]) == "work, urgent"

    # Test with empty tags
    assert "(no tags)" in format_tags([])

    # Test with single tag
    assert format_tags(["work"]) == "work"
