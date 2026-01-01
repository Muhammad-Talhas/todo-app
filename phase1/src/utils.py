"""Input validation and formatting helpers for Phase I Todo Application"""


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
