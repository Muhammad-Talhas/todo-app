---
name: "environment-variable-sync-skill"
description: "Ensure frontend and backend environment variables remain synchronized across local, Docker, and production environments. Detect port drift, mismatched API URLs, and broken CORS origins."
version: "1.0.0"
---

# Environment Variable Sync Skill

## When to Use This Skill

- User reports frontend cannot reach backend
- API works locally but fails in Docker or production
- User mentions CORS errors or network failures
- User asks to verify environment configuration
- Ports, URLs, or env variables were recently changed
- Multiple environments (local, docker, prod) are involved

## Core Responsibility

Maintain **configuration parity** between:
Frontend → Docker → Backend → Deployment Environment

Prevent failures caused by **env drift** rather than code bugs.

## Procedure

1. **Identify Active Environments**
   - Determine which environments exist:
     - Local (dev)
     - Docker / docker-compose
     - Production
   - Identify which one is currently failing

2. **Inspect Frontend Environment Variables**
   - Locate frontend env files:
     - `.env.local`
     - `.env.development`
     - `.env.production`
   - Validate:
     - `NEXT_PUBLIC_API_URL`
     - Protocol (`http` vs `https`)
     - Hostname
     - Port number

3. **Inspect Docker Configuration**
   - Review `docker-compose.yml`
   - Extract:
     - Backend service exposed ports
     - Internal vs external ports
     - Env variables injected into containers
   - Detect:
     - Incorrect port mappings
     - Hardcoded URLs
     - Missing env propagation

4. **Inspect Backend Server Configuration**
   - Locate FastAPI startup command
   - Verify:
     - `uvicorn` host and port
     - Environment-specific overrides
     - `.env` or settings module usage
   - Confirm backend is listening on the expected port

5. **Cross-Environment Comparison**
   - Compare:
     - `NEXT_PUBLIC_API_URL`
     - Docker exposed ports
     - Uvicorn listening port
   - Detect **port drift**:
     - Frontend calls port A
     - Docker exposes port B
     - Backend listens on port C

6. **CORS Validation**
   - Inspect FastAPI CORS middleware
   - Verify:
     - Allowed origins include frontend URL(s)
     - No missing protocol or port
     - Production and local origins are separated
   - Detect:
     - Missing origins
     - Wildcard misuse
     - Environment-specific CORS failures

7. **Environment Parity Check**
   - Ensure:
     - Local and production values are intentionally different
     - No dev URLs leak into production
     - No prod URLs hardcoded in local configs

## Output Format

**Environment Scope**:
- Local:
- Docker:
- Production:

**Frontend Config**:
- `NEXT_PUBLIC_API_URL`:
- Source file:

**Docker Config**:
- Service name:
- Exposed port(s):
- Internal port(s):

**Backend Config**:
- Uvicorn host:
- Uvicorn port:
- Env source:

**Detected Issues**:
- Port drift:
- URL mismatch:
- Missing env vars:
- Broken CORS origins:
- Environment leakage:

**Impact Assessment**:
- Frontend connectivity risk
- CORS failure likelihood
- Deployment stability risk

**Recommended Fixes**:
- Step-by-step corrective actions
- Explicit file and line-level guidance
- Environment-specific recommendations

## Quality Criteria

- Never assume defaults — always verify actual values
- Ports must align across all layers
- URLs must include correct protocol and port
- CORS origins must be explicit and environment-aware
- Recommendations must be minimal and reversible

## Example

**Input**:
"Frontend fails to call backend after moving to Docker."

**Output**:
- **Frontend Config**:
  - `NEXT_PUBLIC_API_URL=http://localhost:3001`
- **Docker Config**:
  - Backend exposed: `8000:8000`
- **Backend Config**:
  - Uvicorn running on `8000`

**Detected Issues**:
- Frontend calls port `3001`, backend exposed on `8000`
- CORS does not include `http://localhost:3000`

**Recommended Fixes**:
1. Update `NEXT_PUBLIC_API_URL` to `http://localhost:8000`
2. Add `http://localhost:3000` to FastAPI CORS allowed origins
3. Rebuild frontend Docker image to apply env changes