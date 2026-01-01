# Complete Task Specification

This specification defines the requirements for marking tasks as complete/incomplete in the todo application.

## Inputs
- Task ID (positive integer): Required to identify task to update
- Status (boolean): True for complete, False for incomplete

## Behavior
- Validate task ID exists before update
- Update completion status to specified value
- Return confirmation of successful update

## Validation
- Task ID must exist in task collection
- Task ID must be a positive integer
- Status must be boolean value
