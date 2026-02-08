from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Optional
from sqlmodel import Session
from src.database.database import get_session
from src.managers.conversation_manager import ConversationManager
from src.agents.todo_agent import TodoAgent
from src.middleware.user_validation import get_current_user
import uuid

router = APIRouter()

class ChatMessage(BaseModel):
    message: str
    conversation_id: Optional[uuid.UUID] = None

@router.post("/chat/")
async def chat(
    chat_message: ChatMessage,
    current_user: uuid.UUID = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    conversation_manager = ConversationManager(session)
    todo_agent = TodoAgent()

    conversation_id = chat_message.conversation_id
    if not conversation_id:
        conversation = conversation_manager.create_conversation(user_id=current_user)
        conversation_id = conversation.id

    # Store user message
    conversation_manager.add_message(
        conversation_id=conversation_id, role="user", content=chat_message.message
    )

    # Process message with AI agent
    agent_response = todo_agent.process_message(str(current_user), chat_message.message)

    # Store agent response
    conversation_manager.add_message(
        conversation_id=conversation_id, role="assistant", content=agent_response
    )

    return {"response": agent_response, "conversation_id": conversation_id}
