"""Console interface and entry point for Phase I Todo Application"""

import sys
from datetime import datetime
from task_manager import TaskManager
from utils import validate_title, validate_task_id, format_task_list
from task import Priority


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
    print("6. Search Tasks")
    print("7. Sort Tasks")
    print("8. Filter by Priority")
    print("9. Filter by Tag")
    print("10. View Overdue Tasks")
    print("11. Task Statistics")
    print("12. Exit")
    print("\nEnter your choice (1-12):")


def display_view_menu() -> None:
    """Display view options submenu."""
    print("\nView options:")
    print("1. All Tasks")
    print("2. Completed Tasks")
    print("3. Pending Tasks")
    print("4. Overdue Tasks")
    print("\nEnter your choice (1-4):")


def display_sort_menu() -> None:
    """Display sort options submenu."""
    print("\nSort options:")
    print("1. By Priority (High to Low)")
    print("2. By Due Date (Earliest First)")
    print("3. Alphabetically (A-Z)")
    print("\nEnter your choice (1-3):")


def display_priority_menu() -> None:
    """Display priority filter options."""
    print("\nPriority options:")
    print("1. High Priority")
    print("2. Medium Priority")
    print("3. Low Priority")
    print("\nEnter your choice (1-3):")


def add_task(manager: TaskManager) -> None:
    """Handle adding a new task."""
    print("\n--- Add Task ---")
    title = input("Enter task title: ").strip()

    if not validate_title(title):
        print("Error: Task title cannot be empty")
        return

    description = input("Enter task description (optional, press Enter to skip): ").strip()

    # Get priority
    print("\nPriority options:")
    print("1. High (🔴)")
    print("2. Medium (🟡)")
    print("3. Low (🟢)")
    priority_choice = input("Enter priority (1-3, default 2): ").strip()

    priority_map = {"1": Priority.HIGH, "2": Priority.MEDIUM, "3": Priority.LOW}
    priority = priority_map.get(priority_choice, Priority.MEDIUM)

    # Get tags
    tags_input = input("Enter tags (comma-separated, optional): ").strip()
    tags = [tag.strip() for tag in tags_input.split(",")] if tags_input else []

    # Get due date
    due_date_input = input("Enter due date (DD-MM-YYYY HH:MM, optional): ").strip()
    due_date = None
    if due_date_input:
        try:
            due_date = datetime.strptime(due_date_input, "%d-%m-%Y %H:%M")
        except ValueError:
            print("Warning: Invalid date format. No due date will be set.")
            due_date = None

    try:
        task = manager.add_task(title, description, priority, tags, due_date)
        print(f"Task created successfully with ID {task.id}")
        print(f"  {task}")
    except ValueError as e:
        print(f"Error: {e}")


def view_tasks(manager: TaskManager) -> None:
    """Handle viewing tasks with filtering."""
    display_view_menu()
    choice = input("\nEnter your choice (1-4): ").strip()

    if choice not in ["1", "2", "3", "4"]:
        print("Error: Invalid choice. Please enter 1, 2, 3, or 4")
        return

    if choice == "1":
        display_all_tasks(manager)
    elif choice == "2":
        display_filtered_tasks(manager, completed=True)
    elif choice == "3":
        display_filtered_tasks(manager, completed=False)
    elif choice == "4":
        display_overdue_tasks(manager)


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


def display_overdue_tasks(manager: TaskManager) -> None:
    """Display overdue tasks."""
    print(f"\n--- Overdue Tasks ---")

    tasks = manager.view_overdue_tasks()

    if not tasks:
        print("No overdue tasks found")
    else:
        print(format_task_list(tasks))
        print(f"\nTotal: {len(tasks)} overdue task(s)")


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

    # Get what fields to update
    print("\nWhat would you like to update?")
    print("1. Title only")
    print("2. Description only")
    print("3. Priority only")
    print("4. Tags only")
    print("5. Due date only")
    print("6. Multiple fields")

    update_choice = input("Enter your choice (1-6): ").strip()

    if update_choice == "1":
        new_title = input("Enter new title: ").strip()
        if not new_title:
            print("Error: Title cannot be empty")
            return
        try:
            task = manager.update_task(task_id, title=new_title)
            print(f"Task {task_id} title updated successfully")
            print(f"  {task}")
        except ValueError as e:
            print(f"Error: {e}")

    elif update_choice == "2":
        new_description = input("Enter new description: ").strip()
        try:
            task = manager.update_task(task_id, description=new_description)
            print(f"Task {task_id} description updated successfully")
            print(f"  {task}")
        except ValueError as e:
            print(f"Error: {e}")

    elif update_choice == "3":
        print("\nPriority options:")
        print("1. High (🔴)")
        print("2. Medium (🟡)")
        print("3. Low (🟢)")
        priority_choice = input("Enter new priority (1-3): ").strip()

        priority_map = {"1": Priority.HIGH, "2": Priority.MEDIUM, "3": Priority.LOW}
        if priority_choice in priority_map:
            new_priority = priority_map[priority_choice]
            try:
                task = manager.update_task(task_id, priority=new_priority)
                print(f"Task {task_id} priority updated successfully")
                print(f"  {task}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Error: Invalid priority choice")

    elif update_choice == "4":
        tags_input = input("Enter new tags (comma-separated): ").strip()
        new_tags = [tag.strip() for tag in tags_input.split(",")] if tags_input else []
        try:
            task = manager.update_task(task_id, tags=new_tags)
            print(f"Task {task_id} tags updated successfully")
            print(f"  {task}")
        except ValueError as e:
            print(f"Error: {e}")

    elif update_choice == "5":
        due_date_input = input("Enter new due date (DD-MM-YYYY HH:MM): ").strip()
        new_due_date = None
        if due_date_input:
            try:
                new_due_date = datetime.strptime(due_date_input, "%d-%m-%Y %H:%M")
            except ValueError:
                print("Error: Invalid date format. Please use DD-MM-YYYY HH:MM format.")
                return
        try:
            task = manager.update_task(task_id, due_date=new_due_date)
            print(f"Task {task_id} due date updated successfully")
            print(f"  {task}")
        except ValueError as e:
            print(f"Error: {e}")

    elif update_choice == "6":
        new_title = input("Enter new title (press Enter to skip): ").strip() or None
        if new_title == "":
            new_title = None

        new_description = input("Enter new description (press Enter to skip): ").strip() or None
        if new_description == "":
            new_description = None

        print("\nPriority options (press Enter to skip):")
        print("1. High (🔴)")
        print("2. Medium (🟡)")
        print("3. Low (🟢)")
        priority_choice = input("Enter new priority (1-3, or Enter to skip): ").strip()

        new_priority = None
        if priority_choice:
            priority_map = {"1": Priority.HIGH, "2": Priority.MEDIUM, "3": Priority.LOW}
            if priority_choice in priority_map:
                new_priority = priority_map[priority_choice]
            else:
                print("Error: Invalid priority choice")
                return

        tags_input = input("Enter new tags (comma-separated, or Enter to skip): ").strip()
        new_tags = None
        if tags_input:
            new_tags = [tag.strip() for tag in tags_input.split(",")]

        due_date_input = input("Enter new due date (DD-MM-YYYY HH:MM, or Enter to skip): ").strip()
        new_due_date = None
        if due_date_input:
            try:
                new_due_date = datetime.strptime(due_date_input, "%d-%m-%Y %H:%M")
            except ValueError:
                print("Error: Invalid date format. Please use DD-MM-YYYY HH:MM format.")
                return

        try:
            task = manager.update_task(task_id, new_title, new_description, new_priority, new_tags, new_due_date)
            print(f"Task {task_id} updated successfully")
            print(f"  {task}")
        except ValueError as e:
            print(f"Error: {e}")

    else:
        print("Error: Invalid choice")


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
        print(f"  {task}")
    except ValueError as e:
        print(f"Error: {e}")


def search_tasks(manager: TaskManager) -> None:
    """Handle searching tasks."""
    print("\n--- Search Tasks ---")
    keyword = input("Enter keyword to search: ").strip()

    if not keyword:
        print("Error: Keyword cannot be empty")
        return

    tasks = manager.search_tasks(keyword)

    if not tasks:
        print("No tasks found matching the keyword")
    else:
        print(f"\n--- Search Results for '{keyword}' ---")
        print(format_task_list(tasks))
        print(f"\nTotal: {len(tasks)} task(s) found")


def sort_tasks(manager: TaskManager) -> None:
    """Handle sorting tasks."""
    print("\n--- Sort Tasks ---")
    display_sort_menu()
    choice = input("\nEnter your choice (1-3): ").strip()

    if choice == "1":
        tasks = manager.sort_tasks_by_priority()
        print("\n--- Tasks Sorted by Priority (High to Low) ---")
    elif choice == "2":
        tasks = manager.sort_tasks_by_due_date()
        print("\n--- Tasks Sorted by Due Date (Earliest First) ---")
    elif choice == "3":
        tasks = manager.sort_tasks_alphabetically()
        print("\n--- Tasks Sorted Alphabetically (A-Z) ---")
    else:
        print("Error: Invalid choice. Please enter 1, 2, or 3")
        return

    if not tasks:
        print("No tasks found")
    else:
        print(format_task_list(tasks))
        print(f"\nTotal: {len(tasks)} task(s)")


def filter_by_priority(manager: TaskManager) -> None:
    """Handle filtering tasks by priority."""
    print("\n--- Filter by Priority ---")
    display_priority_menu()
    choice = input("\nEnter your choice (1-3): ").strip()

    if choice == "1":
        priority = Priority.HIGH
        priority_text = "High"
    elif choice == "2":
        priority = Priority.MEDIUM
        priority_text = "Medium"
    elif choice == "3":
        priority = Priority.LOW
        priority_text = "Low"
    else:
        print("Error: Invalid choice. Please enter 1, 2, or 3")
        return

    tasks = manager.view_tasks_by_priority(priority)

    print(f"\n--- {priority_text} Priority Tasks ---")
    if not tasks:
        print(f"No {priority_text.lower()} priority tasks found")
    else:
        print(format_task_list(tasks))
        print(f"\nTotal: {len(tasks)} {priority_text.lower()} priority task(s)")


def filter_by_tag(manager: TaskManager) -> None:
    """Handle filtering tasks by tag."""
    print("\n--- Filter by Tag ---")
    tag = input("Enter tag to filter by: ").strip()

    if not tag:
        print("Error: Tag cannot be empty")
        return

    tasks = manager.view_tasks_by_tag(tag)

    print(f"\n--- Tasks with Tag '{tag}' ---")
    if not tasks:
        print(f"No tasks found with tag '{tag}'")
    else:
        print(format_task_list(tasks))
        print(f"\nTotal: {len(tasks)} task(s) with tag '{tag}'")


def view_overdue_tasks(manager: TaskManager) -> None:
    """Handle viewing overdue tasks."""
    print("\n--- Overdue Tasks ---")
    tasks = manager.view_overdue_tasks()

    if not tasks:
        print("No overdue tasks found")
    else:
        print(format_task_list(tasks))
        print(f"\nTotal: {len(tasks)} overdue task(s)")


def view_task_statistics(manager: TaskManager) -> None:
    """Handle viewing task statistics."""
    print("\n--- Task Statistics ---")
    stats = manager.get_task_statistics()

    print(f"Total tasks: {stats['total']}")
    print(f"Completed tasks: {stats['completed']}")
    print(f"Pending tasks: {stats['pending']}")
    print(f"Overdue tasks: {stats['overdue']}")

    if stats['total'] > 0:
        completion_rate = (stats['completed'] / stats['total']) * 100
        print(f"Completion rate: {completion_rate:.1f}%")


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
            search_tasks(manager)
        elif choice == "7":
            sort_tasks(manager)
        elif choice == "8":
            filter_by_priority(manager)
        elif choice == "9":
            filter_by_tag(manager)
        elif choice == "10":
            view_overdue_tasks(manager)
        elif choice == "11":
            view_task_statistics(manager)
        elif choice == "12":
            print("\nGoodbye! Note: All tasks are in-memory only and will be lost on exit.")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 12")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()