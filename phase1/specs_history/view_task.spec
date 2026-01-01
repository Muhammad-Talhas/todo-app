# View Task Specification

This specification defines the requirements for viewing tasks in the todo application.

## Inputs
- Filter (optional): None for all tasks, True for completed, False for pending

## Behavior
- Display all tasks with ID, title, description, and completion status
- Option to filter by completion status (all/completed/pending)
- Format output for readability

## Validation
- Handle empty task list case
- Format long titles/descriptions appropriately
