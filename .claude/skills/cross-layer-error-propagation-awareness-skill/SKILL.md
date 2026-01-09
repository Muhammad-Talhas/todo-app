---
name: "cross-layer-error-propagation-awareness-skill"
description: "Ensure backend errors are explicit, structured, and meaningful, and that frontend correctly surfaces and reacts to them. Prevent silent failures across API boundaries."
version: "1.0.0"
---

# Cross-Layer Error Propagation Awareness Skill

## When to Use This Skill

- Errors appear in logs but not in the UI
- UI fails silently without feedback
- Backend returns generic or empty error responses
- Frontend assumes success on failure
- Debugging "nothing happens" issues
- Reviewing error-handling patterns

## Core Responsibility

Guarantee **errors travel intact and intentionally** across:
Backend → API → Frontend → User

Prevent failures from being swallowed or obscured at any boundary.

## Procedure

1. **Identify Error Sources**
   - Locate backend error generation:
     - Exception handling
     - Validation failures
     - Database errors
     - External service failures
   - Map:
     - Error types
     - Error contexts
     - Expected error handling

2. **Validate Backend Error Structuring**
   - Verify:
     - Errors are caught and handled
     - Error responses are structured
     - Appropriate HTTP status codes
     - Error details are meaningful
   - Check:
     - No raw exception messages exposed
     - Error codes are consistent
     - User-friendly messages provided

3. **Validate API Error Contract**
   - Confirm:
     - Error responses match documented spec
     - Error schema is consistent
     - Status codes align with error types
     - Error details are properly serialized
   - Detect:
     - Undocumented error responses
     - Inconsistent error shapes

4. **Validate Frontend Error Handling**
   - Verify:
     - Non-2xx responses are handled
     - Error responses are parsed correctly
     - UI provides feedback to user
     - Error states are escapable
   - Check:
     - Error boundaries exist
     - User feedback is actionable
     - No optimistic updates after errors

5. **Detect Silent Failure Patterns**
   - Identify:
     - Errors that don't reach UI
     - Success assumptions on failure
     - Swallowed exceptions
     - Missing error handlers
   - Flag:
     - `.catch()` without action
     - Missing error states
     - Unhandled promise rejections

6. **Cross-Layer Error Flow Verification**
   - Ensure:
     - Backend error → API response → Frontend error state
     - Error context is preserved
     - User receives meaningful feedback
     - Error handling doesn't create new issues

7. **Error Recovery Validation**
   - Confirm:
     - Errors can be recovered from
     - UI returns to valid state
     - User can retry or correct
     - Error state doesn't persist

## Output Format

**Error Flow**:
**Backend Error Source**:
**API Contract**: `/specs/api/error-responses.md`

**Error Propagation Chain**:
- **Backend**: Error type and structure
- **API**: HTTP code and response shape
- **Frontend**: Error handling and UI feedback

**Chain Status**: ✅ Complete / ❌ Broken

**Detected Issues**:
- Silent failures:
- Missing error handlers:
- Generic error messages:
- Unhandled error types:
- Inconsistent error shapes:

**Impact Assessment**:
- User experience degradation
- Debugging difficulty
- Hidden system issues

**Recommended Fixes**:
- Backend error structuring
- API error contract updates
- Frontend error handling improvements

## Quality Criteria

- Every error must reach the user in some form
- Error messages must be actionable
- No raw exception details exposed to frontend
- Error handling must be explicit, not implicit
- Recovery paths must exist for all errors

## Example

**Input**:
"Form submission fails but no error shown."

**Output**:
- **Error Flow**: Form submit → API → Error response
- **Backend**: Validation error with field details
- **Frontend**: Ignores non-2xx responses

**Detected Issues**:
- Backend returns validation errors
- Frontend only handles success case

**Recommended Fixes**:
1. Return `400 Bad Request` with validation error details
2. Document error response in API specs
3. Update frontend to show inline error message