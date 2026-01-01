"""Unit tests for Task class"""

import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from task import Task


def test_task_creation():
    """Test creating a task with valid parameters."""
    task = Task(id=1, title="Test Task", description="Test Description", completed=False)
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed is False


def test_task_default_values():
    """Test task creation with default values."""
    task = Task(id=1, title="Test Task")
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == ""
    assert task.completed is False


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


def test_task_str_representation():
    """Test string representation of task."""
    task = Task(id=1, title="Test Task", description="Test Desc", completed=True)
    str_repr = str(task)
    assert "[1]" in str_repr
    assert "✓" in str_repr
    assert "Test Task" in str_repr
    assert "Test Desc" in str_repr

    task.incomplete = False  # Make it incomplete
    task.completed = False
    str_repr = str(task)
    assert "○" in str_repr
