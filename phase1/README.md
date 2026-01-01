# Phase I: In-Memory Python Console Todo App

This is Phase I of the multi-phase Todo application project: an in-memory console-based application supporting CRUD operations.

## Overview

A simple console-based todo application written in Python that supports:
- Adding tasks with title and description
- Viewing all tasks with filtering options
- Updating task details
- Deleting tasks
- Marking tasks as complete/incomplete
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
1. Add Task
2. View Tasks (with filtering options)
3. Update Task
4. Delete Task
5. Mark Complete/Incomplete
6. Exit

## Features

- Clear, human-readable console output
- Input validation and error handling
- Task ID generation and uniqueness
- Filtering by completion status
- In-memory storage for session-only data

## Architecture

- `src/task.py`: Task entity with validation
- `src/task_manager.py`: In-memory storage and CRUD operations
- `src/utils.py`: Validation and formatting utilities
- `src/main.py`: Console interface and user interaction

## Limitations

- Data is stored in-memory only (lost on exit)
- Single-user session
- No external persistence
- Console-based interface only
