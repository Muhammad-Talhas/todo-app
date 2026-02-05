from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from typing import List
from ...database import get_session
from ...models.task import Task, TaskCreate, TaskRead, TaskUpdate, TaskPatch
from .auth import get_current_user 
from ...models.user import User
from src.models.user import User

router = APIRouter()

@router.get("/{user_id}/tasks")
def get_tasks(
    user_id: str, 
    session: Session = Depends(get_session)
    # Ensure NO other 'Depends' are here for now!
):
    # Just fetch the tasks for the ID provided in the URL
    statement = select(Task).where(Task.user_id == user_id)
    tasks = session.exec(statement).all()
    
    print(f"DEBUG: Returning {len(tasks)} tasks for {user_id}")
    return tasks

# 1. Update/Toggle Task (Checkbox)
@router.patch("/{user_id}/tasks/{task_id}/complete")
def toggle_task(user_id: str, task_id: int, session: Session = Depends(get_session)):
    # Find the task by ID
    task = session.get(Task, task_id)
    
    if not task or task.user_id != user_id:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Task not found")

    # Flip the completed status
    task.completed = not task.completed
    
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

# 2. Delete Task
@router.delete("/{user_id}/tasks/{task_id}")
def delete_task(user_id: str, task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    
    if not task or task.user_id != user_id:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Task not found")

    session.delete(task)
    session.commit()
    return {"status": "success", "message": "Task deleted"}

@router.post("/{user_id}/tasks")
def create_task(
    user_id: str,
    task_data: TaskCreate,
    session: Session = Depends(get_session)
):
    # 1. Check if the user exists
    user = session.get(User, user_id)
    
    # 2. If the user doesn't exist, create them
    if not user:
        new_user = User(
            id=user_id, 
            email=f"{user_id}@example.com", 
            password_hash="temporary_password"
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)

    # 3. Create the task object
    new_task = Task(
        **task_data.dict(), 
        user_id=user_id
    )

    # 4. SAVE THE TASK TO THE DATABASE (The missing part!)
    session.add(new_task)
    session.commit()
    session.refresh(new_task)

    return new_task