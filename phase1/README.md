# Phase I: In-Memory Python Console Todo App

This is Phase I of the multi-phase Todo application project: an in-memory console-based application supporting advanced CRUD operations with priority, tags, search, and more.

## Overview

A feature-rich console-based todo application written in Python that supports:
- **Basic Operations**: Adding, viewing, updating, deleting, and marking tasks as complete/incomplete
- **Advanced Features**:
  - Priorities & Tags/Categories – Assign levels (high/medium/low) or labels (work/home)
  - Search & Filter – Search by keyword; filter by status, priority, or date
  - Sort Tasks – Reorder by due date, priority, or alphabetically
  - Due Dates & Time Reminders – Set deadlines with date/time pickers
- All data stored in-memory only (no persistence)

## Prerequisites

- Python 3.13+
- UV package manager

## Setup

1. Clone the repository
2. Navigate to the phase1 directory: `cd phase1`
3. Install dependencies: `uv sync` or `pip install -r requirements.txt`

## Usage

Run the application:
```bash
python src/main.py
```

Follow the menu prompts to perform operations:
1. Add Task (with priority, tags, due date)
2. View Tasks (with filtering options)
3. Update Task (title, description, priority, tags, due date)
4. Delete Task
5. Mark Complete/Incomplete
6. Search Tasks (by keyword in title/description)
7. Sort Tasks (by priority, due date, or alphabetically)
8. Filter by Priority (high, medium, low)
9. Filter by Tag (show tasks with specific tag)
10. View Overdue Tasks (show tasks past due date that aren't completed)
11. Task Statistics (show completion rates and summaries)
12. Exit

## Features

- **Clear, human-readable console output** with visual indicators (🔴 High priority, 🟡 Medium priority, 🟢 Low priority)
- **Input validation and error handling** with informative messages
- **Task ID generation and uniqueness** with sequential numbering
- **Advanced filtering** by status, priority, or tags
- **Powerful search** by keyword in title or description
- **Flexible sorting** by priority, due date, or alphabetical order
- **Due date support** with overdue task detection
- **Tagging system** for categorizing tasks
- **Priority system** with high/medium/low levels
- **Statistics dashboard** showing completion rates and summaries
- **In-memory storage** for session-only data

## Architecture

- `src/task.py`: Task entity with advanced features (priority, tags, due dates, etc.)
- `src/task_manager.py`: In-memory storage and advanced CRUD operations
- `src/utils.py`: Validation and formatting utilities
- `src/main.py`: Console interface and user interaction with all advanced features

## Limitations

- Data is stored in-memory only (lost on exit)
- Single-user session
- No external persistence
- Console-based interface only
- No recurring tasks yet (future enhancement)
