# Claude Agent Context: Phase 2 Todo Web Application

## Technologies Introduced

### Frontend Technologies
- **Next.js 16+**: React framework with App Router for the web application
- **Better Auth**: Authentication library with JWT support for user management
- **Tailwind CSS**: Utility-first CSS framework for styling
- **TypeScript**: Type-safe JavaScript for frontend development

### Backend Technologies
- **FastAPI**: High-performance Python web framework for API development
- **SQLModel**: SQL database modeling library combining SQLAlchemy and Pydantic
- **Neon Serverless PostgreSQL**: Cloud database service for data persistence
- **python-jose**: JWT token encoding/decoding library for authentication

## Key Architecture Patterns

### Frontend Architecture
- **App Router**: Next.js routing system for page organization
- **Component-Based**: React components for UI elements (TaskList, TaskForm, etc.)
- **Context API**: State management for authentication tokens and user data
- **API Client**: Centralized service for making authenticated API calls

### Backend Architecture
- **RESTful API**: Standard HTTP methods for resource operations
- **Model-Service-Route Pattern**: Separation of data models, business logic, and API endpoints
- **JWT Middleware**: Authentication and authorization enforcement
- **SQLModel ORM**: Database abstraction layer with type safety

## Security Considerations
- JWT token validation on all API endpoints
- User ID matching between JWT and URL parameters
- Secure password hashing for user accounts
- Environment variable management for secrets

## Integration Points
- Frontend API calls to backend endpoints
- JWT token flow from authentication to API requests
- Database connection from backend to Neon PostgreSQL
- Environment variable sharing between frontend and backend