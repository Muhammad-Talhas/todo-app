import openai
from src.config import OPENAI_API_KEY

class TodoAgent:
    def __init__(self):
        # Ensure OPENAI_API_KEY is not None before initializing
        if OPENAI_API_KEY is None:
            raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
        
        # openai.api_key is deprecated in newer versions, client handles it
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)

    def process_message(self, user_id: str, message_content: str):
        # This will eventually contain logic to interact with OpenAI Assistant
        # and call MCP tools.
        # For now, it's a placeholder.
        return f"Hello {user_id}, I received your message: '{message_content}'. I am a todo agent."
