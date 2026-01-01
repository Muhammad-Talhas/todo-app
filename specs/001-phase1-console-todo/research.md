# Phase 0 Research: Technology Decisions

**Feature**: Phase I - In-Memory Python Console Todo App
**Date**: 2026-01-01
**Purpose**: Research and justify technology choices for Technical Context items

## Technology Decisions

### 1. Language/Version: Python 3.13+

**Decision**: Python 3.13+ (latest stable release)

**Rationale**:
- Python has excellent readability and simplicity, ideal for console applications
- Rich standard library provides all necessary functionality (input/output, string manipulation, data structures)
- Strong community support and documentation
- Clean syntax supports PEP 8 compliance naturally
- UV package manager officially supports Python 3.13+
- Cross-platform compatibility (Windows, Linux, macOS) without code changes

**Alternatives Considered**:
1. **Python 3.12** - Rejected because Python 3.13 is the latest stable release with improved performance and features
2. **Python 3.11** - Rejected because Python 3.13 is newer and project specification explicitly requires 3.13+
3. **Node.js** - Rejected because specification requires Python 3.13+, and console apps are more idiomatic in Python for this use case
4. **Go** - Rejected because specification requires Python 3.13+, and Go would be premature optimization for a simple console app

---

### 2. Primary Dependencies: None (Standard Library Only)

**Decision**: Use Python standard library exclusively, no external dependencies

**Rationale**:
- Phase I is in-memory application with simple CRUD operations
- Standard library provides all necessary modules:
  - `dataclasses` for Task entity definition
  - `typing` for type hints
  - `builtins` for input/output and string manipulation
  - `unittest` or `pytest` for testing (pytest is a dev dependency, not runtime dependency)
- Reduces complexity and installation overhead
- Aligns with Phase I scope: MVP/prototype without premature optimization
- Consistent with constitution principle of technology constraint discipline

**Alternatives Considered**:
1. **Click** - Rejected because it's a CLI framework that adds unnecessary complexity for simple menu-driven interface
2. **Rich** - Rejected because rich text formatting is premature for Phase I, simple formatted strings suffice (FR-027 through FR-028)
3. **Pydantic** - Rejected because dataclasses provide sufficient validation for simple Task entity
4. **SQLAlchemy** - Rejected because Phase I explicitly forbids external databases (FR-025, in-memory only)

---

### 3. Storage: In-Memory Python List

**Decision**: Python list for in-memory task storage

**Rationale**:
- Simplest data structure for sequential task collection
- O(1) append (add task), O(n) search by ID, O(n) remove by ID
- All CRUD operations are in-memory, satisfying FR-025
- No persistence required for Phase I (specification constraints)
- Python list is built-in, no import needed
- Natural iteration for display and filtering operations

**Alternatives Considered**:
1. **Dictionary (ID → Task)** - Rejected because list maintains insertion order (important for sequential ID display), and O(n) search is acceptable for Phase I scope (up to 100 tasks)
2. **Database (SQLite)** - Rejected because specification explicitly forbids external databases, FR-025 mandates in-memory only
3. **File persistence** - Rejected because specification requires in-memory only, no file persistence
4. **collections.deque** - Rejected because we need random access by ID, not just FIFO operations

---

### 4. Testing: pytest

**Decision**: pytest as testing framework

**Rationale**:
- De facto standard for Python testing
- Simple, readable test syntax (no boilerplate)
- Powerful assertion messages with detailed diffs
- Fixture support for common test data
- Integration with UV for easy installation
- Follows Python best practices
- Compatible with PEP 8 and clean code principles

**Alternatives Considered**:
1. **unittest** (standard library) - Rejected because pytest offers superior developer experience, better error messages, and is more maintainable
2. **nose2** - Rejected because pytest is more modern and widely adopted
3. **unittest.mock** - Rejected because no mocking required for Phase I (all operations are in-memory, testable directly)

---

### 5. Target Platform: Command-Line Terminal

**Decision**: Any platform supporting Python 3.13+ (Windows, Linux, macOS)

**Rationale**:
- Python 3.13+ runs on all major platforms
- Console applications are inherently cross-platform
- `input()` and `print()` work identically across platforms
- No platform-specific code required
- Maximizes accessibility for developers and users

**Alternatives Considered**:
1. **Windows-only** - Rejected because Python is cross-platform, no reason to restrict to Windows
2. **Linux-only** - Rejected because Python is cross-platform, no reason to restrict to Linux
3. **Specific terminal emulator** - Rejected because standard input/output works across all terminals

---

### 6. Project Type: Single

**Decision**: Single project structure with /src and /tests directories

**Rationale**:
- Simplest appropriate structure for console application
- No frontend/backend separation needed (Phase I is command-line only)
- Single codebase reduces complexity
- Aligns with constitution principle of maintainable architecture (separation of concerns within single project)
- Follows Spec-Kit Plus conventions for single project type

**Alternatives Considered**:
1. **Multi-module** - Rejected because unnecessary complexity for Phase I scope (5 files max)
2. **Package distribution** - Rejected because Phase I is local console application, not published library
3. **Monorepo with separate subprojects** - Rejected because Phase I is single feature, no separate subprojects required

---

### 7. Performance Goals: <200ms Operations, <1s Display

**Decision**: Support up to 100 tasks, operations complete within performance budgets

**Rationale**:
- Success criteria SC-005 sets scope at 100 tasks
- O(1) add/delete operations complete in <200ms easily (Python list operations)
- O(n) display operations complete in <1 second for n=100 (100 iterations is trivial)
- No I/O delays (all in-memory operations)
- Performance budgets are conservative, allowing margin for future growth

**Alternatives Considered**:
1. **<50ms operations** - Rejected as premature optimization, current budgets are sufficient for user experience
2. **<10s display** - Rejected as too slow, violates user experience principle (II. User Experience Excellence)
3. **Unbounded performance** - Rejected because measurable goals ensure quality (constitution principle III. Correctness and Quality)

---

### 8. Constraints: PEP 8, 80-Character Width

**Decision**: PEP 8 code style, console output formatted for 80-character width

**Rationale**:
- PEP 8 is Python community standard for code readability
- Enforces clean, maintainable code (constitution principle IV. Maintainable Architecture)
- 80-character width is traditional terminal width, ensures readability
- Aligns with user experience excellence principle (clear, consistent output)
- Python standard library tools (ruff, black) support PEP 8

**Alternatives Considered**:
1. **120-character width** - Rejected because 80 is more conservative and works on all terminals
2. **No style enforcement** - Rejected because PEP 8 is mandated by constitution principle IV
3. **Dynamic width detection** - Rejected as unnecessary complexity for Phase I scope, 80 is reasonable default

---

### 9. Scale/Scope: Single-User, Ephemeral Session

**Decision**: Single user per session, data lost on application exit

**Rationale**:
- Specification explicitly requires in-memory only (FR-025)
- No persistence requirement for Phase I (assumptions section in spec.md)
- Simplifies implementation and testing
- Aligns with incremental delivery principle (Phase I is MVP/prototype)
- No authentication required (constitution principle VII. Security and Reliability - not applicable to Phase I)

**Alternatives Considered**:
1. **Multi-user support** - Rejected because specification assumes single user, would require concurrency control
2. **Persistence across sessions** - Rejected because specification explicitly requires in-memory only (FR-025)
3. **Session management** - Rejected as unnecessary complexity for Phase I scope

---

## Summary

All Technical Context items resolved with clear decisions and rationale. No NEEDS CLARIFICATION markers remain. Technology choices are aligned with:

- Constitution principles (I-VI applicable to Phase I)
- Phase I-specific standards from constitution
- Feature specification requirements
- Success criteria from spec.md
- Clean code and maintainability best practices

**All decisions are conservative, well-justified, and appropriate for Phase I MVP scope.**

---

## Constitution Compliance Post-Research

Re-evaluating Constitution Check after research:

**VI. Technology Constraint Discipline**: ✅ PASS
- Python 3.13+ selected (mandated)
- UV environment (mandated)
- No external databases or frameworks (confirmed - standard library only)
- No persistence beyond in-memory (confirmed)

**IV. Maintainable Architecture**: ✅ PASS
- Clean, modular code following PEP 8 (confirmed)
- Separation of concerns (Task, TaskManager, utils, main) (confirmed)
- Self-documenting code (confirmed - meaningful names)

**II. User Experience Excellence**: ✅ PASS
- Clear, consistent output (80-character width, formatted strings)
- PEP 8 ensures readability

**All constitutional checks remain passed.**
