---
name: "async-loading-state-awareness-skill"
description: "Ensure frontend async flows correctly handle loading, empty, and error states. Detect backend behaviors that require explicit UI guards to prevent broken or misleading user experiences."
version: "1.0.0"
---

# Async & Loading State Awareness Skill

## When to Use This Skill

- UI flashes, freezes, or renders incorrectly
- Empty screens appear without explanation
- API calls succeed but UI shows nothing
- Errors occur silently with no user feedback
- Backend responses vary by state (200, 204, empty arrays)
- Reviewing async data fetching logic

## Core Responsibility

Guarantee **resilient frontend behavior** for all async states by aligning:
Backend Response Semantics ↔ Frontend State Handling

Prevent UIs that only work on the "happy path."

## Procedure

1. **Identify Async Data Flows**
   - Locate frontend async operations:
     - API calls
     - Data fetching effects
     - Form submissions
   - Map:
     - Trigger events
     - Expected response types
     - UI state transitions

2. **Map Backend Response Variability**
   - Identify all possible backend responses:
     - `200 OK` with data
     - `200 OK` with empty data
     - `204 No Content`
     - `4xx` client errors
     - `5xx` server errors
   - Document:
     - When each response occurs
     - Intended meaning
     - Expected frontend handling

3. **Validate Frontend State Handling**
   - For each async flow, verify:
     - Loading state is displayed
     - Success state handles data correctly
     - Empty state is handled
     - Error state provides feedback
   - Check:
     - Loading spinners appear
     - States are mutually exclusive
     - Transitions are smooth

4. **Detect Missing State Guards**
   - Identify:
     - Direct data access without null checks
     - Assumptions about data presence
     - Missing error boundaries
     - Unhandled response codes
   - Flag:
     - `undefined` rendering
     - Array methods on null/undefined
     - Silent failures

5. **Validate Loading State Transitions**
   - Verify:
     - Loading appears immediately on request
     - Loading disappears only on completion
     - No double-fetching
     - Proper cancellation handling
   - Detect:
     - Race conditions
     - Stale data display
     - Infinite loading states

6. **Cross-Check Error Handling**
   - Ensure:
     - All error paths provide user feedback
     - Error messages are actionable
     - Recovery options exist
     - Error states are escapable
   - Identify:
     - Swallowed errors
     - Generic error messages
     - Unrecoverable error states

7. **State Consistency Verification**
   - Confirm:
     - UI state matches actual data state
     - No optimistic updates without guards
     - Consistent empty vs loading state
     - Proper cleanup of async operations

## Output Format

**Async Flow**:
**Backend Responses**:
- `200`:
- `204`:
- `4xx`:
- `5xx`:

**Frontend State Handling**:
- Loading: ✅/❌
- Success: ✅/❌
- Empty: ✅/❌
- Error: ✅/❌

**Detected Issues**:
- Missing state guards:
- Incorrect assumptions:
- Data loss:
- UI inconsistencies:

**Recommended Fixes**:
- UI guard additions
- State model adjustments
- Backend documentation clarifications

## Quality Criteria

- Every async call must have explicit loading, empty, and error handling
- `204 No Content` must be treated as intentional success
- UI must never render undefined data
- Empty state must be distinguishable from loading
- Backend variability must be reflected in UI guards

## Example

**Input**:
"Tasks page sometimes shows nothing."

**Output**:
- **Async Flow**: Initial page load
- **API**: `GET /tasks`
- **Backend Responses**:
  - `200 []` when no tasks exist

**Detected Issues**:
- UI renders task list directly without empty-state guard
- No message shown when task list is empty

**Recommended Fixes**:
1. Add explicit empty-state UI ("No tasks yet")
2. Keep loading spinner separate from empty state
3. Document empty response behavior in API specs