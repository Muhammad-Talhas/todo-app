# src/api/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

# Imports based on your folder structure
from src.logging_config import app_logger, log_security_event, log_user_action
from src.api.routes import tasks, auth
from src.config import settings, get_settings
from src.database import create_db_and_tables
from src.models.user import User 
from src.models.task import Task

# Define the lifespan function
@asynccontextmanager
async def lifespan(app: FastAPI):
    # This code runs on startup
    print("Starting up: Creating database tables...")
    create_db_and_tables()
    yield
    # This code runs on shutdown (if needed)
    print("Shutting down...")

# Create FastAPI app instance
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Secure multi-user Todo API with JWT authentication",
    debug=settings.debug,
    lifespan=lifespan 
)

# Setup CORS middleware
origins = (
    [origin.strip() for origin in settings.backend_cors_origins.split(",")]
    if settings.backend_cors_origins else ["*"]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Authorization", "Content-Type"],
)

# Include routers
app.include_router(tasks.router, prefix="/api")
app.include_router(auth.router, prefix="/auth", tags=["auth"])

# Exception handlers
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    """Custom handler for HTTP exceptions."""
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    """Custom handler for request validation errors."""
    return JSONResponse(
        status_code=422,
        content={
            "detail": "Validation error",
            "errors": [
                {
                    "loc": error["loc"],
                    "msg": error["msg"],
                    "type": error["type"]
                } for error in exc.errors()
            ]
        }
    )

# Basic routes
@app.get("/")
def read_root():
    return {"message": f"{settings.app_name} is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
