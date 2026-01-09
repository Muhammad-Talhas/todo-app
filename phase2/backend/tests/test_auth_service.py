import pytest
from unittest.mock import Mock, patch
from sqlmodel import Session
from src.models.user import User
from src.services.auth import authenticate_user, create_access_token, verify_token

def test_authenticate_user_success():
    """Test successful user authentication."""
    # Mock the database session
    mock_session = Mock(spec=Session)

    # Create a mock user
    mock_user = User(
        id=1,
        email="test@example.com",
        password_hash="$2b$12$LQv3c1eS8Jfyqrq.LKg/.Oj4mYBFT6BKrKCuKGq5/W4n5xHgK7aF2"  # bcrypt hash for "password"
    )

    # Mock the query result
    mock_query_result = Mock()
    mock_query_result.first.return_value = mock_user

    # Mock the session.exec method
    mock_session.exec.return_value = mock_query_result

    # Test authentication
    result = authenticate_user(mock_session, "test@example.com", "password")

    assert result == mock_user

def test_authenticate_user_invalid_credentials():
    """Test authentication with invalid credentials."""
    # Mock the database session
    mock_session = Mock(spec=Session)

    # Mock the query result to return None (no user found)
    mock_query_result = Mock()
    mock_query_result.first.return_value = None

    # Mock the session.exec method
    mock_session.exec.return_value = mock_query_result

    # Test authentication with non-existent user
    result = authenticate_user(mock_session, "nonexistent@example.com", "password")

    assert result is None

def test_create_and_verify_token():
    """Test creating and verifying a JWT token."""
    # Create a token
    data = {"sub": "1", "email": "test@example.com"}
    token = create_access_token(data)

    # Verify the token
    payload = verify_token(token)

    assert payload is not None
    assert payload["sub"] == "1"
    assert payload["email"] == "test@example.com"