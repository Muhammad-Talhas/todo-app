---
name: "dead-code-endpoint-detection-skill"
description: "Identify API endpoints never called and frontend components never rendered. Suggest safe cleanup while preserving active functionality."
version: "1.0.0"
---

# Dead Code & Endpoint Detection Skill

## When to Use This Skill

- Codebase has accumulated unused components or routes
- Refactoring or optimizing the stack
- Preparing for production release
- Cleaning technical debt
- Debugging unexplained dead paths

## Core Responsibility

Detect **dead code and unused endpoints** across frontend and backend, ensuring that only truly unused elements are removed while preserving functional features.

## Procedure

1. **Enumerate Backend Endpoints**
   - Extract all FastAPI routes:
     - Path, method, tags
     - Associated services
   - Gather usage data:
     - Logs (requests made)
     - Test coverage
     - Instrumentation / telemetry

2. **Detect Unused Backend Endpoints**
   - Compare routes to:
     - Active API calls (from frontend, other services, or logs)
     - Test coverage
   - Flag:
     - Routes never called in production, staging, or tests
     - Orphaned service functions backing routes

3. **Enumerate Frontend Components**
   - Scan React components and pages:
     - JSX files
     - Hooks and stateful components
   - Gather usage data:
     - Render traces
     - Route mapping
     - Test coverage

4. **Detect Unused Frontend Components**
   - Flag components:
     - Never rendered anywhere
     - Only used in deprecated routes
     - Tests exist but component is unmounted or unreferenced

5. **Cross-Layer Validation**
   - Ensure endpoints flagged as unused are not:
     - Called by any component
     - Referenced in tests, cron jobs, or admin scripts
   - Ensure components flagged as unused are not:
     - Rendering API calls
     - Used in conditional features or feature flags

6. **Assess Safe Cleanup**
   - Recommend removal only if:
     - No runtime references
     - No active tests depend on it
     - Optional: flag for deprecation instead of immediate deletion

7. **Provide Cleanup Guidance**
   - Suggest deprecation annotations (`@deprecated`, comments)
   - Suggest staging cleanup before full removal
   - Recommend updating documentation/specs

## Output Format

### Backend Endpoint Dead Code

| Route | Method | Service Function | Used? | Notes |
|-------|--------|-----------------|-------|-------|
| `/tasks/legacy` | GET | get_legacy_tasks | ❌ | No calls in production or tests |

### Frontend Component Dead Code

| Component | Path | Rendered? | Notes |
|-----------|------|-----------|-------|
| `LegacyTaskList` | components/tasks/LegacyTaskList.tsx | ❌ | Not used in any route or test |

### Detected Issues

- API routes never called:
  - `/tasks/legacy`
  - `/analytics/old-summary`
- Frontend components never rendered:
  - `LegacyTaskList`
  - `OldDashboardWidget`

### Recommended Actions

1. Mark unused routes/components as deprecated
2. Remove them after one release cycle
3. Update tests and documentation to reflect removals
4. Monitor logs to confirm no usage

## Quality Criteria

- No removal without confirming zero references
- Safe cleanup process recommended (deprecate → remove)
- Cross-layer validation ensures no hidden dependencies
- Detect both test-covered and production-unused code
- Reports are actionable and prioritized by risk/impact

## Example

**Input**:
"Check for dead endpoints and components in the Task Management module."

**Output**:
- **Backend**:
  - `/tasks/legacy` → never called
  - `/tasks/old-summary` → only exists in test stubs
- **Frontend**:
  - `LegacyTaskList` → not imported anywhere
  - `OldTaskChart` → only in deprecated route
- **Recommended Fixes**:
  1. Annotate all deprecated items
  2. Remove in next sprint
  3. Update API documentation and specs