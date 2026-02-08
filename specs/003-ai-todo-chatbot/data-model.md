# Data Model: AI-powered Todo Chatbot

**Feature**: 003-ai-todo-chatbot
**Created**: 2026-02-08
**Status**: Draft

## Entity Models

### Task Model (Extended from Phase 2)
- **Entity Name**: Task
- **Fields**:
  - `user_id`: Integer (foreign key to user)
  - `id`: Integer (primary key, auto-increment)
  - `title`: String (required, max 255 chars)
  - `description`: Text (optional)
  - `completed`: Boolean (default: False)
  - `created_at`: DateTime (auto-generated)
  - `updated_at`: DateTime (auto-generated)
- **Relationships**: Belongs to a User, referenced in Message entities
- **Validation Rules**: Title is required, user_id must match authenticated user

### Conversation Model
- **Entity Name**: Conversation
- **Fields**:
  - `user_id`: Integer (foreign key to user)
  - `id`: Integer (primary key, auto-increment)
  - `created_at`: DateTime (auto-generated)
  - `updated_at`: DateTime (auto-generated)
- **Relationships**: Belongs to a User, contains multiple Messages
- **Validation Rules**: user_id must match authenticated user, proper indexing for performance

### Message Model
- **Entity Name**: Message
- **Fields**:
  - `user_id`: Integer (foreign key to user)
  - `id`: Integer (primary key, auto-increment)
  - `conversation_id`: Integer (foreign key to conversation)
  - `role`: String (enum: 'user' or 'assistant')
  - `content`: Text (required)
  - `created_at`: DateTime (auto-generated)
- **Relationships**: Belongs to a Conversation, associated with a User
- **Validation Rules**: Role must be 'user' or 'assistant', content is required

## Entity Relationships

```
User (1) <---> (Many) Conversation
Conversation (1) <---> (Many) Message
User (1) <---> (Many) Task
User (1) <---> (Many) Message
```

## State Transitions

### Task States
- **Created**: Task is added to user's todo list (completed=False)
- **Updated**: Task details (title, description) are modified
- **Completed**: Task status changes from False to True
- **Deleted**: Task is removed from user's list

### Message States
- **Created**: Message is added to conversation with role assignment
- **Referenced**: Message becomes part of ongoing conversation context

## Database Schema Considerations

### Indexing Strategy
- Conversation table: Index on user_id for efficient user isolation
- Message table: Composite index on (conversation_id, created_at) for chronological retrieval
- Task table: Index on user_id for efficient user-specific queries

### Constraints
- Foreign key constraints to enforce referential integrity
- User ownership validation on all operations
- Non-null constraints on required fields