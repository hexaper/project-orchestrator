# Phase 6: Final Review

## Purpose

Validate that all produced artifacts are consistent, complete, and properly linked. Declare initialization complete or identify what must be fixed.

## Precheck

All phases 1-5 must be `done`. If any are not, stop and list the incomplete phases.

## Review steps

Run these in order using `init-reviewer` with the full artifact list:

### 1. Cross-doc coherence

- Project name is identical in: brief, PRD, solution design, README.
- Target users described in the PRD match the brief's user description.
- Deployment target is consistent across PRD, solution design, ADRs, and language adaptation.
- Tech stack choices in solution design are covered by accepted ADRs.

### 2. Entry-doc parity

- `README.md` project description matches the brief's one-line summary.
- `AGENTS.md` directory inventory includes all directories created or adapted during Phase 5.
- Tracked assistant command entrypoints are accurate.

### 3. Completeness check

- All active artifacts in the Artifact Roadmap are `done`.
- All produced docs are reachable from `docs/INDEX.md`.
- No `[TBD]` or `[NEEDS-REVIEW]` markers remain in any produced doc.

### 4. Standards pass

- All produced docs pass markdownlint.
- All produced docs pass the docs validator: `PYTHONPATH=tools/docs_validator/src python3 -m docs_validator.cli docs docs/_examples`

## Verdict

- **Pass**: All findings resolved or `advisory`. Mark Phase 6 `done`. Declare initialization complete. Suggest commit: `"docs: complete project initialization"`.
- **Concerns remain**: Leave Phase 6 `in-progress`. List what must be fixed before declaring complete. The user runs `/init` again after fixes.

## Output

Use the shared end-of-run output format from `project-initialization/contract.md`.
