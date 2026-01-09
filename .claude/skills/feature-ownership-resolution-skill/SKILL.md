---
name: "feature-ownership-resolution-skill"
description: "Resolve clear ownership between features, frontend components, backend routes, and data models. Enforce feature-based reasoning instead of file-based navigation."
version: "1.0.0"
---

# Feature Ownership Resolution Skill

## When to Use This Skill

- User asks "which feature owns this code?"
- Refactoring or adding features causes confusion
- Files are organized by technical layers, not features
- Reviewing PRs or onboarding new contributors
- Tracing bugs across frontend and backend feels ambiguous

## Core Responsibility

Establish **unambiguous feature ownership** across:
Feature Specs ↔ UI Components ↔ API Routes ↔ Backend Logic ↔ Data Models

Shift reasoning from **where code lives** to **what feature it serves**.

## Procedure

1. **Identify the Feature Boundary**
   - Determine which feature the code belongs to
   - Locate feature specification:
     - `/specs/features/<feature-name>.md`
   - Extract:
     - Feature scope
     - Feature boundaries
     - Cross-feature dependencies

2. **Map UI Components to Features**
   - Identify components that belong to the feature:
     - React components
     - Pages
     - Shared components (if feature-specific)
   - Verify:
     - Component names reflect feature ownership
     - Props align with feature requirements
     - No cross-feature prop drilling without explicit contracts

3. **Map API Routes to Features**
   - Identify routes that belong to the feature:
     - FastAPI endpoints
     - Route prefixes
     - Request/response schemas
   - Verify:
     - Route paths align with feature scope
     - No cross-feature route access without explicit contracts

4. **Map Backend Logic to Features**
   - Identify service functions that belong to the feature:
     - Business logic functions
     - Validation logic
     - Domain models
   - Verify:
     - Logic is encapsulated within feature boundaries
     - No cross-feature logic coupling without explicit contracts

5. **Map Data Models to Features**
   - Identify database tables/models that belong to the feature:
     - ORM models
     - Migration files
     - Schema definitions
   - Verify:
     - Models align with feature scope
     - Relationships respect feature boundaries

6. **Cross-Feature Dependency Analysis**
   - Identify legitimate cross-feature dependencies
   - Verify:
     - Dependencies are documented
     - Explicit contracts exist
     - No circular dependencies
     - Proper abstraction layers

7. **Ownership Validation**
   - Confirm:
     - Every file has clear feature ownership
     - No orphaned code
     - Feature boundaries are respected
     - Refactoring impact is limited to owning feature

## Output Format

**Feature Name**:
**Spec Reference**: `/specs/features/<feature-name>.md`

**Owned Assets**:
- UI Components:
- API Routes:
- Backend Logic:
- Data Models:

**Cross-Feature Dependencies**:
- Depends on:
- Used by:

**Detected Issues**:
- Ambiguous ownership:
- Cross-feature violations:
- Orphaned code:

**Recommended Actions**:
1. Clarify ownership for ambiguous code
2. Or create a feature-specific variant for shared functionality

## Quality Criteria

- Every file has one clear feature owner
- Cross-feature dependencies are explicit and documented
- Feature boundaries are respected
- Refactoring impact is predictable and limited
- No code exists without feature ownership

## Example

**Input**:
"Which feature owns the user profile page?"

**Output**:
- **Feature Name**: User Profile Management
- **Spec Reference**: `/specs/features/user-profile.md`
- **Owned Assets**:
  - UI Components: `pages/profile.tsx`, `components/ProfileForm.tsx`
  - API Routes: `GET /api/profile`, `PUT /api/profile`
  - Backend Logic: `services/profile_service.py`
  - Data Models: `models/user.py` (profile fields)
- **Cross-Feature Dependencies**:
  - Depends on: Authentication
- **Recommended Actions**:
  - All profile-related code belongs to User Profile Management feature
  - Authentication dependency is explicit and documented