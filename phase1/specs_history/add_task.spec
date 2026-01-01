# Add Task Specification

This specification defines the requirements for adding tasks to the todo application.

## Inputs
- Title (string): Required task title
- Description (string): Optional task description

## Behavior
- Generate unique task ID automatically
- Set completion status to False by default
- Add task to in-memory storage
- Return confirmation with task ID

## Validation
- Title must not be empty
- Description can be empty
- Task ID must be unique within session
