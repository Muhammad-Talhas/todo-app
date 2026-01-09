# Quickstart Guide: Secure Multi-User Todo Web Application

## Prerequisites
- Node.js 18+ for frontend
- Python 3.11+ for backend
- Neon Serverless PostgreSQL account
- Better Auth account or self-hosted instance

## Setup Instructions

### 1. Clone and Navigate
```bash
# Clone the repository
git clone <repository-url>
cd <repository-name>
```

### 2. Create Phase 2 Directory Structure
```bash
mkdir -p phase2/{frontend,backend}
```

### 3. Backend Setup
```bash
cd phase2/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install fastapi sqlmodel uvicorn python-jose python-multipart python-dotenv

# Create project structure
mkdir -p src/{models,services,api/routes}
```

### 4. Frontend Setup
```bash
cd phase2/frontend

# Initialize Next.js project
npx create-next-app@latest . --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"

# Install additional dependencies
npm install @better-auth/react better-auth
```

### 5. Environment Variables
Create `.env` files in both frontend and backend:

**Backend (.env):**
```env
DATABASE_URL="postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require"
BETTER_AUTH_SECRET="your-super-secret-jwt-key-here"
BETTER_AUTH_URL="http://localhost:3000"
```

**Frontend (.env.local):**
```env
NEXT_PUBLIC_API_URL="http://localhost:8000"
NEXT_PUBLIC_BETTER_AUTH_URL="http://localhost:3000"
```

### 6. Run the Applications

**Backend:**
```bash
cd phase2/backend
uvicorn src.main:app --reload --port 8000
```

**Frontend:**
```bash
cd phase2/frontend
npm run dev
```

## API Endpoints
- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- API Base: http://localhost:8000/api/{user_id}/

## Testing the API
1. Register a user via the frontend
2. Login and obtain JWT token
3. Use the token to access API endpoints with proper user_id
4. Test all CRUD operations on tasks

## Common Issues
- Ensure JWT token is properly included in Authorization header
- Verify that user_id in URL matches the authenticated user
- Check database connection string format for Neon
- Confirm CORS settings allow frontend-backend communication