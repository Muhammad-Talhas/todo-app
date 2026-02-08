# Tasks: AI-powered Todo Chatbot using MCP and OpenAI Agents

**Feature**: 003-ai-todo-chatbot
**Created**: 2026-02-08
**Status**: Draft

## Phase 1: Setup

Initialize project structure and install dependencies needed for the AI-powered Todo Chatbot.

- [ ] T001 Create phase3 directory structure with backend, frontend, and mcp-server subdirectories
- [ ] T002 Install required Python dependencies: openai, mcp-sdk-python, fastapi, sqlmodel, uvicorn
- [ ] T003 Install required JavaScript dependencies for chatbot frontend components
- [ ] T004 Set up configuration files for MCP server and OpenAI integration

## Phase 2: Foundational Components

Create foundational components that all user stories depend on.

- [ ] T005 [P] Create Conversation model in phase3/backend/models/conversation.py
- [ ] T006 [P] Create Message model in phase3/backend/models/message.py
- [ ] T007 [P] Update Task model to support chatbot interactions in phase3/backend/models/task.py
- [ ] T008 Create database migration for new conversation/message tables in phase3/backend/database/migrations/
- [ ] T009 [P] Create JWT authentication utility functions in phase3/backend/utils/auth.py
- [ ] T010 Implement user validation middleware in phase3/backend/middleware/user_validation.py

## Phase 3: User Story 1 - Natural Language Todo Management (Priority: P1)

A user wants to manage their todos using natural language instead of clicking buttons. They can say things like "Add a task to buy groceries" or "Mark the meeting task as complete" and the AI chatbot will interpret their intent and perform the appropriate action.

**Independent Test**: Can be fully tested by sending various natural language commands to the chatbot and verifying that the appropriate todo operations are performed (add, list, update, complete, delete).

- [ ] T011 [P] [US1] Create MCP tool server skeleton in phase3/mcp-server/server.py
- [ ] T012 [P] [US1] Implement add_task MCP tool in phase3/mcp-server/tools/task_operations.py
- [ ] T013 [P] [US1] Implement list_tasks MCP tool in phase3/mcp-server/tools/task_operations.py
- [ ] T014 [P] [US1] Implement complete_task MCP tool in phase3/mcp-server/tools/task_operations.py
- [ ] T015 [P] [US1] Implement delete_task MCP tool in phase3/mcp-server/tools/task_operations.py
- [ ] T016 [P] [US1] Implement update_task MCP tool in phase3/mcp-server/tools/task_operations.py
- [ ] T017 [US1] Create AI Agent controller in phase3/backend/agents/todo_agent.py
- [ ] T018 [US1] Implement conversation manager in phase3/backend/managers/conversation_manager.py
- [ ] T019 [US1] Create chat API endpoint in phase3/backend/api/chat.py
- [ ] T020 [US1] Integrate OpenAI Assistant with MCP tools in phase3/backend/agents/todo_agent.py
- [ ] T021 [US1] Test basic natural language command processing with sample inputs

## Phase 4: User Story 2 - Persistent Conversation Context (Priority: P2)

A user can have ongoing conversations with the chatbot across multiple sessions. The system remembers the conversation history and maintains context between interactions, allowing for more natural and coherent dialogue.

**Independent Test**: Can be tested by creating a conversation, performing some operations, disconnecting, reconnecting, and verifying that the conversation context is maintained appropriately.

- [ ] T022 [P] [US2] Enhance conversation manager to load history from database in phase3/backend/managers/conversation_manager.py
- [ ] T023 [P] [US2] Implement conversation context reconstruction logic in phase3/backend/managers/conversation_manager.py
- [ ] T024 [US2] Modify chat API to persist conversation messages in database in phase3/backend/api/chat.py
- [ ] T025 [US2] Create conversation history retrieval function in phase3/backend/services/conversation_service.py
- [ ] T026 [US2] Test conversation persistence across multiple API calls with same conversation ID

## Phase 5: User Story 3 - Secure Task Isolation (Priority: P3)

Each user can only access and modify their own tasks and conversations. The system enforces proper authentication and authorization to ensure data privacy and security.

**Independent Test**: Can be tested by attempting to access another user's tasks or conversations and verifying that the system properly restricts access.

- [ ] T027 [P] [US3] Implement user ownership validation for tasks in phase3/backend/services/task_service.py
- [ ] T028 [P] [US3] Implement user ownership validation for conversations in phase3/backend/services/conversation_service.py
- [ ] T029 [P] [US3] Add JWT validation to chat API endpoint in phase3/backend/api/chat.py
- [ ] T030 [US3] Verify user_id in JWT matches user_id in API path parameter
- [ ] T031 [US3] Test user isolation by attempting cross-user access to tasks and conversations

## Phase 6: Frontend Integration

Integrate the chatbot interface with the existing frontend from Phase 2.

- [ ] T032 Create chatbot UI components in phase3/frontend/src/components/chatbot/
- [ ] T033 Integrate chat API calls in phase3/frontend/src/services/chatService.ts
- [ ] T034 Add JWT token handling for chat API requests in phase3/frontend/src/lib/api.ts
- [ ] T035 Implement loading and error states for chat interface in phase3/frontend/src/components/chatbot/
- [ ] T036 Test frontend integration with backend chat API

## Phase 7: Polish & Cross-Cutting Concerns

Final touches, error handling, and documentation.

- [ ] T037 Implement comprehensive error handling for AI agent failures
- [ ] T038 Add meaningful error messages for failed operations in phase3/backend/api/chat.py
- [ ] T039 Create health check endpoints for MCP server and backend
- [ ] T040 Add logging for debugging and monitoring in all components
- [ ] T041 Write documentation for installation and usage in phase3/README.md
- [ ] T042 Perform end-to-end testing of all user stories
- [ ] T043 Optimize response times for chat API under 5 seconds

## Dependencies

- **User Story 2** depends on: User Story 1 (needs basic chat functionality)
- **User Story 3** depends on: User Story 1 (needs basic chat functionality)

## Parallel Execution Opportunities

- **T005-T007**: Models can be created in parallel
- **T012-T016**: MCP tools can be implemented in parallel
- **T032-T035**: Frontend components can be developed in parallel after backend APIs are established

## Implementation Strategy

Follow MVP-first approach by implementing User Story 1 first (basic natural language todo management), then iteratively adding persistent conversation context and security features. Each user story should result in a independently testable increment that provides value to users.