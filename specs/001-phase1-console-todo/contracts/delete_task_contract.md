# Delete Task Contract

**Operation**: Delete Task
**Purpose**: Remove a task from in-memory storage by unique ID
**User Story**: User Story 4 - Delete Tasks (Priority: P2)

## Inputs

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|----------|------------|
| task_id | int | Yes | N/A | Positive integer task ID to delete |

## Outputs

**Success Response**:
```json
{
    "success": true,
    "message": "Task {task_id} deleted successfully",
    "task": null
}
```

**Error Response**:
```json
{
    "success": false,
    "message": "Error: Task with ID {task_id} not found",
    "task": null
}
```

## Behavior

1. **Validation**:
   - Validate `task_id` is positive integer (> 0)
   - Validate `task_id` exists in task collection

2. **Deletion**:
   - Find task by `task_id`
   - Remove task from in-memory task collection
   - Task ID is not reused after deletion

3. **Response**:
   - On success: Return confirmation message
   - On error: Return error message indicating task not found

## Validation Rules

- **task_id**:
  - MUST be positive integer (> 0)
  - MUST exist in task collection
  - Type: int
  - Example valid: 1, 2, 99
  - Example invalid: 0, -1, "abc" (non-integer)
  - Example invalid: 999 (if task doesn't exist)

## Acceptance Scenarios

From spec.md User Story 4:

1. **Given** a task with ID "1" exists, **When** user enters "Delete Task" with ID "1", **Then** system removes task from memory and confirms deletion
2. **Given** task ID "99" does not exist, **When** user tries to delete task with ID "99", **Then** system displays an error message indicating task was not found
3. **Given** a task with ID "1" has been deleted, **When** user views all tasks, **Then** task ID "1" no longer appears in list
4. **Given** multiple tasks exist, **When** user deletes a task with ID "2", **Then** other tasks remain unchanged and their IDs are not modified

## Implementation Notes

- Calls `TaskManager.delete_task(task_id)`
- TaskManager validates task ID exists before deleting
- TaskManager removes task from internal list
- Console interface prompts user for task ID
- Success message: "Task {id} deleted successfully"
- Error message: "Error: Task with ID {id} not found"
- Deletion is permanent within session (cannot undo)

## Related Functional Requirements

- **FR-016**: System MUST allow users to delete tasks by providing task ID
- **FR-017**: System MUST validate that a task ID exists before attempting deletion
- **FR-018**: System MUST remove task entirely from memory upon successful deletion
- **FR-022**: System MUST display a confirmation message for all successful operations
- **FR-023**: System MUST display an informative error message for invalid task IDs
- **FR-030**: System MUST ensure that updating or deleting one task does not affect other tasks
