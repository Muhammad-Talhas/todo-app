"""Input validation and formatting helpers for Phase I Todo Application"""

from datetime import datetime


def validate_title(title: str) -> bool:
    """Validate that task title is non-empty.

    Args:
        title: Task title to validate

    Returns:
        True if valid, False otherwise
    """
    return isinstance(title, str) and title.strip() != ""


def validate_task_id(task_id: int) -> bool:
    """Validate that task ID is a positive integer.

    Args:
        task_id: Task ID to validate

    Returns:
        True if valid, False otherwise
    """
    return isinstance(task_id, int) and task_id > 0


def validate_priority(priority: str) -> bool:
    """Validate that priority is one of the allowed values.

    Args:
        priority: Priority level to validate

    Returns:
        True if valid, False otherwise
    """
    return priority in ["low", "medium", "high"]


def validate_datetime(date_str: str) -> bool:
    """Validate that date string is in the correct format.

    Args:
        date_str: Date string to validate

    Returns:
        True if valid, False otherwise
    """
    try:
        datetime.strptime(date_str, "%d-%m-%Y %H:%M")
        return True
    except ValueError:
        return False


def format_task(task) -> str:
    """Format a single task for display.

    Args:
        task: Task object to format

    Returns:
        Formatted string representation of task
    """
    return str(task)


def format_task_list(tasks) -> str:
    """Format a list of tasks for display.

    Args:
        tasks: List of Task objects to format

    Returns:
        Formatted string representation of task list
    """
    if not tasks:
        return "No tasks found"

    output = []
    for task in tasks:
        output.append(format_task(task))

    return "\n".join(output)


def format_task_statistics(stats: dict) -> str:
    """Format task statistics for display.

    Args:
        stats: Dictionary with task statistics

    Returns:
        Formatted string representation of statistics
    """
    return f"""Task Statistics:
- Total tasks: {stats['total']}
- Completed: {stats['completed']}
- Pending: {stats['pending']}
- Overdue: {stats['overdue']}
- Completion Rate: {(stats['completed']/stats['total']*100) if stats['total'] > 0 else 0:.1f}%"""


def format_priority(priority: str) -> str:
    """Format priority level with emoji.

    Args:
        priority: Priority level (low, medium, high)

    Returns:
        Formatted priority with emoji
    """
    priority_emojis = {
        "high": "🔴 High",
        "medium": "🟡 Medium",
        "low": "🟢 Low"
    }
    return priority_emojis.get(priority, priority)


def format_tags(tags: list) -> str:
    """Format list of tags for display.

    Args:
        tags: List of tags

    Returns:
        Formatted string representation of tags
    """
    if not tags:
        return "(no tags)"
    return ", ".join(tags)