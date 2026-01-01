# Phase I Constitution: In-Memory Python Console Todo App

## Core Principles

### I. In-Memory Storage
All task data MUST be stored in-memory only during the application session. No persistence to files, databases, or external storage. Data is ephemeral and lost when the application exits. Rationale: Phase I is designed as a prototype/MVP to demonstrate core functionality without persistence complexity.

### II. Console-Only Interface
All user interaction MUST be through a command-line console interface. No GUI, web interface, or other UI technologies. Clear, readable text output and input prompts are required. Rationale: Keeps implementation simple for initial phase while focusing on core functionality.

### III. Python 3.13+ Compliance
All code MUST be compatible with Python 3.13+ and follow PEP 8 standards. No deprecated Python features. Rationale: Ensures modern Python standards and maintainability.

### IV. Task Uniqueness
Each task MUST have a unique identifier that persists during the session. Duplicate task IDs are not allowed. Rationale: Critical for proper CRUD operations.

### V. User Experience Excellence
All console output MUST be clear, consistent, and human-readable. Error messages MUST guide users to resolution. Rationale: Usability is critical even in a console application.

### VI. Validation and Error Handling
All user inputs MUST be validated with clear error messages for invalid data. The application MUST handle errors gracefully without crashing. Rationale: Robust applications must handle edge cases and user errors.

### VII. Clean Architecture
Code MUST follow clean architecture principles with separation of concerns. Task entity, TaskManager service, and console interface MUST be separated. Rationale: Enables maintainability and testing.

### VIII. Minimal Dependencies
Application MUST use only Python standard library with no external dependencies. Rationale: Keeps Phase I simple and focused on core functionality.

## Phase I Standards

### Storage Requirements
- In-memory Python list for task storage
- No file or database persistence
- All data lost on application exit
- Task IDs increment sequentially and are never reused during session

### Interface Requirements
- Menu-driven console interface
- Clear prompts and labels
- 80-character width formatting
- Consistent visual indicators (✓ for complete, ○ for pending)

### Validation Requirements
- Task titles must be non-empty
- Task IDs must be positive integers
- Proper error messages for invalid inputs
- Confirmation messages for all operations

### Testing Requirements
- Unit tests for all core functionality
- Test edge cases and error conditions
- Validate all user stories from specification

## Success Criteria

### Functional
- All 5 CRUD operations (Add, View, Update, Delete, Mark Complete) work correctly
- Task data integrity maintained throughout session
- Proper error handling and user feedback
- All acceptance scenarios from spec pass

### Non-Functional
- Console interface is responsive (operations complete within 1 second)
- Output is readable and consistently formatted
- Application handles up to 100 tasks without performance issues
- PEP 8 compliance maintained

## Governance

This constitution governs Phase I development. Any deviations require explicit approval and documentation of rationale. All code, tests, and documentation MUST comply with these principles and standards.

For Phase I, all features must be implemented and tested before moving to Phase II (web application).
