---
name: "test-coverage-mapping-skill"
description: "Map test coverage across frontend and backend features. Identify untested features, misaligned tests, and obsolete tests for unused APIs."
version: "1.0.0"
---

# Test Coverage Mapping Skill

## When to Use This Skill

- Preparing for release and verifying coverage
- Refactoring features or endpoints
- Frontend and backend tests exist but may be misaligned
- Determining which features are under-tested
- Removing obsolete or unused tests
- Auditing QA effectiveness

## Core Responsibility

Provide **feature-centric test visibility** across the stack, ensuring:
- Each feature has proper test coverage
- Tests reflect real behavior, not outdated assumptions
- No unused or redundant tests clutter the codebase

## Procedure

1. **Identify Feature Universe**
   - Enumerate features from:
     - `/specs/features/*`
   - Record associated API endpoints, UI components, and database interactions

2. **Map Existing Backend Tests**
   - Identify tests:
     - Unit tests (services, models)
     - Integration tests (API endpoints, database interactions)
   - Map tests to features:
     - Which endpoints or business logic are exercised
   - Detect gaps:
     - Features with no backend tests
     - Features partially covered

3. **Map Existing Frontend Tests**
   - Identify tests:
     - Component/unit tests
     - Integration/UI tests
   - Map tests to features:
     - Components tested vs features implemented
   - Detect gaps:
     - Features rendered but untested
     - Features tested but API behavior differs

4. **Cross-Layer Alignment**
   - Compare:
     - Backend test coverage → API behavior
     - Frontend test coverage → component behavior and state
   - Detect:
     - Misalignment (frontend assumes backend behavior not implemented)
     - Tests that pass but no longer reflect real endpoints

5. **Obsolete Test Detection**
   - Identify tests for endpoints, components, or features no longer used
   - Flag tests that always pass trivially
   - Recommend removal or update

6. **Coverage Gaps & Risk Assessment**
   - For each feature, determine:
     - Fully tested
     - Partially tested
     - Untested
   - Assess impact on:
     - Production stability
     - User experience
     - Regression risk

## Output Format

**Feature List**:
- Feature Name
- Spec Reference

### Feature Coverage Map

| Feature | Backend Tests | Frontend Tests | Status | Notes |
|---------|---------------|----------------|--------|-------|
| Task Management | 80% endpoints tested | 60% components tested | Partial | Missing tests for `TaskFilterPanel` |
| Analytics | 0% | 100% | Partial | Backend API not implemented |

### Detected Issues

- Features lacking tests
- Frontend tests misaligned with backend
- Tests for unused APIs or components
- Partial coverage risks

### Recommended Actions

- Add missing backend or frontend tests
- Update tests to reflect current API and UI
- Remove obsolete tests
- Prioritize coverage for critical features

## Quality Criteria

- Every feature must have at least basic test coverage
- Tests must align with current implementation
- No tests for non-existent features
- Coverage metrics must be feature-focused, not code-focused
- Test alignment must be verified across layers

## Example

**Input**:
"Check test coverage for user authentication."

**Output**:
- **Feature**: User Authentication
- **Spec**: `/specs/features/auth.md`

**Coverage Map**:
| Feature | Backend Tests | Frontend Tests | Status | Notes |
|---------|---------------|----------------|--------|-------|
| Login | 90% | 70% | Partial | Missing edge cases in UI |
| Logout | 100% | 0% | Partial | No frontend tests |

**Recommended Actions**:
1. Add frontend tests for logout flow
2. Add invalid credentials test to backend
3. Update tests to match current API contracts