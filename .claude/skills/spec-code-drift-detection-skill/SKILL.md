---
name: "spec-code-drift-detection-skill"
description: "Detect drift between specifications and implementation across API, UI, and database layers. Flag undocumented implementations and unimplemented documented features."
version: "1.0.0"
---

# Spec ↔ Code Drift Detection Skill

## When to Use This Skill

- User asks to verify if the code matches the specs
- Features behave differently than documented
- Specs were updated recently
- New code was merged without spec updates
- User wants confidence in spec-driven development
- Preparing for review, audit, or handoff

## Core Responsibility

Ensure **specs and code remain in lockstep**.

Treat specifications as the **single source of truth** and identify any divergence across:
Specs ↔ API ↔ UI ↔ Database

## Procedure

1. **Identify Spec Sources**
   - Locate spec files:
     - `/specs/api/rest-endpoints.md`
     - `/specs/ui/components.md`
     - `/specs/database/schema.md`
   - Extract declared features, endpoints, components, and schemas

2. **Analyze API Specifications**
   - From `/specs/api/rest-endpoints.md`, extract:
     - Endpoint paths
     - HTTP methods
     - Request/response models
   - Scan FastAPI routes:
     - Registered paths
     - Methods
     - Schemas
   - Compare spec ↔ implementation

3. **Analyze UI Specifications**
   - From `/specs/ui/components.md`, extract:
     - Component names
     - Props
     - Intended behaviors
   - Scan React codebase:
     - Component files
     - Props usage
     - Render logic
   - Compare spec ↔ implementation

4. **Analyze Database Specifications**
   - From `/specs/database/schema.md`, extract:
     - Tables
     - Columns
     - Relationships
   - Inspect:
     - ORM models
     - Migrations
   - Compare spec ↔ implementation

5. **Drift Classification**
   For each layer, classify findings as:
   - **Implemented but Undocumented**
   - **Documented but Unimplemented**
   - **Partially Implemented**
   - **Fully Aligned**

6. **Cross-Layer Consistency Check**
   - Verify:
     - API endpoints map to UI usage
     - DB schemas support API contracts
     - No orphaned implementations

7. **Drift Severity Assessment**
   - Critical: Functionality missing from code but in spec
   - High: Security, performance, or core features affected
   - Medium: Minor feature gaps
   - Low: Documentation or cosmetic differences

## Output Format

**Spec Files Analyzed**:
- API: `/specs/api/rest-endpoints.md`
- UI: `/specs/ui/components.md`
- DB: `/specs/database/schema.md`

**API Layer Drift**:
- Spec-only endpoints:
- Code-only endpoints:
- Schema mismatches:

**UI Layer Drift**:
- Spec-only components:
- Code-only components:
- Prop differences:

**Database Layer Drift**:
- Spec-only tables/columns:
- Code-only tables/columns:
- Schema inconsistencies:

**Cross-Layer Issues**:
- Orphaned implementations:
- Missing API-UI connections:
- DB-API gaps:

**Drift Severity**:
- Critical:
- High:
- Medium:
- Low:

**Impact Assessment**:
- User-facing impact
- Compliance risk
- Technical debt

**Recommended Actions**:
- Update specs to match code (if intentional)
- Update code to match specs (if bug)
- Prioritized action list

## Quality Criteria

- Specs are the source of truth unless explicitly deprecated
- All drift must be classified as intentional or unintentional
- Severity assessment must consider user impact
- Recommendations must be actionable
- No false positives in drift detection

## Example

**Input**:
"Check if our user management feature matches the spec."

**Output**:
- **API Layer Drift**:
  - Spec-only: `DELETE /api/users/{id}` (not implemented)
  - Code-only: `PATCH /api/users/profile` (missing from spec)

- **Drift Severity**: High
- **Impact**: User deletion feature missing, profile update undocumented

**Recommended Actions**:
1. Implement `DELETE /api/users/{id}` endpoint
2. Document `PATCH /api/users/profile` in API spec
3. Add tests for new endpoint