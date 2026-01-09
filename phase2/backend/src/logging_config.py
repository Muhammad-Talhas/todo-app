import logging
import sys
from datetime import datetime
from pathlib import Path

def setup_logging():
    """Configure logging for the application with security event logging."""

    # Create logs directory if it doesn't exist
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    # Create logger
    logger = logging.getLogger("todo_app")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if already configured
    if logger.handlers:
        return logger

    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(detailed_formatter)

    # File handler for general logs
    general_file_handler = logging.FileHandler(logs_dir / "app.log")
    general_file_handler.setLevel(logging.INFO)
    general_file_handler.setFormatter(detailed_formatter)

    # File handler for security events
    security_file_handler = logging.FileHandler(logs_dir / "security.log")
    security_file_handler.setLevel(logging.WARNING)
    security_file_handler.setFormatter(detailed_formatter)

    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(general_file_handler)
    logger.addHandler(security_file_handler)

    # Also configure the root logger for third-party libraries
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    return logger

# Initialize the logger
app_logger = setup_logging()

def log_security_event(event_type: str, user_id: int = None, ip_address: str = None, details: str = None):
    """Log a security-related event."""
    message = f"SECURITY EVENT: {event_type}"
    if user_id:
        message += f" | User ID: {user_id}"
    if ip_address:
        message += f" | IP: {ip_address}"
    if details:
        message += f" | Details: {details}"

    app_logger.warning(message)

def log_user_action(action: str, user_id: int, details: str = None):
    """Log a user action for audit trail."""
    message = f"USER ACTION: {action} | User ID: {user_id}"
    if details:
        message += f" | Details: {details}"

    app_logger.info(message)