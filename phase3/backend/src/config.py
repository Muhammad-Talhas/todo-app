import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MCP_SERVER_URL = os.getenv("MCP_SERVER_URL")
MCP_SERVER_API_KEY = os.getenv("MCP_SERVER_API_KEY")

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key") # TODO: Change this to a strong random key
ALGORITHM = "HS256"

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db")
