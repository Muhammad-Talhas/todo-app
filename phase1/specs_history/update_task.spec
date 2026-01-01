# Update Task Specification

This specification defines the requirements for updating tasks in the todo application.

## Inputs
- Task ID (positive integer): Required to identify task to update
- New title (string, optional): New task title
- New description (string, optional): New task description

## Behavior
- Validate task ID exists before update
- Update only provided fields (title and/or description)
- Return confirmation of successful update
- Require at least one field to be provided

## Validation
- Task ID must exist in task collection
- At least one field (title or description) must be provided
- Title, if provided, must not be empty
