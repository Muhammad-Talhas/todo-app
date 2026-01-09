from sqlmodel import Session, select
from typing import List, Optional
from ..models.task import Task, TaskCreate, TaskUpdate, TaskPatch
from ..models.user import User

def get_tasks_by_user_id(session: Session, user_id: int) -> List[Task]:
    """Get all tasks for a specific user."""
    statement = select(Task).where(Task.user_id == user_id)
    return session.exec(statement).all()

def get_task_by_id_and_user_id(session: Session, task_id: int, user_id: int) -> Optional[Task]:
    """Get a specific task for a specific user."""
    statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
    return session.exec(statement).first()

def create_task_for_user(session: Session, task_create: TaskCreate, user_id: int) -> Task:
    """Create a new task for a specific user."""
    db_task = Task.model_validate(task_create)
    db_task.user_id = user_id
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

def update_task_for_user(session: Session, task_id: int, user_id: int, task_update: TaskUpdate) -> Optional[Task]:
    """Update a specific task for a specific user."""
    db_task = get_task_by_id_and_user_id(session, task_id, user_id)
    if not db_task:
        return None

    # Update task fields
    for field, value in task_update.dict(exclude_unset=True).items():
        setattr(db_task, field, value)

    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

def delete_task_for_user(session: Session, task_id: int, user_id: int) -> bool:
    """Delete a specific task for a specific user."""
    db_task = get_task_by_id_and_user_id(session, task_id, user_id)
    if not db_task:
        return False

    session.delete(db_task)
    session.commit()
    return True

def update_task_completion_for_user(session: Session, task_id: int, user_id: int, completed: bool) -> Optional[Task]:
    """Update the completion status of a specific task for a specific user."""
    db_task = get_task_by_id_and_user_id(session, task_id, user_id)
    if not db_task:
        return None

    db_task.completed = completed

    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task