# Tasks: Phase I - In-Memory Python Console Todo App

**Input**: Design documents from `/specs/001-phase1-console-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

---
**IMPORTANT**: The tasks below are GENERATED TASKS based on user stories from spec.md, data-model.md, and contracts/. All tasks are actionable and specific enough for LLM execution without additional context.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [ ] [X] T002 [P] Initialize Python project with UV and create pyproject.toml
- [ ] [X] T003 [P] Create empty `__init__.py` files in src/ and tests/
- [ ] [X] T004 [P] Create empty source files: src/main.py, src/task.py, src/task_manager.py, src/utils.py
- [ ] [X] T005 [P] Create empty test files: tests/test_task.py, tests/test_task_manager.py, tests/test_utils.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] [X] T006 Implement Task dataclass in src/task.py with id, title, description, completed fields and __post_init__ validation
- [ ] [X] T007 Implement TaskManager class in src/task_manager.py with tasks list, next_id counter, and all CRUD methods
- [ ] [X] T008 Implement input validation functions in src/utils.py (validate_title, validate_task_id)
- [ ] [X] T009 Implement formatting functions in src/utils.py (format_task, format_task_list)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Create Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to create tasks with title and description, auto-generating unique IDs

**Independent Test**: Users can add a task by entering a title and description, then see a confirmation message showing the task was created with a unique ID. Delivers immediate value as a simple task recording tool.

### Implementation for User Story 1

- [ ] [X] T010 [P] [US1] Add menu option "Add Task" to src/main.py main loop with prompt for title and description
- [ ] [X] T011 [P] [US1] Implement user input collection in src/main.py for task title and description (optional)
- [ ] [X] T012 [US1] Call TaskManager.add_task(title, description) from src/main.py and display confirmation with task ID

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P1) 🎯 MVP

**Goal**: Enable users to view all tasks with filtering options (all, completed, pending)

**Independent Test**: Users can view all tasks in a formatted list showing ID, title, description, and completion status. Users can also filter to see only completed or only pending tasks. Delivers value as a task visualization tool.

### Implementation for User Story 2

- [ ] [X] T013 [P] [US2] Add menu option "View Tasks" to src/main.py main loop with sub-menu for filtering
- [ ] [X] T014 [P] [US2] Implement display_menu function in src/main.py to show view options: (1) All Tasks, (2) Completed, (3) Pending
- [ ] [X] T015 [P] [US2] Implement display_all_tasks function in src/main.py that calls TaskManager.view_all_tasks() and formats output
- [ ] [X] T016 [P] [US2] Implement display_filtered_tasks function in src/main.py that calls TaskManager.view_tasks_by_status(completed) and formats output
- [ ] [X] T017 [US2] Handle empty task list case in src/main.py by displaying "No tasks found" message
- [ ] [X] T018 [US2] Use utils.format_task_list() in src/main.py for consistent task display formatting

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 5 - Mark Task Completion Status (Priority: P1) 🎯 MVP

**Goal**: Enable users to toggle task completion status between complete and incomplete

**Independent Test**: Users can toggle a task's completion status between complete and incomplete by providing a task ID. The system confirms the status change. Delivers value as a progress tracking tool.

### Implementation for User Story 5

- [ ] [X] T019 [P] [US5] Add menu option "Mark Complete/Incomplete" to src/main.py main loop
- [ ] [X] T020 [P] [US5] Implement user input collection in src/main.py for task ID and status (complete/incomplete)
- [ ] [X] T021 [P] [US5] Implement mark_task function in src/main.py that calls TaskManager.mark_task_completion(task_id, completed)
- [ ] [X] T022 [US5] Add error handling in src/main.py for invalid task IDs with informative error message
- [ ] [X] T023 [US5] Display confirmation message in src/main.py after successful status change

**Checkpoint**: At this point, User Stories 1, 2, AND 5 should all be independently functional

---

## Phase 6: User Story 3 - Update Task Information (Priority: P2)

**Goal**: Enable users to update task title and/or description for existing tasks

**Independent Test**: Users can update an existing task's title and/or description by providing a task ID. The system confirms successful updates. Delivers value as a task editing tool.

### Implementation for User Story 3

- [ ] [X] T024 [P] [US3] Add menu option "Update Task" to src/main.py main loop
- [ ] [X] T025 [P] [US3] Implement user input collection in src/main.py for task ID, new title (optional), new description (optional)
- [ ] [X] T026 [P] [US3] Implement update_task function in src/main.py that calls TaskManager.update_task(task_id, title, description)
- [ ] [X] T027 [US3] Add error handling in src/main.py for invalid task IDs and missing fields
- [ ] [X] T028 [US3] Display confirmation message in src/main.py after successful update with updated task details

**Checkpoint**: All user stories (1, 2, 3, 5) should now be independently functional

---

## Phase 7: User Story 4 - Delete Tasks (Priority: P2)

**Goal**: Enable users to remove tasks from their task list

**Independent Test**: Users can delete a task by providing its ID. The system removes the task from memory and confirms the deletion. Delivers value as a task removal tool.

### Implementation for User Story 4

- [ ] [X] T029 [P] [US4] Add menu option "Delete Task" to src/main.py main loop
- [ ] [X] T030 [P] [US4] Implement user input collection in src/main.py for task ID
- [ ] [X] T031 [P] [US4] Implement delete_task function in src/main.py that calls TaskManager.delete_task(task_id)
- [ ] [X] T032 [US4] Add error handling in src/main.py for invalid task IDs with informative error message
- [ ] [X] T033 [US4] Display confirmation message in src/main.py after successful deletion

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] [X] T034 [P] Add "Exit" menu option to src/main.py main loop with goodbye message
- [ ] [X] T035 [P] Add application title and separator lines to src/main.py for professional appearance
- [ ] [X] T036 [P] Implement consistent menu numbering and spacing in src/main.py main loop
- [ ] [X] T037 [P] Add input validation in src/main.py for numeric menu choices
- [ ] [X] T038 [P] Add friendly error messages in src/main.py for invalid menu choices
- [ ] [X] T039 [P] Ensure all output in src/main.py fits within 80-character terminal width
- [ ] [X] T040 [P] Add docstrings to all functions in src/main.py, src/task.py, src/task_manager.py, src/utils.py
- [ ] [X] T041 [P] Verify all error messages in src/main.py are clear, informative, and guide user resolution
- [ ] [X] T042 [P] Test all user stories from spec.md manually via command line
- [ ] [X] T043 Verify PEP 8 compliance using `uv run ruff check src/` (if ruff installed)

**Checkpoint**: All tasks complete - Phase I is ready for final validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phases 3-7)**: All depend on Foundational phase completion
  - User stories can proceed in priority order (P1 → P2)
  - P1 stories: US1 (Create) → US2 (View) → US5 (Mark Complete)
  - P2 stories: US3 (Update) → US4 (Delete)
  - Each user story is independently testable
- **Polish (Phase 8)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) and US1 - Needs tasks to display
- **User Story 5 (P1)**: Can start after Foundational (Phase 2) and US1 - Needs tasks to mark
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) and US1 - Needs tasks to update
- **User Story 4 (P2)**: Can start after Foundational (Phase 2) and US1 - Needs tasks to delete

### Within Each User Story

- All implementation tasks for a story should complete in order
- Tasks marked [P] within a story can be executed in parallel (different functions/sections)
- Each story should be testable independently after completion

### Parallel Opportunities

- All Setup tasks ([X] T002-[X] T005) can run in parallel
- All Foundational tasks ([X] T007-[X] T009) can run in parallel
- Within US1: [X] T010-[X] T012 must run sequentially
- Within US2: [X] T013-[X] T018 can be executed with parallelism where marked
- Within US5: [X] T019-[X] T023 can be executed with parallelism where marked
- Within US3: [X] T024-[X] T028 can be executed with parallelism where marked
- Within US4: [X] T029-[X] T033 can be executed with parallelism where marked
- Polish tasks ([X] T034-[X] T043) can run in parallel

---

## Parallel Example: User Story 2

```bash
# Launch menu and sub-menu creation together:
Task: "Add menu option 'View Tasks' to src/main.py main loop with sub-menu for filtering"
Task: "Implement display_menu function in src/main.py to show view options"

# Launch display functions together:
Task: "Implement display_all_tasks function in src/main.py that calls TaskManager.view_all_tasks() and formats output"
Task: "Implement display_filtered_tasks function in src/main.py that calls TaskManager.view_tasks_by_status(completed) and formats output"
Task: "Handle empty task list case in src/main.py by displaying 'No tasks found' message"
Task: "Use utils.format_task_list() in src/main.py for consistent task display formatting"
```

---

## Implementation Strategy

### MVP First (User Stories 1, 2, 5 Only)

1. Complete Phase 1: Setup (["X] T001"]-[X] T005)
2. Complete Phase 2: Foundational ([X] T006-[X] T009) - CRITICAL
3. Complete Phase 3: User Story 1 ([X] T010-[X] T012)
4. Complete Phase 4: User Story 2 ([X] T013-[X] T018)
5. Complete Phase 5: User Story 5 ([X] T019-[X] T023)
6. **STOP and VALIDATE**: Test User Stories 1, 2, 5 independently
7. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → MVP core: create tasks
3. Add User Story 2 → Test independently → MVP core + visibility: create + view
4. Add User Story 5 → Test independently → MVP core: create + view + mark complete
5. Add User Story 3 → Test independently → Enhancement: update tasks
6. Add User Story 4 → Test independently → Enhancement: delete tasks
7. Complete Polish → Final Phase I application
8. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (["X] T001"]-[X] T009)
2. Once Foundational is done:
   - Developer A: User Story 1 (Create Tasks) - [X] T010-[X] T012
   - Developer B: User Story 2 (View Tasks) - [X] T013-[X] T018
   - Developer C: User Story 5 (Mark Complete) - [X] T019-[X] T023
3. After P1 stories complete:
   - Developer A: User Story 3 (Update Tasks) - [X] T024-[X] T028
   - Developer B: User Story 4 (Delete Tasks) - [X] T029-[X] T033
4. All developers contribute to Polish - [X] T034-[X] T043
5. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies on incomplete tasks
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- All tasks reference exact file paths (e.g., src/main.py:line_number)
- P1 user stories: US1 (Create), US2 (View), US5 (Mark Complete) - MVP scope
- P2 user stories: US3 (Update), US4 (Delete) - Enhancement scope
- Total tasks: 43
- Tasks per user story:
  - Setup: 5 tasks
  - Foundational: 4 tasks (blocking)
  - US1 (Create): 3 tasks
  - US2 (View): 6 tasks
  - US5 (Mark Complete): 5 tasks
  - US3 (Update): 5 tasks
  - US4 (Delete): 5 tasks
  - Polish: 10 tasks
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
