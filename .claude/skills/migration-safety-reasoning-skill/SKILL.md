---
name: "migration-safety-reasoning-skill"
description: "Analyze database and schema migrations to detect breaking changes that invalidate API contracts or frontend assumptions. Recommend versioning or backward-compatible strategies."
version: "1.0.0"
---

# Migration Safety Reasoning Skill

## When to Use This Skill

- New DB migration is proposed
- Existing fields are renamed, removed, or retyped
- API responses change after deployment
- Frontend breaks after backend schema changes
- Preparing production migration rollout
- Reviewing schema PRs or release plans

## Core Responsibility

Ensure **schema evolution does not break consumers** by aligning:
Database Migrations ↔ ORM Models ↔ API Contracts ↔ Frontend Assumptions

Favor **backward compatibility** over convenience.

## Procedure

1. **Identify Migration Scope**
   - Locate migration files
   - Extract:
     - Added, removed, renamed columns
     - Type changes
     - Constraint changes
     - Default value changes

2. **Classify Change Types**
   For each change, classify as:
   - Additive (safe)
   - Deprecation (potentially safe)
   - Breaking (unsafe)
   - Data-destructive (high risk)

3. **API Contract Impact Analysis**
   - Map affected fields to:
     - Pydantic response schemas
     - API endpoints
   - Detect:
     - Fields removed from responses
     - Type changes altering serialized output
     - Nullability changes violating clients

4. **Frontend Assumption Validation**
   - Identify frontend usage of affected fields
   - Detect:
     - Required fields becoming optional or removed
     - Enum value changes
     - Shape changes (object → array)
   - Flag unguarded assumptions

5. **Backward Compatibility Assessment**
   - Determine if:
     - Old fields are still readable
     - Defaults preserve previous behavior
     - Clients can safely ignore new fields
   - Identify compatibility window requirements

6. **Versioning & Rollout Strategy**
   - Recommend:
     - Dual-write or dual-read strategies
     - Soft-deprecation with warnings
     - API versioning
     - Feature flags or phased rollout

7. **Risk Scoring**
   - Assign risk level:
     - Low
     - Medium
     - High
   - Base score on:
     - Number of consumers
     - Severity of breakage
     - Rollback difficulty

## Output Format

**Migration File(s)**:
**Affected Tables**:

### Change Summary
- Added:
- Removed:
- Renamed:
- Retyped:

### Breaking Change Analysis
- Field:
- Change:
- Affected API endpoints:
- Frontend dependencies:

### Compatibility Status
- Backward compatible: ✅ / ❌
- Safe rollout possible: ✅ / ❌

### Risk Assessment
- Risk Level:
- Failure Mode:
- Blast Radius:

### Recommended Actions
- Schema-level mitigations
- API-level compatibility fixes
- Frontend guard or fallback
- Versioning strategy (if required)

## Quality Criteria

- No destructive change without explicit mitigation
- API contracts must remain valid during migration
- Frontend assumptions must be respected or guarded
- Migration must be reversible if needed
- Risk assessment must be proportional to impact

## Example

**Input**:
"Changing user email from required to optional in migration."

**Output**:
- **Migration**: `2023_add_optional_email.py`
- **Change**: `email NOT NULL` → `email NULL`

**Breaking Change Analysis**:
- API contract assumes email is always present
- Frontend accesses `user.email` without null checks

**Risk Assessment**:
- Risk Level: High
- Failure Mode: Runtime errors in UI

**Recommended Actions**:
1. Add null guards in frontend before migration
2. Update Pydantic schema to make email optional
3. Update API documentation
4. Deploy in phases with monitoring