---
name: "environment-parity-enforcement-skill"
description: "Detect environment mismatches across local development, Docker, and production. Ensure .env files, ports, and service endpoints are consistent. Warn when .env.example is outdated."
version: "1.0.0"
---

# Environment Parity Enforcement Skill

## When to Use This Skill

- Bugs appear only in Docker or production but not locally
- Deployment fails due to missing or incorrect env variables
- Ports or service URLs differ between environments
- .env.example is stale or incomplete
- Preparing release or onboarding new developers

## Core Responsibility

Ensure **identical assumptions across all environments** by validating:
Local `.env` ↔ Docker Compose `.env` ↔ Production `.env` / environment variables

Prevent "it works on my machine" scenarios.

## Procedure

1. **Identify Environment Sources**
   - Local dev `.env` or `.env.local`
   - `docker-compose.yml` environment variables
   - Production environment variables or secrets
   - `.env.example` as reference

2. **Extract Environment Variables**
   - For each environment, extract:
     - API endpoints
     - Database URLs
     - Ports
     - Feature flags
     - Authentication keys (mask secrets in output)

3. **Compare Across Environments**
   - Detect:
     - Missing variables in any environment
     - Conflicting values (e.g., ports, URLs)
     - Variables present in `.env.example` but missing in actual env
     - Variables present in actual env but missing from `.env.example`

4. **Validate Critical Parity Rules**
   - Backend URL matches frontend expectation
   - Ports are consistent with docker-compose and host
   - Feature flags behave identically
   - Secrets are masked but present
   - Local dev mirrors production as closely as feasible

5. **Detect .env.example Drift**
   - Compare `.env.example` against actual required variables
   - Flag outdated keys:
     - Deprecated keys still present
     - Missing new keys required for current code

6. **Recommend Fixes**
   - Update `.env.example` to reflect all required variables
   - Align local and Docker variables with production values where possible
   - Warn if dev overrides could break Docker or production
   - Suggest documenting defaults and optional variables

## Output Format

**Environment Comparison Table**:

| Variable | Local Dev | Docker | Production | .env.example | Notes |
|----------|-----------|--------|------------|--------------|-------|
| NEXT_PUBLIC_API_URL | http://localhost:8000 | http://backend:8000 | http://api.prod | http://localhost:8000 | Mismatch detected in Docker & production |
| DATABASE_URL | postgres://dev | postgres://db | postgres://prod | postgres://dev | Matches local only |
| FEATURE_FLAG_X | true | true | false | true | Production differs |

**Detected Issues**:
- Backend URL mismatch between Docker and production
- DATABASE_URL not aligned across environments
- FEATURE_FLAG_X differs in production
- .env.example missing `NEW_FEATURE_KEY`

**Recommended Actions**:
1. Update `.env.example` to include `NEW_FEATURE_KEY` and remove deprecated keys
2. Align Docker backend URL with local and production expectations
3. Document any deliberate environment differences
4. Add preflight check to validate env parity before deployment

## Quality Criteria

- All critical variables must exist in every environment
- Values should be consistent unless intentional divergence is documented
- .env.example must represent the superset of required variables
- Misalignment warnings are actionable and prevent runtime errors
- Secrets are never printed in full; masked in reports

## Example

**Input**:
"Frontend fails to fetch API only in Docker."

**Output**:
- **Issue**: `NEXT_PUBLIC_API_URL` points to `localhost` in `.env.local`, but backend is `backend:8000` in Docker
- **.env.example**: Still lists `localhost`
- **Recommended Fixes**:
  1. Update `.env.example` to reflect containerized service names
  2. Add Docker-specific environment file with correct service URLs
  3. Document the difference between local and containerized environments