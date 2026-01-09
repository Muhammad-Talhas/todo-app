---
name: "docker-compose-intelligence-skill"
description: "Analyze docker-compose services, ports, and networking. Ensure containerized frontend connects to containerized backend, preventing localhost misconfigurations and port conflicts."
version: "1.0.0"
---

# Docker & Compose Intelligence Skill

## When to Use This Skill

- Dockerized environment misbehaves (frontend cannot reach backend)
- Ports or services conflict across containers
- Preparing multi-service deployments (dev, staging, prod)
- Ensuring container networking follows best practices
- Reviewing docker-compose setups

## Core Responsibility

Ensure **containerized services communicate reliably**, mapping ports, environment variables, and networking correctly between frontend and backend.

Prevent accidental reliance on host `localhost` instead of container DNS.

## Procedure

1. **Analyze Docker Compose Structure**
   - Parse `docker-compose.yml`:
     - Services defined
     - Port mappings (external:internal)
     - Network configurations
     - Environment variables
   - Identify:
     - Frontend service
     - Backend service
     - Database or other dependencies
     - Shared networks

2. **Validate Container Networking**
   - Verify:
     - Services are on same network or properly linked
     - Internal DNS names match service names
     - No localhost references inside containers
     - Proper network isolation
   - Check:
     - Network definitions
     - Service dependencies
     - Inter-container communication paths

3. **Validate Port Mappings**
   - Confirm:
     - External ports don't conflict
     - Internal ports match service expectations
     - Port ranges are appropriate for environment
     - No overlapping port assignments
   - Verify:
     - Frontend exposed port matches user access
     - Backend exposed port matches frontend connection
     - Database ports not unnecessarily exposed

4. **Validate Environment Variables**
   - Check:
     - Backend URL in frontend container
     - Database connection strings
     - API endpoints for inter-service communication
   - Ensure:
     - Container-internal URLs use service names
     - Host-external URLs use localhost or IP
     - No hardcoded host IPs in container configs

5. **Cross-Service Communication Analysis**
   - Verify:
     - Frontend can reach backend via container DNS
     - Backend can reach database via container DNS
     - All service dependencies are satisfied
     - Health checks and readiness probes
   - Detect:
     - Circular dependencies
     - Missing service links
     - Incorrect protocol assumptions

6. **Environment-Specific Validation**
   - For dev/staging/prod environments:
     - Port conflicts avoided
     - Security considerations addressed
     - Resource allocations appropriate
     - Secrets management implemented

7. **Best Practices Compliance**
   - Verify adherence to:
     - Container networking best practices
     - Security guidelines
     - Resource allocation patterns
     - Health and readiness checks

## Output Format

**Compose File**: `docker-compose.yml`
**Services Analyzed**:
- Frontend: `<service-name>`
- Backend: `<service-name>`
- Database: `<service-name>`

**Network Analysis**:
- Networks defined:
- Services per network:
- Communication paths:

**Port Analysis**:
- External mappings:
- Internal mappings:
- Conflict status:

**Environment Variables**:
- Frontend API URL:
- Backend database connection:
- Cross-service URLs:

**Detected Issues**:
- Networking problems:
- Port conflicts:
- Environment misconfigurations:
- Best practice violations:

**Impact Assessment**:
- Connectivity risk
- Security concerns
- Performance implications

**Recommended Fixes**:
- Specific configuration changes
- Network reconfiguration
- Environment variable corrections

## Quality Criteria

- Services and ports explicitly defined
- Environment variables aligned across containers and dev environments
- Misconfigurations flagged with actionable recommendations

## Example

**Input**:
"Frontend cannot fetch data from backend in docker-compose environment."

**Output**:
- **Issue**: Frontend environment variable points to `http://localhost:8000`
- **Backend**: Exposed at `backend:8000` inside container network
- **Fix**: Change `NEXT_PUBLIC_API_URL` to `http://backend:8000`, connect both services to `frontend-backend-net`, verify port mapping