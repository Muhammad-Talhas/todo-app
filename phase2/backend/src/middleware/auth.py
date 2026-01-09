from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlmodel import Session
from jose import JWTError
from typing import Optional
from ..database import get_session
from ..services.auth import verify_token
import os

security = HTTPBearer()

def get_current_user_id(credentials: HTTPAuthorizationCredentials = Depends(security)) -> int:
    """
    Dependency to get the current user ID from the JWT token.
    Raises HTTPException if the token is invalid or expired.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        token = credentials.credentials
        payload = verify_token(token)

        if payload is None:
            raise credentials_exception

        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception

        return int(user_id)

    except JWTError:
        raise credentials_exception

def verify_user_owns_resource(current_user_id: int, requested_user_id: int) -> bool:
    """
    Verify that the current user owns the requested resource.
    Returns True if the user_id in the token matches the requested user_id.
    """
    return current_user_id == requested_user_id

def get_current_user_optional(credentials: HTTPAuthorizationCredentials = Depends(security)) -> Optional[int]:
    """
    Dependency to get the current user ID from the JWT token (optional).
    Returns None if the token is invalid or expired.
    """
    try:
        token = credentials.credentials
        payload = verify_token(token)

        if payload is None:
            return None

        user_id: str = payload.get("sub")
        if user_id is None:
            return None

        return int(user_id)

    except JWTError:
        return None