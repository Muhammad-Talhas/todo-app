---
name: "full-stack-context-switching-skill"
description: "Trace a feature end-to-end across frontend, backend, and database layers. Detect mismatches, outdated contracts, and unused implementations. Use when validating real-world full-stack features against specs."
version: "1.0.0"
---

# Full-Stack Context Switching Skill

## When to Use This Skill

- User asks to "trace a feature end-to-end"
- User reports bugs that may originate from frontend–backend mismatch
- User asks to verify if a feature matches its specification
- User is working with FastAPI + frontend (Next.js or similar)
- User mentions missing fields, broken APIs, or unexpected behavior

## Core Responsibility

Maintain **cross-layer coherence** by tracking a single feature through:
UI → API → Backend → Database → Specs

Ensure that **what is built matches what is specified**.

## Procedure

1. **Identify the Feature**
   - Extract the feature name or user flow
   - Locate its specification under `/specs/features/*`
   - Determine expected inputs, outputs, and behavior

2. **Trace the Frontend Layer**
   - Locate the UI component(s) using the feature
   - Identify:
     - API endpoint called
     - HTTP method
     - Payload structure
     - Expected response shape

3. **Trace the API Layer**
   - Verify the API route exists
   - Match:
     - Route path
     - HTTP method
     - Request schema
     - Response schema
   - Detect deprecated or unused endpoints

4. **Trace the Backend Logic**
   - Locate the FastAPI route handler
   - Follow execution into:
     - Service layer
     - Business logic
     - Validation logic
   - Ensure all required fields are handled

5. **Trace the Database Layer**
   - Identify the database table(s) involved
   - Verify:
     - Columns match request/response fields
     - Required fields are persisted
     - No unused or missing columns

6. **Cross-Layer Validation**
   - Compare all layers side-by-side
   - Detect:
     - Missing fields
     - Mismatched field names
     - Renamed or outdated fields
     - Unused APIs
     - UI fields with no backend support
     - Backend logic not exposed to UI

7. **Spec Alignment Check**
   - Validate implementation against `/specs/features/*`
   - Flag deviations:
     - Spec says feature exists but code does not
     - Code exists but spec is outdated or missing

## Output Format

**Feature Name**:
**Spec Reference**: `/specs/features/<feature-name>.md`

**End-to-End Trace**:
- **UI Component**: file path + role
- **API Call**: method + endpoint
- **FastAPI Route**: file path + function
- **Service Layer**: file path + function
- **Database Table**: table name + relevant columns

**Detected Issues**:
- Missing fields:
- Mismatched field names:
- Unused APIs:
- Broken contracts:
- Spec mismatches:

**Impact Assessment**:
- User-facing impact
- Data integrity risk
- Security or performance implications (if any)

**Recommended Fixes**:
- Concrete, layer-specific actions
- Ordered by priority (frontend → backend → DB → spec)

## Quality Criteria

- No assumptions: every claim must be traceable to code or specs
- Field names must match exactly (case-sensitive)
- Always reference real file paths
- Prefer detection over speculation
- Specs are treated as the source of truth unless explicitly outdated

## Example

**Input**:
"Trace the `Create Task` feature and check why `priority` is not saving."

**Output**:
- **Feature Name**: Create Task
- **Spec Reference**: `/specs/features/create-task.md`
- **UI Component**: `frontend/components/CreateTaskForm.tsx`
- **API Call**: `POST /api/tasks`
- **FastAPI Route**: `backend/routes/tasks.py::create_task`
- **Service Layer**: `backend/services/task_service.py::create_task`
- **Database Table**: `tasks (id, title, description, status)`

**Detected Issues**:
- `priority` field exists in UI but not in DB schema
- API request includes `priority` but backend ignores it
- Spec defines `priority` as required

**Recommended Fixes**:
1. Add `priority` column to `tasks` table
2. Update Pydantic schema to include `priority`
3. Persist `priority` field in service layer