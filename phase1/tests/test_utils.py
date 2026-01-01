"""Unit tests for utility functions"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from task import Task
from utils import validate_title, validate_task_id, format_task, format_task_list


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


def test_format_task():
    """Test task formatting."""
    task = Task(id=1, title="Test Task", description="Test Description", completed=True)
    formatted = format_task(task)

    assert "[1]" in formatted
    assert "✓" in formatted
    assert "Test Task" in formatted
    assert "Test Description" in formatted

    # Test with incomplete task
    task.completed = False
    formatted = format_task(task)
    assert "○" in formatted


def test_format_task_no_description():
    """Test task formatting with no description."""
    task = Task(id=1, title="Test Task", description="", completed=False)
    formatted = format_task(task)

    assert "[1]" in formatted
    assert "○" in formatted
    assert "Test Task" in formatted
    assert "(no description)" in formatted


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
