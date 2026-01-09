# Data Model: Secure Multi-User Todo Web Application

## User Entity
- **id**: Integer (Primary Key, Auto-increment)
- **email**: String (Unique, Required, Validated)
- **name**: String (Optional)
- **password_hash**: String (Required, Encrypted)
- **created_at**: DateTime (Auto-generated)
- **updated_at**: DateTime (Auto-generated)
- **is_active**: Boolean (Default: True)

## Task Entity
- **id**: Integer (Primary Key, Auto-increment)
- **title**: String (Required, Max 200 characters)
- **description**: Text (Optional)
- **completed**: Boolean (Default: False)
- **user_id**: Integer (Foreign Key to User.id, Required)
- **created_at**: DateTime (Auto-generated)
- **updated_at**: DateTime (Auto-generated)
- **due_date**: DateTime (Optional)

## Relationships
- User (1) to Task (Many): One user can have many tasks
- Task (Many) to User (1): Each task belongs to one user

## Validation Rules
- User email must be unique and properly formatted
- Task title must not be empty
- Task user_id must reference an existing user
- Task completion status can be updated independently
- User cannot access tasks belonging to other users

## State Transitions
- Task: Incomplete → Complete (via PATCH /api/{user_id}/tasks/{id}/complete)
- User: Active → Inactive (administrative action, not implemented in this phase)