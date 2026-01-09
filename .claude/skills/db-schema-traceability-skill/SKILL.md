---
name: "db-schema-traceability-skill"
description: "Trace data fields end-to-end from database tables through ORM models and Pydantic schemas to UI props. Detect orphaned fields, missing persistence, and backend-only data never exposed to the UI."
version: "1.0.0"
---

# DB Schema Traceability Skill

## When to Use This Skill

- Data appears in UI but is not saved
- Database contains columns no one understands
- Backend models grow but UI never uses new fields
- Refactoring schemas or adding new fields
- Auditing data flow before release
- Debugging "why is this always null?"

## Core Responsibility

Maintain **full data lineage visibility** across:
Database ↔ ORM ↔ Pydantic ↔ Frontend UI

Ensure every field has a **clear purpose, owner, and destination**.

## Procedure

1. **Identify the Data Field**
   - Select specific field to trace
   - Locate:
     - Database table and column
     - ORM model field
     - Pydantic schema field
     - UI component prop

2. **Trace Database Schema**
   - Locate table definition:
     - Raw SQL schema
     - Migration files
     - Database introspection
   - Extract:
     - Column name
     - Data type
     - Constraints (NOT NULL, UNIQUE, etc.)
     - Default values

3. **Trace ORM Model**
   - Locate ORM model:
     - SQLAlchemy/SQLModel class
     - Field definition
     - Column mapping
   - Verify:
     - Column name matches DB
     - Type matches DB
     - Constraints preserved
     - No field aliases causing mismatches

4. **Trace Pydantic Schema**
   - Locate Pydantic models:
     - Request models
     - Response models
     - Validation schemas
   - Verify:
     - Field exists and is accessible
     - Type matches ORM
     - Required vs optional status matches intent
     - Field name matches unless aliased

5. **Trace UI Usage**
   - Locate UI components using the field:
     - Prop definitions
     - Data access patterns
     - Display logic
   - Verify:
     - Field is accessed correctly
     - Null/undefined handling exists
     - Field name matches Pydantic output

6. **Validate End-to-End Chain**
   - Confirm data flows:
     - DB → ORM → Pydantic → UI
     - All transformations are intentional
     - No missing links in chain
     - No broken assumptions

7. **Detect Field Issues**
   - **Orphaned**: DB column exists but no UI usage
   - **Missing Link**: Gap in chain (e.g., DB → ORM → UI, skipping Pydantic)
   - **One-Way**: Field flows in only one direction
   - **Type Mismatch**: Type changes unexpectedly between layers
   - **Null Safety**: Field can be null but UI doesn't handle it

## Output Format

**Field Name**: `<field>`
**Table**: `<table_name>`

**Trace Chain**:
- **Database**: `column_name (type, constraints)`
- **ORM Model**: `model.field (type, mapping)`
- **Pydantic Schema**: `schema.field (type, required)`
- **UI Component**: `component.prop (usage pattern)`

**Chain Status**: ✅ Complete / ❌ Broken

**Detected Issues**:
- Orphaned fields:
- Missing links:
- Type mismatches:
- Null safety gaps:
- One-way flows:

**Impact Assessment**:
- Data integrity risk
- Confusing or misleading UI
- Long-term schema decay

### Recommended Fixes

- Remove unused DB columns
- Add missing ORM or Pydantic fields
- Persist UI-critical data
- Explicitly mark backend-only fields as internal

## Quality Criteria

- Every DB column must have a consumer or be explicitly internal
- UI must not assume persistence without backing storage
- ORM and Pydantic models must be intentional subsets
- Broken field chains are treated as bugs
- Traceability must be provable, not assumed

## Example

**Input**:
"Why does task priority reset after refresh?"

**Output**:
- **DB**: `priority` column exists
- **ORM**: Field present
- **Pydantic**: Missing from response schema
- **UI**: Reads `priority`

**Detected Issue**:
- Backend never exposes `priority`, UI reads undefined

**Recommended Fixes**:
1. Add `priority` to Pydantic response model
2. Update API docs
3. Add UI guard until fixed