---
name: "pydantic-typescript-schema-parity-skill"
description: "Ensure Pydantic models are mirrored exactly in TypeScript interfaces or types. Detect mismatches in required fields, enums, nested objects, and serialization that cause runtime undefined errors."
version: "1.0.0"
---

# Pydantic ↔ TypeScript Schema Parity Skill

## When to Use This Skill

- User reports `undefined` or `null` values in frontend
- Backend responses serialize but frontend breaks
- TypeScript compiles but runtime data is missing
- Pydantic models were recently changed
- User asks to validate API contracts
- Enum or nested object issues appear across layers

## Core Responsibility

Enforce **strict schema parity** between:
FastAPI (Pydantic) ↔ Frontend (TypeScript)

Guarantee that **what the backend sends is exactly what the frontend expects**.

## Procedure

1. **Identify the Data Contract**
   - Determine the API endpoint involved
   - Identify:
     - Request model
     - Response model
   - Locate Pydantic model file(s)

2. **Inspect Pydantic Models**
   - Extract:
     - Field names
     - Types
     - Required vs optional (`Optional`, default values)
     - Enums and allowed values
     - Nested models
   - Note:
     - Field aliases
     - `exclude_unset`, `orm_mode`, `model_config`
     - Serialization behavior

3. **Inspect TypeScript Schemas**
   - Locate:
     - Interfaces
     - Types
     - Zod / Yup / other validators (if present)
   - Extract:
     - Required vs optional fields
     - Union types for enums
     - Nested object definitions
   - Verify nullability vs undefined handling

4. **Field-by-Field Parity Check**
   For every field:
   - Name matches exactly
   - Required/optional status matches
   - Type compatibility is preserved
   - Default values do not create false optionality
   - Alias handling is reflected on frontend

5. **Enum Parity Validation**
   - Compare:
     - Pydantic `Enum` values
     - TypeScript union or enum values
   - Detect:
     - Missing enum values
     - Case mismatches
     - Numeric vs string enum drift

6. **Nested Object Shape Validation**
   - Recursively validate nested models
   - Detect:
     - Flattened objects on frontend
     - Missing nested fields
     - Incorrect array vs object assumptions

7. **Serialization & Runtime Safety Check**
   - Validate:
     - Fields excluded during serialization
     - Optional fields accessed without guards
     - Mismatch between compile-time safety and runtime data
   - Flag:
     - Guaranteed runtime `undefined`
     - Silent data loss

## Output Format

**API Endpoint**:
**Pydantic Model(s)**: file path(s)
**TypeScript Schema(s)**: file path(s)

**Schema Comparison**:

- **Field Name**:
  - Backend: type / required?
  - Frontend: type / required?
  - Status: ✅ Match / ❌ Mismatch

**Enum Comparison**:
- Backend values:
- Frontend values:
- Status:

**Nested Objects**:
- Model path:
- Issues detected:

**Detected Issues**:
- Required field mismatches:
- Optionality drift:
- Enum mismatches:
- Nested shape errors:
- Serialization risks:

**Impact Assessment**:
- Runtime crash risk
- Data integrity risk
- UI inconsistency risk

**Recommended Fixes**:
- Backend fixes (Pydantic)
- Frontend fixes (TypeScript)
- Contract enforcement suggestions

## Quality Criteria

- No implicit assumptions about optionality
- Field names must match serialized output
- Enums must be exhaustive and exact
- Nested models must be fully mirrored
- Prefer runtime validation when possible
- Zero tolerance for silent mismatches

## Example

**Input**:
"Frontend crashes when rendering task status."

**Output**:
- **API Endpoint**: `GET /tasks`
- **Pydantic Model**: `models/task.py::TaskRead`
- **TypeScript Schema**: `types/task.ts::Task`

**Detected Issues**:
- Backend enum: `["pending", "completed", "archived"]`
- Frontend union: `"pending" | "completed"`
- `archived` not handled → runtime crash

**Recommended Fixes**:
1. Add `"archived"` to TypeScript union
2. Update UI switch-case to handle new value
3. Add runtime validation for API response