# Delete Task Specification

This specification defines the requirements for deleting tasks in the todo application.

## Inputs
- Task ID (positive integer): Required to identify task to delete

## Behavior
- Validate task ID exists before deletion
- Remove task from in-memory storage
- Return confirmation of successful deletion

## Validation
- Task ID must exist in task collection
- Task ID must be a positive integer
