from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import Dict
from ...database import get_session
from ...models.user import User, UserCreate, UserRead
from ...services.auth import authenticate_user, create_access_token, create_user

router = APIRouter()

@router.post("/register", response_model=UserRead)
def register(user_create: UserCreate, session: Session = Depends(get_session)):
    """Register a new user."""
    # Check if user already exists
    from sqlmodel import select
    statement = select(User).where(User.email == user_create.email)
    existing_user = session.exec(statement).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Create new user
    db_user = create_user(session, user_create)

    # Create access token
    access_token_expires = None  # Use default expiration
    access_token = create_access_token(
        data={"sub": str(db_user.id)}, expires_delta=access_token_expires
    )

    # Return user data and token
    return {
        "id": db_user.id,
        "email": db_user.email,
        "name": db_user.name,
        "created_at": db_user.created_at,
        "updated_at": db_user.updated_at,
        "is_active": db_user.is_active
    }


@router.post("/login")
def login(email: str, password: str, session: Session = Depends(get_session)) -> Dict:
    """Authenticate user and return access token."""
    user = authenticate_user(session, email, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )

    access_token = create_access_token(data={"sub": str(user.id)})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "name": user.name
        }
    }


@router.post("/logout")
def logout():
    """Logout user (client-side token invalidation)."""
    # In a real implementation, you might want to add the token to a blacklist
    # For this implementation, we just return a success message
    return {"message": "Logged out successfully"}


# Note: This router should be included in main.py, not here to avoid circular imports