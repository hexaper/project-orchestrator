# src

Purpose: Source location for the TypeScript workflow engine and adapter modules.

Rules:

- Keep contracts and orchestration rules explicit and easy to review.
- Keep adapter behavior separated from runtime-agnostic workflow logic.
- Prefer narrow modules under the following folders:
  - `workflow/` for phase and artifact orchestration.
  - `contracts/` for shared workflow invariants.
  - `adapters/` for assistant-specific integrations.
  - `review/` for review dispatch and findings handling.
- Avoid feature stubs; add implementation files only when tied to accepted plans.
