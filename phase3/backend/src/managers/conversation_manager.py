from sqlmodel import Session, select
from src.models.conversation import Conversation
from src.models.message import Message
import uuid

class ConversationManager:
    def __init__(self, session: Session):
        self.session = session

    def create_conversation(self, user_id: uuid.UUID) -> Conversation:
        conversation = Conversation(user_id=user_id)
        self.session.add(conversation)
        self.session.commit()
        self.session.refresh(conversation)
        return conversation

    def add_message(self, conversation_id: uuid.UUID, role: str, content: str) -> Message:
        message = Message(conversation_id=conversation_id, role=role, content=content)
        self.session.add(message)
        self.session.commit()
        self.session.refresh(message)
        return message

    def get_messages(self, conversation_id: uuid.UUID) -> list[Message]:
        statement = select(Message).where(Message.conversation_id == conversation_id)
        messages = self.session.exec(statement).all()
        return messages
