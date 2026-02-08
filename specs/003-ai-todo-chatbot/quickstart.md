# Quickstart Guide: AI-powered Todo Chatbot

**Feature**: 003-ai-todo-chatbot
**Created**: 2026-02-08

## Prerequisites

- Python 3.13+
- Node.js 18+
- Access to OpenAI API
- Access to MCP SDK
- Phase 2 backend running (with Better Auth and database)

## Setup Instructions

### 1. Clone and Navigate
```bash
cd phase3
```

### 2. Backend Setup
```bash
cd backend
pip install -r requirements.txt  # Or use uv if available
export OPENAI_API_KEY="your-openai-key"
export DATABASE_URL="your-neon-db-url"
export AUTH_SECRET="your-auth-secret"
```

### 3. MCP Server Setup
```bash
cd mcp-server
pip install -r requirements.txt
export DATABASE_URL="your-neon-db-url"
python mcp_server.py
```

### 4. Start the Services
```bash
# Terminal 1: Start MCP server
cd phase3/mcp-server
python server.py

# Terminal 2: Start backend
cd phase3/backend
uvicorn main:app --reload

# Terminal 3: Start frontend (reuse Phase 2)
cd phase2/frontend
npm run dev
```

## Configuration

### Environment Variables
Create `.env` file in backend directory:
```
OPENAI_API_KEY=your_openai_key_here
DATABASE_URL=your_neon_db_connection_string
AUTH_SECRET=your_auth_secret_from_phase2
JWT_ALGORITHM=HS256
MCP_SERVER_URL=http://localhost:3001
```

## Usage Examples

### Interacting with the Chatbot
1. Log in to the application using your Phase 2 credentials
2. Navigate to the chat interface
3. Type natural language commands like:
   - "Add a task to buy groceries"
   - "Show me my tasks"
   - "Mark the meeting task as complete"
   - "Remove the expired task"

### API Usage
```bash
curl -X POST \
  http://localhost:8000/api/1/chat \
  -H 'Authorization: Bearer YOUR_JWT_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "message": "Add a task to call mom tomorrow"
  }'
```

## Development

### Running Tests
```bash
# Backend tests
cd phase3/backend
pytest

# MCP server tests
cd phase3/mcp-server
pytest
```

### Building for Production
```bash
# Build backend
cd phase3/backend
python -m build

# Build frontend (reuse Phase 2)
cd phase2/frontend
npm run build
```