---
name: Source Coding Practices
description: Use for work under src/. Covers code quality, implementation style, and change discipline for the reference TypeScript runtime.
applyTo: "src/**"
---

# Source Coding Practices

Apply these rules when editing files under `src/`.

This file is adapted for the reference runtime selected in Phase 5.

## Most Important Rules

- Prefer simple, explicit code over clever abstractions.
- Keep changes tightly scoped to the requested behavior.
- Fix root causes instead of layering symptom patches.
- Match existing project patterns, naming, and structure.
- Avoid unnecessary dependencies, configuration, or framework complexity.
- Do not mix unrelated responsibilities into one file or module.

## Commands

- Build: `pnpm run build` (fallback: `npm run build`)
- Test: `pnpm run test` (fallback: `npm run test`)
- Lint: `pnpm run lint` (fallback: `npm run lint`)
- Format: `pnpm run format` (fallback: `npm run format`)
- Type-check: `pnpm run typecheck` (fallback: `npm run typecheck`)

## Project structure

- Runtime: Node.js 22+ with TypeScript as the reference implementation stack.
- Primary structure:
  - `src/workflow/` for phase and artifact orchestration logic.
  - `src/contracts/` for cross-agent workflow contracts and invariants.
  - `src/adapters/` for assistant-specific integrations.
  - `src/review/` for review dispatch and findings handling logic.
- Naming: prefer `kebab-case` for filenames and clear module-level responsibilities.
- Boundaries: core contracts stay runtime-agnostic; adapter modules translate host-specific behavior.

## Code style

- Enable TypeScript strict mode and avoid `any` unless there is a documented boundary reason.
- Prefer small pure functions for orchestration decisions and explicit return types for exported symbols.
- Keep host/tool side effects in adapter modules and pass normalized data into core workflow modules.

Canonical pattern:

```ts
export function resolveNextPhase(roadmap: string[]): string | undefined {
  return roadmap.find((phase) => phase !== "done");
}
```

## Testing

- Framework: Vitest.
- Locations:
  - `tests/unit/` for pure workflow logic and rule evaluation.
  - `tests/integration/` for adapter and validation-layer interactions.
  - `tests/e2e/` for end-to-end initialization flows and resumability checks.
- Single test run: `pnpm vitest tests/unit/<file>.test.ts -t "<case>"`.
- Coverage expectation: prioritize phase-gate logic, plan-state transitions, and adapter conformance paths before broad line-coverage targets.

## Git workflow

- Branch naming: `feature/<topic>`, `fix/<topic>`, `docs/<topic>`.
- Commit style: imperative summary with scoped intent, for example `docs: tighten phase gate acceptance references`.
- Merge expectation: no unresolved critical or important review findings; required validation commands must pass.

## Quality rules

- Write code that is easy to read, review, and verify.
- Prefer maintainability over micro-optimizations.
- Add or update tests with behavior changes unless explicitly told not to.
- Call out edge cases, compatibility risks, and verification gaps in the final response.
- Do not claim success without verification evidence; if verification cannot run, state what was not run, why, and the residual risk.
