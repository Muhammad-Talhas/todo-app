# Mark Complete/Incomplete Contract

**Operation**: Mark Task Complete/Incomplete
**Purpose**: Toggle or set task completion status
**User Story**: User Story 5 - Mark Task Completion Status (Priority: P1)

## Inputs

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|----------|------------|
| task_id | int | Yes | N/A | Positive integer task ID |
| completed | bool | Yes | N/A | True for complete, False for incomplete |

## Outputs

**Success Response (Mark Complete)**:
```json
{
    "success": true,
    "message": "Task {task_id} marked as complete",
    "task": {
        "id": 1,
        "title": "Learn Python",
        "description": "",
        "completed": true
    }
}
```

**Success Response (Mark Incomplete)**:
```json
{
    "success": true,
    "message": "Task {task_id} marked as incomplete",
    "task": {
        "id": 1,
        "title": "Learn Python",
        "description": "",
        "completed": false
    }
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
   - Validate `completed` is boolean value (True or False)

2. **Status Update**:
   - Find task by `task_id`
   - Update `completed` field to provided value
   - Task status toggles between True and False based on input

3. **Response**:
   - On success: Return confirmation message with updated task status
   - On error: Return error message indicating task not found

## Validation Rules

- **task_id**:
  - MUST be positive integer (> 0)
  - MUST exist in task collection
  - Type: int
  - Example valid: 1, 2, 99
  - Example invalid: 0, -1, "abc" (non-integer)
  - Example invalid: 999 (if task doesn't exist)

- **completed**:
  - MUST be boolean value
  - Type: bool
  - Example valid: true
  - Example valid: false
  - Example invalid: "yes", 1, 0 (non-boolean)

## Acceptance Scenarios

From spec.md User Story 5:

1. **Given** a task with ID "1" is incomplete, **When** user marks it as complete, **Then** task's completion status updates to True and system confirms
2. **Given** a task with ID "1" is complete, **When** user marks it as incomplete, **Then** task's completion status updates to False and system confirms
3. **Given** task ID "99" does not exist, **When** user tries to mark task with ID "99" as complete, **Then** system displays an error message indicating task was not found
4. **Given** a task is marked as complete, **When** user views all tasks, **Then** task is displayed with completion status indicating it is finished
5. **Given** a task is marked as incomplete, **When** user filters to view only completed tasks, **Then** task does not appear in filtered list

## Implementation Notes

- Calls `TaskManager.mark_task_completion(task_id, completed)`
- TaskManager validates task ID exists before updating
- Console interface prompts user for task ID and new status (complete/incomplete)
- Success message: "Task {id} marked as complete" or "Task {id} marked as incomplete"
- Error message: "Error: Task with ID {id} not found"
- Status can be toggled multiple times (complete ↔ incomplete)

## Related Functional Requirements

- **FR-019**: System MUST allow users to mark tasks as complete by providing task ID
- **FR-020**: System MUST allow users to mark tasks as incomplete by providing task ID
- **FR-021**: System MUST validate that a task ID exists before attempting status changes
- **FR-022**: System MUST display a confirmation message for all successful operations
- **FR-023**: System MUST display an informative error message for invalid task IDs
