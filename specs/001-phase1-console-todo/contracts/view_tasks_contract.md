# View Tasks Contract

**Operation**: View Tasks
**Purpose**: Display tasks in human-readable format with optional filtering by completion status
**User Story**: User Story 2 - View Task List (Priority: P1)

## Inputs

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|----------|------------|
| filter | Optional[bool] | No | None | Optional filter: True for completed, False for pending, None for all |

## Outputs

**Success Response (All Tasks)**:
```json
{
    "success": true,
    "message": "Found {count} task(s)",
    "tasks": [
        {
            "id": 1,
            "title": "Buy groceries",
            "description": "Milk, eggs, bread",
            "completed": false
        },
        {
            "id": 2,
            "title": "Learn Python",
            "description": "",
            "completed": true
        }
    ]
}
```

**Success Response (Filtered by Status)**:
```json
{
    "success": true,
    "message": "Found {count} completed task(s)",
    "tasks": [
        {
            "id": 2,
            "title": "Learn Python",
            "description": "",
            "completed": true
        }
    ]
}
```

**Success Response (Empty List)**:
```json
{
    "success": true,
    "message": "No tasks found",
    "tasks": []
}
```

## Behavior

1. **Validation**:
   - `filter` parameter is optional
   - If provided, must be boolean value (True or False)

2. **Retrieval**:
   - If `filter` is None: Return all tasks in insertion order
   - If `filter` is True: Return only completed tasks (completed == True)
   - If `filter` is False: Return only pending tasks (completed == False)

3. **Formatting**:
   - Display tasks in human-readable format
   - Show ID, title, description, and completion status
   - Format for 80-character terminal width
   - Use consistent visual indicators (e.g., ✓ for complete, ○ for pending)

4. **Response**:
   - Always return success response (viewing cannot fail)
   - Message indicates count of tasks found
   - Empty task list is valid state

## Validation Rules

- **Filter**:
  - Optional parameter
  - If provided, type must be bool
  - Example valid: null / None (show all tasks)
  - Example valid: true (show only completed)
  - Example valid: false (show only pending)

## Acceptance Scenarios

From spec.md User Story 2:

1. **Given** multiple tasks exist in memory, **When** user enters "View Tasks" command, **Then** system displays all tasks with ID, title, description, and completion status in a readable format
2. **Given** multiple tasks exist with mixed completion states, **When** user filters to show "completed" tasks, **Then** only tasks marked as complete are displayed
3. **Given** multiple tasks exist with mixed completion states, **When** user filters to show "pending" tasks, **Then** only tasks marked as incomplete are displayed
4. **Given** no tasks exist in memory, **When** user enters "View Tasks" command, **Then** system displays a friendly message indicating no tasks are available
5. **Given** tasks have very long titles or descriptions, **When** user views tasks, **Then** display formats text to remain readable without truncating essential information

## Implementation Notes

- Calls `TaskManager.view_all_tasks()` or `TaskManager.view_tasks_by_status(completed)`
- Console interface provides menu options: (1) All Tasks, (2) Completed, (3) Pending
- Format each task as: `[{id}] {status} {title} - {description or '(no description)'}`
- Status indicator: "✓" for complete, "○" for pending
- Success message: "Found {count} task(s)" or "No tasks found"
- No error response possible (view operation cannot fail)

## Related Functional Requirements

- **FR-006**: System MUST allow users to view all tasks in a human-readable format
- **FR-007**: System MUST display task ID, title, description, and completion status for each task
- **FR-008**: System MUST provide an option to filter tasks to show only completed tasks
- **FR-009**: System MUST provide an option to filter tasks to show only incomplete tasks
- **FR-010**: System MUST display a friendly message when no tasks are available to view
- **FR-028**: System MUST display tasks in a consistent format that is easy to read
