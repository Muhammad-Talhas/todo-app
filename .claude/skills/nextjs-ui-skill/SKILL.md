---
name: "nextjs-ui-skill"
description: "Reason about Next.js UI architecture, rendering behavior, routing, and data-fetching to ensure correct, performant, and spec-aligned frontend implementation."
version: "1.0.0"
---

# Next.js UI Intelligence Skill

## When to Use This Skill

- Building or reviewing a Next.js frontend
- Debugging UI behavior that differs between dev and production
- Migrating between Pages Router and App Router
- Ensuring UI aligns with backend APIs and specs
- Optimizing rendering, data fetching, and user experience

## Core Responsibility

Understand and reason about **Next.js UI behavior end-to-end**, including routing, rendering mode, data fetching, state handling, and environment assumptions.

## Procedure

1. **Routing Awareness**
   - Identify whether project uses:
     - App Router (`app/`)
     - Pages Router (`pages/`)
   - Map routes to UI components and layouts
   - Detect unused or unreachable routes

2. **Rendering Mode Detection**
   - Determine per route/component:
     - Server Components
     - Client Components (`"use client"`)
     - Static rendering (SSG)
     - Server-side rendering (SSR)
     - Dynamic rendering
   - Warn when client-only logic exists in Server Components

3. **Data Fetching Reasoning**
   - Trace data flow:
     - `fetch()` (server vs client)
     - React Server Actions
     - API routes (`/api/*`)
   - Ensure caching, revalidation, and mutation behavior matches intent

4. **State & Side-Effect Handling**
   - Validate correct use of:
     - `useState`, `useEffect`
     - URL params and search params
     - Global state (context, Zustand, etc.)
   - Warn about hydration mismatches or unsafe side effects

5. **Async & UX Awareness**
   - Ensure usage of:
     - `loading.tsx`
     - `error.tsx`
     - Suspense boundaries
     - Empty states
   - Warn when backend responses require UI guards

6. **Environment & Runtime Awareness**
   - Validate usage of:
     - `NEXT_PUBLIC_*` env vars
     - Server-only envs
   - Detect mismatches between:
     - Local
     - Docker
     - Production (Vercel / Node)

7. **Spec & API Alignment**
   - Ensure UI:
     - Calls documented APIs
     - Handles non-200 responses
     - Matches request/response shapes
   - Detect assumptions like “always returns data”

8. **Performance & UX Checks**
   - Detect unnecessary client components
   - Warn about excessive re-renders
   - Identify blocking waterfalls

## Output Format

### Route Analysis
- Route: `/dashboard`
- Rendering: Server Component + Client widgets
- Data Source: `/api/stats`
- Issues:
  - Client-only hook used in Server Component
  - Missing loading state

### UI Risks Detected
- Hydration mismatch risk
- Silent failure on empty API response
- Hardcoded localhost API URL

### Recommendations
1. Move client logic behind `"use client"`
2. Add `loading.tsx` for async routes
3. Align API assumptions with backend behavior

## Quality Criteria

- Clear distinction between Server vs Client Components
- Rendering mode always explicitly reasoned
- UI never assumes backend success
- Environment-safe configuration
- UX guards for async behavior
- Feature-based reasoning, not file-based guessing

## Example

**Input**:
"Review the Next.js UI for the Tasks feature."

**Output**:
- Route `/tasks` is server-rendered
- TaskList is a Client Component
- API call assumes non-empty array
- Missing empty and error states
- Recommendation: add Suspense + guards
