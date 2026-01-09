import pytest
from unittest.mock import Mock, patch
from sqlmodel import Session
from src.models.task import Task
from src.services.task import get_tasks_by_user_id, create_task_for_user, get_task_by_id_and_user_id

def test_get_tasks_by_user_id():
    """Test getting tasks for a specific user."""
    # Mock the database session
    mock_session = Mock(spec=Session)

    # Create mock tasks
    mock_tasks = [
        Task(id=1, title="Test Task 1", completed=False, user_id=1),
        Task(id=2, title="Test Task 2", completed=True, user_id=1)
    ]

    # Mock the query result
    mock_query_result = Mock()
    mock_query_result.all.return_value = mock_tasks

    # Mock the session.exec method
    mock_session.exec.return_value = mock_query_result

    # Test getting tasks for user
    result = get_tasks_by_user_id(mock_session, 1)

    assert len(result) == 2
    assert result[0].title == "Test Task 1"
    assert result[1].title == "Test Task 2"

def test_create_task_for_user():
    """Test creating a task for a specific user."""
    # Mock the database session
    mock_session = Mock(spec=Session)

    # Create a task to be created
    from src.models.task import TaskCreate
    task_to_create = TaskCreate(
        title="New Task",
        description="A new task to be created",
        user_id=1
    )

    # Create the expected result
    expected_task = Task(
        id=1,
        title="New Task",
        description="A new task to be created",
        completed=False,
        user_id=1
    )

    # Mock the session.add and session.refresh methods
    mock_session.add = Mock()
    mock_session.commit = Mock()
    mock_session.refresh = Mock(side_effect=lambda obj: setattr(obj, 'id', 1))

    # Test creating task for user
    result = create_task_for_user(mock_session, task_to_create, 1)

    assert result.title == "New Task"
    assert result.description == "A new task to be created"
    assert result.user_id == 1
    assert mock_session.add.called
    assert mock_session.commit.called

def test_get_task_by_id_and_user_id():
    """Test getting a specific task for a specific user."""
    # Mock the database session
    mock_session = Mock(spec=Session)

    # Create a mock task
    mock_task = Task(id=1, title="Specific Task", completed=False, user_id=1)

    # Mock the query result
    mock_query_result = Mock()
    mock_query_result.first.return_value = mock_task

    # Mock the session.exec method
    mock_session.exec.return_value = mock_query_result

    # Test getting specific task for user
    result = get_task_by_id_and_user_id(mock_session, 1, 1)

    assert result is not None
    assert result.id == 1
    assert result.title == "Specific Task"
    assert result.user_id == 1

def test_get_task_by_id_and_user_id_not_found():
    """Test getting a task that doesn't exist for the user."""
    # Mock the database session
    mock_session = Mock(spec=Session)

    # Mock the query result to return None
    mock_query_result = Mock()
    mock_query_result.first.return_value = None

    # Mock the session.exec method
    mock_session.exec.return_value = mock_query_result

    # Test getting non-existent task for user
    result = get_task_by_id_and_user_id(mock_session, 999, 1)

    assert result is None