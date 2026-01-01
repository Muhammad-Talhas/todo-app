# Add Task Contract

**Operation**: Add Task
**Purpose**: Create a new todo item with auto-generated unique ID
**User Story**: User Story 1 - Create Tasks (Priority: P1)

## Inputs

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|----------|------------|
| title | str | Yes | N/A | Non-empty task title |
| description | str | No | "" | Optional task description |

## Outputs

**Success Response**:
```
{
    "success": true,
    "message": "Task created successfully with ID {task_id}",
    "task": {
        "id": 1,
        "title": "Buy groceries",
        "description": "Milk, eggs, bread",
        "completed": false
    }
}
```

**Error Response**:
```
{
    "success": false,
    "message": "Error: {error_message}",
    "task": null
}
```

## Behavior

1. **Validation**:
   - Validate `title` is non-empty string (after stripping whitespace)
   - `description` is optional, can be empty string

2. **ID Generation**:
   - Generate unique sequential integer ID starting from 1
   - Increment counter after each task creation
   - IDs are never reused after deletion

3. **Task Creation**:
   - Create Task object with provided title and description
   - Set `completed` field to `false` by default
   - Add task to in-memory task collection

4. **Response**:
   - On success: Return confirmation message with task details including generated ID
   - On error: Return error message explaining validation failure

## Validation Rules

- **Title**:
  - MUST be non-empty string after whitespace removal
  - Type: str
  - Example valid: "Buy groceries"
  - Example valid: "  Learn Python  "
  - Example invalid: "" (empty string)
  - Example invalid: "   " (whitespace only)

- **Description**:
  - Optional, can be empty string
  - Type: str
  - Example valid: "Milk, eggs, bread"
  - Example valid: "" (empty string)
  - Example valid: null / None (omitted)

## Acceptance Scenarios

From spec.md User Story 1:

1. **Given** application is running, **When** user enters "Add Task" command with title "Buy groceries" and description "Milk, eggs, bread", **Then** system confirms task creation and displays unique task ID
2. **Given** application is running, **When** user enters "Add Task" with title only, **Then** system creates a task with an empty description and confirms creation
3. **Given** application is running, **When** user tries to add a task with empty title, **Then** system displays an error message explaining title is required
4. **Given** application is running, **When** user adds multiple tasks sequentially, **Then** each task receives a different unique identifier

## Implementation Notes

- Calls `TaskManager.add_task(title, description)`
- TaskManager handles ID generation and task storage
- Validation error raised by Task.__post_init__() if title is empty
- Console interface prompts user for title and optional description
- Success message: "Task created successfully with ID {id}"
- Error message: "Error: Task title cannot be empty"

## Related Functional Requirements

- **FR-001**: System MUST allow users to create tasks by providing a title and description
- **FR-002**: System MUST generate a unique identifier for each task automatically
- **FR-003**: System MUST default new tasks to incomplete status
- **FR-004**: System MUST display a confirmation message after successful task creation
- **FR-005**: System MUST validate that task titles are not empty before creating tasks
