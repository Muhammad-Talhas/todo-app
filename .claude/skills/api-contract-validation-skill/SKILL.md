---
name: "api-contract-validation-skill"
description: "Validate API contracts end-to-end. Ensure HTTP methods, request/response payloads, and error handling match documented specs. Detect silent failures caused by mismatched assumptions."
version: "1.0.0"
---

# API Contract Validation Skill

## When to Use This Skill

- API behaves differently than expected
- Frontend works in happy paths but fails silently
- Backend responses changed recently
- User reports inconsistent UI state after API calls
- Preparing for release or contract freeze
- Migrating or refactoring APIs

## Core Responsibility

Enforce **strict API contract correctness** between:
API Specs ↔ Backend Implementation ↔ Frontend Consumption

Prevent bugs caused by **assumed behavior instead of documented behavior**.

## Procedure

1. **Identify the API Contract**
   - Locate API definition in:
     - `/specs/api/rest-endpoints.md`
   - Identify:
     - Endpoint path
     - HTTP method
     - Request schema
     - Response schema(s)
     - Error responses

2. **Validate HTTP Method Alignment**
   - Compare:
     - Spec-defined method
     - FastAPI route decorator
     - Frontend request method
   - Flag:
     - POST vs PUT mismatches
     - Unsafe method misuse
     - Hidden method overrides

3. **Validate Request Payload**
   - Compare:
     - Documented request shape
     - Pydantic request model
     - Frontend payload construction
   - Detect:
     - Missing required fields
     - Extra undocumented fields
     - Incorrect nesting or types

4. **Validate Response Payload**
   - Compare:
     - Documented success response
     - Actual FastAPI response model
     - Frontend parsing logic
   - Detect:
     - Field name drift
     - Optionality mismatches
     - Shape changes (object vs array)
     - Missing response bodies

5. **Validate Error Contracts**
   - Extract documented error cases:
     - HTTP status codes
     - Error payload shapes
   - Verify backend:
     - Returns correct status codes
     - Returns documented error schemas
   - Verify frontend:
     - Handles non-2xx responses
     - Does not assume success

6. **Detect Silent Failures**
   - Identify patterns where:
     - Frontend assumes `200 OK`
     - Backend returns `204 No Content`
     - Backend returns `201 Created` but frontend expects body
     - Errors are swallowed without UI feedback
   - Flag any mismatch that results in:
     - No UI update
     - Incorrect optimistic state
     - Data loss

7. **Cross-Layer Contract Verification**
   - Ensure:
     - Every documented response is handled in UI
     - Every backend response is documented
     - No undocumented success paths exist

## Output Format

**Endpoint**:
**Spec Reference**: `/specs/api/rest-endpoints.md`

**Contract Summary**:
- Method:
- Request schema:
- Success responses:
- Error responses:

**Validation Results**:

- **HTTP Method**: ✅ Match / ❌ Mismatch
- **Request Payload**: ✅ Match / ❌ Mismatch
- **Response Payload**: ✅ Match / ❌ Mismatch
- **Error Handling**: ✅ Covered / ❌ Missing

**Silent Failure Risks**:
- Description:
- Trigger condition:
- User impact:

**Detected Issues**:
- Method mismatches:
- Payload mismatches:
- Unhandled errors:
- Undocumented responses:

**Recommended Fixes**:
- Backend changes
- Frontend changes
- Spec updates (if required)

## Quality Criteria

- Specs are the authoritative contract
- No frontend assumption without spec backing
- Every non-2xx response must be handled
- `204 No Content` must be explicitly expected
- All success paths must be explicitly documented
- Zero tolerance for silent failures

## Example

**Input**:
"Why does the UI not update after deleting a task?"

**Output**:
- **Endpoint**: `DELETE /tasks/{id}`
- **Spec**: Returns `204 No Content`
- **Frontend**: Expects JSON body with updated task list

**Detected Issues**:
- Frontend attempts to parse JSON from `204` response
- Error is swallowed, UI state not updated

**Recommended Fixes**:
1. Update frontend to treat `204` as success without body
2. Or update backend to return `200` with explicit payload
3. Document the chosen approach in specs