from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from ...database import get_session
from ...models.task import Task, TaskCreate, TaskRead, TaskUpdate, TaskPatch
from ...middleware.auth import get_current_user_id, verify_user_owns_resource

router = APIRouter()

@router.get("/tasks", response_model=List[TaskRead])
def get_tasks(
    user_id: int,
    current_user_id: int = Depends(get_current_user_id),
    session: Session = Depends(get_session)
):
    if not verify_user_owns_resource(current_user_id, user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot access other user's tasks"
        )

    statement = select(Task).where(Task.user_id == user_id)
    tasks = session.exec(statement).all()
    return tasks

@router.post("/tasks", response_model=TaskRead)
def create_task(
    user_id: int,
    task: TaskCreate,
    current_user_id: int = Depends(get_current_user_id),
    session: Session = Depends(get_session)
):
    if not verify_user_owns_resource(current_user_id, user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot create tasks for other users"
        )

    db_task = Task.model_validate(task)
    db_task.user_id = user_id
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@router.get("/tasks/{id}", response_model=TaskRead)
def get_task(
    user_id: int,
    id: int,
    current_user_id: int = Depends(get_current_user_id),
    session: Session = Depends(get_session)
):
    if not verify_user_owns_resource(current_user_id, user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot access other user's tasks"
        )

    statement = select(Task).where(Task.id == id, Task.user_id == user_id)
    db_task = session.exec(statement).first()

    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return db_task

@router.put("/tasks/{id}", response_model=TaskRead)
def update_task(
    user_id: int,
    id: int,
    task_update: TaskUpdate,
    current_user_id: int = Depends(get_current_user_id),
    session: Session = Depends(get_session)
):
    if not verify_user_owns_resource(current_user_id, user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot update other user's tasks"
        )

    statement = select(Task).where(Task.id == id, Task.user_id == user_id)
    db_task = session.exec(statement).first()

    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    # Update task fields
    for field, value in task_update.dict(exclude_unset=True).items():
        setattr(db_task, field, value)

    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@router.delete("/tasks/{id}")
def delete_task(
    user_id: int,
    id: int,
    current_user_id: int = Depends(get_current_user_id),
    session: Session = Depends(get_session)
):
    if not verify_user_owns_resource(current_user_id, user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot delete other user's tasks"
        )

    statement = select(Task).where(Task.id == id, Task.user_id == user_id)
    db_task = session.exec(statement).first()

    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    session.delete(db_task)
    session.commit()
    return {"message": "Task deleted successfully"}

@router.patch("/tasks/{id}/complete", response_model=TaskRead)
def update_task_completion(
    user_id: int,
    id: int,
    task_patch: TaskPatch,
    current_user_id: int = Depends(get_current_user_id),
    session: Session = Depends(get_session)
):
    if not verify_user_owns_resource(current_user_id, user_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied: Cannot update other user's tasks"
        )

    statement = select(Task).where(Task.id == id, Task.user_id == user_id)
    db_task = session.exec(statement).first()

    if not db_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    # Update completion status
    db_task.completed = task_patch.completed

    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task