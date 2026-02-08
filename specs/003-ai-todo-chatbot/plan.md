# Implementation Plan: AI-powered Todo Chatbot using MCP and OpenAI Agents

**Feature**: 003-ai-todo-chatbot
**Created**: 2026-02-08
**Status**: Draft
**Author**: Claude Sonnet 4.5

## Technical Context

This implementation plan outlines the development of an AI-powered Todo Chatbot that extends the Phase 2 Todo web application. The system will use OpenAI Agents SDK for reasoning, MCP (Model Context Protocol) for tool-based task operations, and a stateless FastAPI backend with persistent conversation memory.

### Architecture Overview

- **Frontend**: Reusing Phase 2 Next.js components with added chatbot UI
- **Backend**: FastAPI endpoints extending Phase 2 backend with chat functionality
- **AI Layer**: OpenAI Agents SDK interpreting user intent and calling MCP tools
- **MCP Server**: Exposing todo operations as standardized tools
- **Database**: Neon PostgreSQL with extended schema for conversations/messages
- **Authentication**: JWT-based using existing Better Auth integration

### Technology Stack

- **Frontend**: Next.js (reused from Phase 2) with OpenAI ChatKit
- **Backend**: Python FastAPI (reused from Phase 2) with additional chat endpoints
- **AI Framework**: OpenAI Agents SDK
- **MCP**: Official Model Context Protocol SDK
- **Database**: SQLModel ORM with Neon PostgreSQL
- **Authentication**: Better Auth (JWT-based, from Phase 2)

### Unknowns & Dependencies

- MCP server implementation details need research
- Integration patterns between OpenAI Agents and FastAPI
- Conversation persistence strategy with proper context reconstruction

## Constitution Check

### Phase III Compliance (Section 61)
- Interface: Web or console natural language interaction ✓
- Tech: OpenAI ChatKit, Agents SDK, Official MCP SDK, existing Phase II backend ✓
- Structure: `/agents` directory for chatbot logic ✓
- Success: All CRUD via chatbot, accurate intent interpretation, seamless backend integration ✓

### Core Principles Alignment
- Spec-Driven Development: Following approved spec.md from feature requirements ✓
- User Experience Excellence: Natural language interface for todo management ✓
- Correctness and Quality: Reusing proven Phase 2 backend operations ✓
- Maintainable Architecture: Clear separation of frontend, backend, and AI layers ✓
- Technology Constraint Discipline: Using prescribed OpenAI ChatKit, Agents SDK, MCP SDK ✓
- Security and Reliability: Maintaining JWT-based authentication from Phase 2 ✓

### Gate Evaluations
- [X] Technology constraints satisfied (OpenAI ChatKit, Agents SDK, MCP SDK)
- [X] Reuse of Phase 2 components planned
- [X] Architecture aligns with Phase III standards
- [X] Security requirements incorporated

## Phase 0: Research & Resolution

### Research Tasks Completed

#### 1. MCP Server Implementation
- **Decision**: Implement MCP server as separate service using official SDK
- **Rationale**: MCP provides standardized protocol for exposing tools to AI agents
- **Alternatives considered**: Direct function calling, REST API integration (rejected - less standardized)

#### 2. OpenAI Agent Integration Patterns
- **Decision**: Use OpenAI Assistant API with custom tools registered via MCP
- **Rationale**: Provides robust conversation memory and intent interpretation
- **Alternatives considered**: LangChain agents, custom prompt engineering (rejected - MCP is more standardized)

#### 3. Conversation Persistence Strategy
- **Decision**: Store conversation context in database, reconstruct on each request
- **Rationale**: Stateless backend requirement from spec, ensures scalability
- **Alternatives considered**: In-memory sessions (rejected - violates stateless requirement)

## Phase 1: Data Models & Contracts

### Data Model Extensions

#### Task Model (Extended from Phase 2)
- Properties: user_id, id, title, description, completed, created_at, updated_at
- Relationships: Belongs to a user, referenced in conversation messages
- Validation: Required fields (title), proper user ownership checks

#### Conversation Model (New)
- Properties: user_id, id, created_at, updated_at
- Relationships: Belongs to a user, contains multiple messages
- Validation: User ownership verification, proper indexing for performance

#### Message Model (New)
- Properties: user_id, id, conversation_id, role, content, created_at
- Relationships: Belongs to a conversation, associated with a user
- Validation: Role must be 'user' or 'assistant', proper content length limits

#### MCP Tool Interface (New)
- Functions: add_task, list_tasks, complete_task, delete_task, update_task
- Parameters: All functions accept user_id for security isolation
- Validation: All operations verify user ownership before execution

### API Contracts

#### Chat Endpoint Contract
- **Endpoint**: POST `/api/{user_id}/chat`
- **Request Body**:
  ```json
  {
    "conversation_id": "integer (optional)",
    "message": "string (required)"
  }
  ```
- **Response Body**:
  ```json
  {
    "conversation_id": "integer",
    "response": "string",
    "tool_calls": "array"
  }
  ```
- **Authentication**: JWT required, user_id in path must match JWT claims
- **Authorization**: User can only access their own conversations and tasks

#### MCP Tool Contracts
- **add_task(user_id, title, description?)**: Creates new task for user
- **list_tasks(user_id, status?)**: Returns user's tasks with optional status filter
- **complete_task(user_id, task_id)**: Marks user's task as completed
- **delete_task(user_id, task_id)**: Deletes user's task
- **update_task(user_id, task_id, title?, description?)**: Updates user's task

## Phase 2: Component Architecture

### System Components

#### 1. Chat API Service
- **Responsibility**: Handle chat requests, manage conversation flow
- **Location**: `phase3/backend/api/chat.py`
- **Dependencies**: OpenAI Agent, MCP tools, authentication service

#### 2. MCP Tool Server
- **Responsibility**: Expose todo operations as standardized tools
- **Location**: `phase3/mcp-server/tools.py`
- **Dependencies**: Database models, authentication validation

#### 3. AI Agent Controller
- **Responsibility**: Process user input, determine intent, call appropriate tools
- **Location**: `phase3/backend/agents/todo_agent.py`
- **Dependencies**: MCP tools, conversation context

#### 4. Conversation Manager
- **Responsibility**: Load/reconstruct conversation context from database
- **Location**: `phase3/backend/managers/conversation_manager.py`
- **Dependencies**: Database models, message persistence

#### 5. Frontend Chat Interface
- **Responsibility**: Display chat interface, handle user input/output
- **Location**: `phase3/frontend/src/app/chat/`
- **Dependencies**: Existing auth context, chat API

### Integration Points

1. **Frontend ↔ Backend**: Chat API endpoints with JWT authentication
2. **Backend ↔ AI Agent**: OpenAI Assistant API with MCP tools
3. **AI Agent ↔ MCP Server**: Standardized tool calling protocol
4. **MCP Server ↔ Database**: SQLModel operations with user validation

## Phase 3: Implementation Sequence

### Sprint 1: Infrastructure Setup
1. Set up phase3 directory structure
2. Install required dependencies (openai, mcp-sdk-python)
3. Extend database models with conversation/message tables
4. Create basic FastAPI chat endpoint skeleton

### Sprint 2: MCP Server Implementation
1. Implement MCP tool server
2. Create individual MCP tools (add_task, list_tasks, etc.)
3. Add user validation to all MCP operations
4. Test MCP tools with simple direct calls

### Sprint 3: AI Agent Integration
1. Set up OpenAI Assistant with MCP tools
2. Implement conversation context reconstruction
3. Add intent interpretation for todo operations
4. Integrate with existing authentication

### Sprint 4: Frontend Integration
1. Create chat interface components
2. Connect to backend chat API
3. Implement loading/error states
4. Add JWT token handling for chat requests

### Sprint 5: Integration & Testing
1. End-to-end testing of chat-to-task workflows
2. User isolation validation
3. Error handling and graceful degradation
4. Performance optimization and documentation

## Phase 4: Quality Assurance

### Testing Strategy
- Unit tests for MCP tools with mock database
- Integration tests for chat API with real authentication
- End-to-end tests covering full user journeys
- Security tests for user isolation enforcement

### Success Metrics
- 95% of natural language commands result in correct operations
- Sub-5 second response times for 99% of requests
- Zero cross-user data access violations
- Successful authentication validation for all requests

## Phase 5: Deployment & Operations

### Deployment Strategy
- Containerized MCP server separate from main backend
- Stateless FastAPI service with external database
- CDN-cached static assets from Next.js frontend

### Monitoring & Observability
- Request logs with user activity tracking
- Error rates and response time metrics
- Authentication success/failure monitoring
- Conversation and task operation audit trails

### Maintenance Considerations
- Database migration scripts for new conversation/message tables
- MCP server health check endpoints
- Chat session cleanup routines
- Conversation retention policies