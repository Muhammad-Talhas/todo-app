"""Console interface and entry point for Phase I Todo Application"""

import sys
from task_manager import TaskManager
from utils import validate_title, validate_task_id, format_task_list


def display_menu() -> None:
    """Display main menu options."""
    print("\n===================================================")
    print("     In-Memory Todo Console Application")
    print("===================================================\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete/Incomplete")
    print("6. Exit")
    print("\nEnter your choice (1-6):")


def display_view_menu() -> None:
    """Display view options submenu."""
    print("\nView options:")
    print("1. All Tasks")
    print("2. Completed Tasks")
    print("3. Pending Tasks")
    print("\nEnter your choice (1-3):")


def add_task(manager: TaskManager) -> None:
    """Handle adding a new task."""
    print("\n--- Add Task ---")
    title = input("Enter task title: ").strip()

    if not validate_title(title):
        print("Error: Task title cannot be empty")
        return

    description = input("Enter task description (optional, press Enter to skip): ").strip()

    try:
        task = manager.add_task(title, description)
        print(f"Task created successfully with ID {task.id}")
        print(f"  [{task.id}] ○ {title} - {description or '(no description)'}")
    except ValueError as e:
        print(f"Error: {e}")


def view_tasks(manager: TaskManager) -> None:
    """Handle viewing tasks with filtering."""
    display_view_menu()
    choice = input("\nEnter your choice (1-3): ").strip()

    if choice not in ["1", "2", "3"]:
        print("Error: Invalid choice. Please enter 1, 2, or 3")
        return

    if choice == "1":
        display_all_tasks(manager)
    elif choice == "2":
        display_filtered_tasks(manager, completed=True)
    elif choice == "3":
        display_filtered_tasks(manager, completed=False)


def display_all_tasks(manager: TaskManager) -> None:
    """Display all tasks."""
    print("\n--- All Tasks ---")
    tasks = manager.view_all_tasks()

    if not tasks:
        print("No tasks found")
    else:
        print(format_task_list(tasks))
        print(f"\nTotal: {len(tasks)} task(s)")


def display_filtered_tasks(manager: TaskManager, completed: bool) -> None:
    """Display filtered tasks by completion status."""
    status_text = "completed" if completed else "pending"
    print(f"\n--- {status_text.capitalize()} Tasks ---")

    tasks = manager.view_tasks_by_status(completed)

    if not tasks:
        print(f"No {status_text} tasks found")
    else:
        print(format_task_list(tasks))
        print(f"\nTotal: {len(tasks)} {status_text} task(s)")


def update_task(manager: TaskManager) -> None:
    """Handle updating a task."""
    print("\n--- Update Task ---")

    task_id_input = input("Enter task ID: ").strip()

    try:
        task_id = int(task_id_input)
        if not validate_task_id(task_id):
            print("Error: Task ID must be a positive integer")
            return
    except ValueError:
        print("Error: Task ID must be a positive integer")
        return

    new_title = input("Enter new title (leave empty to skip): ").strip()
    new_description = input("Enter new description (leave empty to skip): ").strip()

    if not new_title and not new_description:
        print("Error: At least one field (title or description) must be provided")
        return

    try:
        title_arg = new_title if new_title else None
        desc_arg = new_description if new_description else None
        task = manager.update_task(task_id, title_arg, desc_arg)
        print(f"Task {task_id} updated successfully")
        print(f"  [{task.id}] {'✓' if task.completed else '○'} {task.title} - {task.description or '(no description)'}")
    except ValueError as e:
        print(f"Error: {e}")


def delete_task(manager: TaskManager) -> None:
    """Handle deleting a task."""
    print("\n--- Delete Task ---")

    task_id_input = input("Enter task ID: ").strip()

    try:
        task_id = int(task_id_input)
        if not validate_task_id(task_id):
            print("Error: Task ID must be a positive integer")
            return
    except ValueError:
        print("Error: Task ID must be a positive integer")
        return

    try:
        manager.delete_task(task_id)
        print(f"Task {task_id} deleted successfully")
    except ValueError as e:
        print(f"Error: {e}")


def mark_task_completion(manager: TaskManager) -> None:
    """Handle marking task completion status."""
    print("\n--- Mark Complete/Incomplete ---")

    task_id_input = input("Enter task ID: ").strip()

    try:
        task_id = int(task_id_input)
        if not validate_task_id(task_id):
            print("Error: Task ID must be a positive integer")
            return
    except ValueError:
        print("Error: Task ID must be a positive integer")
        return

    status_input = input("Enter status (complete/incomplete): ").strip().lower()

    if status_input not in ["complete", "incomplete"]:
        print("Error: Invalid status. Please enter 'complete' or 'incomplete'")
        return

    completed = status_input == "complete"

    try:
        task = manager.mark_task_completion(task_id, completed)
        status_text = "complete" if completed else "incomplete"
        print(f"Task {task_id} marked as {status_text}")
        print(f"  [{task.id}] {'✓' if task.completed else '○'} {task.title} - {task.description or '(no description)'}")
    except ValueError as e:
        print(f"Error: {e}")


def main() -> None:
    """Main application loop."""
    manager = TaskManager()

    while True:
        display_menu()
        choice = input().strip()

        if choice == "1":
            add_task(manager)
        elif choice == "2":
            view_tasks(manager)
        elif choice == "3":
            update_task(manager)
        elif choice == "4":
            delete_task(manager)
        elif choice == "5":
            mark_task_completion(manager)
        elif choice == "6":
            print("\nGoodbye! Note: All tasks are in-memory only and will be lost on exit.")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 6")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
