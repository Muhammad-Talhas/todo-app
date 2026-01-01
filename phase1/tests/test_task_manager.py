"""Unit tests for TaskManager class"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from task import Task
from task_manager import TaskManager


def test_task_manager_initialization():
    """Test initializing a TaskManager."""
    manager = TaskManager()
    assert len(manager.tasks) == 0
    assert manager.next_id == 1


def test_add_task():
    """Test adding a task to the manager."""
    manager = TaskManager()
    task = manager.add_task("Test Title", "Test Description")

    assert task.id == 1
    assert task.title == "Test Title"
    assert task.description == "Test Description"
    assert task.completed is False
    assert len(manager.tasks) == 1


def test_add_multiple_tasks():
    """Test adding multiple tasks with unique IDs."""
    manager = TaskManager()
    task1 = manager.add_task("Task 1")
    task2 = manager.add_task("Task 2")

    assert task1.id == 1
    assert task2.id == 2
    assert len(manager.tasks) == 2


def test_view_all_tasks():
    """Test viewing all tasks."""
    manager = TaskManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")

    all_tasks = manager.view_all_tasks()
    assert len(all_tasks) == 2


def test_view_tasks_by_status():
    """Test viewing tasks by completion status."""
    manager = TaskManager()
    task1 = manager.add_task("Task 1")  # Incomplete by default
    task2 = manager.add_task("Task 2")
    manager.mark_task_completion(task2.id, True)  # Mark as complete

    completed_tasks = manager.view_tasks_by_status(True)
    pending_tasks = manager.view_tasks_by_status(False)

    assert len(completed_tasks) == 1
    assert len(pending_tasks) == 1
    assert completed_tasks[0].completed is True
    assert pending_tasks[0].completed is False


def test_get_task_by_id():
    """Test getting a task by ID."""
    manager = TaskManager()
    task = manager.add_task("Test Task")

    found_task = manager.get_task_by_id(task.id)
    assert found_task is not None
    assert found_task.id == task.id
    assert found_task.title == task.title

    not_found_task = manager.get_task_by_id(999)
    assert not_found_task is None


def test_update_task():
    """Test updating a task."""
    manager = TaskManager()
    task = manager.add_task("Old Title", "Old Description")

    updated_task = manager.update_task(task.id, "New Title", "New Description")
    assert updated_task.title == "New Title"
    assert updated_task.description == "New Description"


def test_update_task_partial():
    """Test updating only title or description."""
    manager = TaskManager()
    task = manager.add_task("Original Title", "Original Description")

    # Update only title
    updated_task = manager.update_task(task.id, title="New Title")
    assert updated_task.title == "New Title"
    assert updated_task.description == "Original Description"

    # Update only description
    updated_task = manager.update_task(task.id, description="New Description")
    assert updated_task.title == "New Title"
    assert updated_task.description == "New Description"


def test_delete_task():
    """Test deleting a task."""
    manager = TaskManager()
    task = manager.add_task("Test Task")

    assert len(manager.tasks) == 1
    manager.delete_task(task.id)
    assert len(manager.tasks) == 0

    # Verify task is gone
    assert manager.get_task_by_id(task.id) is None


def test_mark_task_completion():
    """Test marking task completion."""
    manager = TaskManager()
    task = manager.add_task("Test Task")

    # Initially incomplete
    assert task.completed is False

    # Mark as complete
    completed_task = manager.mark_task_completion(task.id, True)
    assert completed_task.completed is True

    # Mark as incomplete
    incomplete_task = manager.mark_task_completion(task.id, False)
    assert incomplete_task.completed is False
