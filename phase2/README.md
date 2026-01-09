# Secure Multi-User Todo Web Application

This is a secure, multi-user Todo web application built with Next.js frontend and FastAPI backend, featuring JWT-based authentication and PostgreSQL database.

## Features

- User registration and authentication with JWT tokens
- Secure task management (CRUD operations)
- Multi-user support with data isolation
- Responsive web interface
- End-to-end encryption for sensitive data

## Tech Stack

- **Frontend**: Next.js 16+, TypeScript, Tailwind CSS
- **Backend**: FastAPI, Python 3.11+
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: JWT tokens with Better Auth
- **ORM**: SQLModel

## Setup Instructions

### Prerequisites

- Node.js 18+
- Python 3.11+
- PostgreSQL (or Neon Serverless PostgreSQL account)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd phase2/backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. Start the backend server:
   ```bash
   uvicorn src.api.main:app --reload --port 8000
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd phase2/frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables:
   ```bash
   cp .env.local.example .env.local
   # Edit .env.local with your configuration
   ```

4. Start the frontend server:
   ```bash
   npm run dev
   ```

## API Endpoints

The application provides the following API endpoints:

- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `POST /auth/logout` - User logout
- `GET /api/{user_id}/tasks` - Get user's tasks
- `POST /api/{user_id}/tasks` - Create a new task
- `GET /api/{user_id}/tasks/{id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{id}` - Update a specific task
- `DELETE /api/{user_id}/tasks/{id}` - Delete a specific task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Update task completion status

## Security Features

- JWT token authentication for all API endpoints
- User data isolation (users can only access their own tasks)
- Password hashing using bcrypt
- Input validation and sanitization
- Protection against common web vulnerabilities

## Environment Variables

### Backend (.env)

- `DATABASE_URL` - PostgreSQL database connection string
- `BETTER_AUTH_SECRET` - Secret key for JWT signing
- `BETTER_AUTH_URL` - Base URL for the application

### Frontend (.env.local)

- `NEXT_PUBLIC_API_URL` - Backend API URL
- `NEXT_PUBLIC_BETTER_AUTH_URL` - Auth service URL

## Running Tests

TODO: Add test instructions once testing framework is implemented.

## Deployment

TODO: Add deployment instructions for production environment.