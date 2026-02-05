"""Unit tests for TaskManager class"""

import sys
import os
from datetime import datetime
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from task import Task, Priority
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
    assert task.priority == Priority.MEDIUM
    assert len(task.tags) == 0
    assert task.due_date is None
    assert len(manager.tasks) == 1


def test_add_task_with_features():
    """Test adding a task with all new features."""
    manager = TaskManager()
    due_date = datetime(2026, 12, 31, 15, 30)
    task = manager.add_task(
        "Test Title",
        "Test Description",
        priority=Priority.HIGH,
        tags=["work", "urgent"],
        due_date=due_date,
        recurring=True,
        recurrence_pattern="weekly"
    )

    assert task.id == 1
    assert task.title == "Test Title"
    assert task.description == "Test Description"
    assert task.completed is False
    assert task.priority == Priority.HIGH
    assert "work" in task.tags
    assert "urgent" in task.tags
    assert task.due_date == due_date
    assert task.recurring is True
    assert task.recurrence_pattern == "weekly"
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
    """Test updating a task with all fields."""
    manager = TaskManager()
    task = manager.add_task("Old Title", "Old Description")

    updated_task = manager.update_task(
        task.id,
        title="New Title",
        description="New Description",
        priority=Priority.HIGH,
        tags=["updated", "task"],
        due_date=datetime(2026, 12, 31, 10, 30)
    )
    assert updated_task.title == "New Title"
    assert updated_task.description == "New Description"
    assert updated_task.priority == Priority.HIGH
    assert "updated" in updated_task.tags
    assert "task" in updated_task.tags
    assert updated_task.due_date == datetime(2026, 12, 31, 10, 30)


def test_update_task_partial():
    """Test updating only specific fields."""
    manager = TaskManager()
    task = manager.add_task("Original Title", "Original Description", priority=Priority.LOW)

    # Update only title
    updated_task = manager.update_task(task.id, title="New Title")
    assert updated_task.title == "New Title"
    assert updated_task.description == "Original Description"
    assert updated_task.priority == Priority.LOW  # Should remain unchanged

    # Update only priority
    updated_task = manager.update_task(task.id, priority=Priority.HIGH)
    assert updated_task.title == "New Title"
    assert updated_task.priority == Priority.HIGH


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


def test_add_and_remove_tags():
    """Test adding and removing tags from tasks."""
    manager = TaskManager()
    task = manager.add_task("Test Task")

    # Add tag
    tagged_task = manager.add_tag_to_task(task.id, "work")
    assert "work" in tagged_task.tags

    # Remove tag
    untagged_task = manager.remove_tag_from_task(task.id, "work")
    assert "work" not in untagged_task.tags


def test_filter_by_priority():
    """Test filtering tasks by priority."""
    manager = TaskManager()
    manager.add_task("High Priority Task", priority=Priority.HIGH)
    manager.add_task("Medium Priority Task", priority=Priority.MEDIUM)
    manager.add_task("Another High Priority Task", priority=Priority.HIGH)

    high_tasks = manager.view_tasks_by_priority(Priority.HIGH)
    medium_tasks = manager.view_tasks_by_priority(Priority.MEDIUM)

    assert len(high_tasks) == 2
    assert len(medium_tasks) == 1
    assert all(task.priority == Priority.HIGH for task in high_tasks)
    assert all(task.priority == Priority.MEDIUM for task in medium_tasks)


def test_filter_by_tag():
    """Test filtering tasks by tag."""
    manager = TaskManager()
    manager.add_task("Work Task", tags=["work"])
    manager.add_task("Personal Task", tags=["personal"])
    manager.add_task("Work & Urgent Task", tags=["work", "urgent"])

    work_tasks = manager.view_tasks_by_tag("work")
    urgent_tasks = manager.view_tasks_by_tag("urgent")

    assert len(work_tasks) == 2  # Both "Work Task" and "Work & Urgent Task"
    assert len(urgent_tasks) == 1  # Only "Work & Urgent Task"


def test_view_overdue_tasks():
    """Test viewing overdue tasks."""
    from datetime import datetime, timedelta

    manager = TaskManager()

    # Past due date task (not completed)
    past_date = datetime.now() - timedelta(days=1)
    manager.add_task("Overdue Task", due_date=past_date)
    # The task is incomplete by default, so no need to mark it

    # Past due date task (completed)
    completed_task = manager.add_task("Completed Past Task", due_date=past_date)
    manager.mark_task_completion(completed_task.id, True)

    # Future due date task
    future_date = datetime.now() + timedelta(days=1)
    manager.add_task("Future Task", due_date=future_date)
    # The task is incomplete by default

    # Task without due date
    manager.add_task("No Due Task")

    overdue_tasks = manager.view_overdue_tasks()

    assert len(overdue_tasks) == 1
    assert overdue_tasks[0].title == "Overdue Task"


def test_search_tasks():
    """Test searching tasks by keyword."""
    manager = TaskManager()
    manager.add_task("Buy groceries", "Get milk, eggs, bread")
    manager.add_task("Finish report", "Complete quarterly report")
    manager.add_task("Call mom", "Call mother for birthday")

    # Search in title
    results = manager.search_tasks("report")
    assert len(results) == 1
    assert results[0].title == "Finish report"

    # Search in description
    results = manager.search_tasks("milk")
    assert len(results) == 1
    assert results[0].title == "Buy groceries"

    # Case-insensitive search
    results = manager.search_tasks("MOM")
    assert len(results) == 1
    assert results[0].title == "Call mom"


def test_sort_tasks():
    """Test sorting tasks."""
    # Test priority sorting
    priority_manager = TaskManager()
    priority_manager.add_task("Low Priority", priority=Priority.LOW)
    priority_manager.add_task("High Priority", priority=Priority.HIGH)
    priority_manager.add_task("Medium Priority", priority=Priority.MEDIUM)

    # Sort by priority (high to low)
    priority_sorted = priority_manager.sort_tasks_by_priority()
    assert priority_sorted[0].priority == Priority.HIGH
    assert priority_sorted[-1].priority == Priority.LOW

    # Test due date sorting
    date_manager = TaskManager()
    date_manager.add_task("Early Due", due_date=datetime(2026, 1, 1))
    date_manager.add_task("Late Due", due_date=datetime(2026, 12, 31))
    date_manager.add_task("Mid Due", due_date=datetime(2026, 6, 15))

    # Sort by due date (earliest first)
    date_sorted = date_manager.sort_tasks_by_due_date()
    assert date_sorted[0].title == "Early Due"
    assert date_sorted[-1].title == "Late Due"

    # Test alphabetical sorting
    alpha_manager = TaskManager()
    alpha_manager.add_task("Alpha Task")
    alpha_manager.add_task("Beta Task")
    alpha_manager.add_task("Aardvark Task")  # Will be first alphabetically

    alpha_sorted = alpha_manager.sort_tasks_alphabetically()
    assert alpha_sorted[0].title == "Aardvark Task"
    assert alpha_sorted[-1].title == "Beta Task"


def test_get_task_statistics():
    """Test getting task statistics."""
    from datetime import datetime, timedelta

    manager = TaskManager()

    # Add various tasks
    completed_task = manager.add_task("Completed Task")
    manager.mark_task_completion(completed_task.id, True)
    manager.add_task("Pending Task")  # Incomplete by default

    # Add overdue task
    past_date = datetime.now() - timedelta(days=1)
    manager.add_task("Overdue Task", due_date=past_date)  # Incomplete by default

    stats = manager.get_task_statistics()

    assert stats["total"] == 3
    assert stats["completed"] == 1
    assert stats["pending"] == 2
    assert stats["overdue"] == 1
