# Update Task Contract

**Operation**: Update Task
**Purpose**: Modify title and/or description of an existing task
**User Story**: User Story 3 - Update Task Information (Priority: P2)

## Inputs

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|----------|------------|
| task_id | int | Yes | N/A | Positive integer task ID to update |
| title | Optional[str] | No | None | Optional new title string |
| description | Optional[str] | No | None | Optional new description string |

## Outputs

**Success Response**:
```json
{
    "success": true,
    "message": "Task {task_id} updated successfully",
    "task": {
        "id": 1,
        "title": "Buy vegetables",
        "description": "Carrots, spinach, tomatoes",
        "completed": false
    }
}
```

**Error Response (Task Not Found)**:
```json
{
    "success": false,
    "message": "Error: Task with ID {task_id} not found",
    "task": null
}
```

**Error Response (No Fields Provided)**:
```json
{
    "success": false,
    "message": "Error: At least one field (title or description) must be provided",
    "task": null
}
```

## Behavior

1. **Validation**:
   - Validate `task_id` is positive integer (> 0)
   - Validate `task_id` exists in task collection
   - Validate at least one of `title` or `description` is provided (not both None)

2. **Update**:
   - Find task by `task_id`
   - Update `title` field if provided (non-empty string)
   - Update `description` field if provided (can be empty string)
   - Keep other fields unchanged

3. **Response**:
   - On success: Return confirmation message with updated task details
   - On error: Return error message explaining validation failure

## Validation Rules

- **task_id**:
  - MUST be positive integer (> 0)
  - MUST exist in task collection
  - Type: int
  - Example valid: 1
  - Example invalid: 0, -1, 999 (if task doesn't exist)

- **title**:
  - Optional parameter
  - If provided, must be non-empty string (after stripping whitespace)
  - Type: str (if provided)
  - Example valid: "Buy vegetables"
  - Example valid: null / None (not provided)
  - Example invalid: "" (empty string if provided)

- **description**:
  - Optional parameter
  - If provided, can be empty string or non-empty string
  - Type: str (if provided)
  - Example valid: "Carrots, spinach, tomatoes"
  - Example valid: "" (empty string if provided)
  - Example valid: null / None (not provided)

## Acceptance Scenarios

From spec.md User Story 3:

1. **Given** a task with ID "1" exists, **When** user enters "Update Task" with ID "1" and new title "Buy vegetables", **Then** system updates task's title and confirms change
2. **Given** a task with ID "1" exists, **When** user enters "Update Task" with ID "1" and new description "Carrots, spinach, tomatoes", **Then** system updates task's description and confirms change
3. **Given** a task with ID "1" exists, **When** user enters "Update Task" with ID "1" and both new title and description, **Then** system updates both fields and confirms change
4. **Given** a task with ID "1" exists, **When** user enters "Update Task" with ID "1" but no new values, **Then** system displays an error message explaining at least one field must be provided
5. **Given** task ID "99" does not exist, **When** user tries to update task with ID "99", **Then** system displays an error message indicating task was not found

## Implementation Notes

- Calls `TaskManager.update_task(task_id, title, description)`
- TaskManager validates task ID exists before updating
- TaskManager validates at least one field provided
- Console interface prompts user for task ID, then optional new title, then optional new description
- Success message: "Task {id} updated successfully"
- Error message (task not found): "Error: Task with ID {id} not found"
- Error message (no fields): "Error: At least one field (title or description) must be provided"

## Related Functional Requirements

- **FR-011**: System MUST allow users to update task titles by providing task ID
- **FR-012**: System MUST allow users to update task descriptions by providing task ID
- **FR-013**: System MUST allow users to update both title and description simultaneously
- **FR-014**: System MUST validate that a task ID exists before attempting updates
- **FR-015**: System MUST require at least one field to be provided when updating a task
- **FR-022**: System MUST display a confirmation message for all successful operations
- **FR-023**: System MUST display an informative error message for invalid task IDs
