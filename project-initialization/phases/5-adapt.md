# Phase 5: Adapt

## Purpose

Specialize the repository structure to match all canonical docs produced in phases 1-4.

## Artifact walk order

1. `language-adaptation`
2. `repo-sync`

For each, load `project-initialization/artifacts/<name>.md` and follow the mode assigned in the plan.

## Phase-specific guidance

- Read all accepted ADRs before running `language-adaptation`. ADRs are the source of truth for stack decisions. If an ADR contradicts something the user says in this phase, raise a concern.
- Do not add feature code, implementation stubs, or dependency version pins beyond what an accepted ADR explicitly requires. If unsure, err on the side of leaving a slot placeholder.
- `docs/09_user_documentation/` is deliberately not touched in this phase. It is produced post-initialization alongside features.
- After `language-adaptation` is complete, run `repo-sync` — it reads the brief and updates `README.md`, `AGENTS.md`, and slot READMEs to match the actual project.

## End-of-phase review

Dispatch `init-reviewer` with all adapted files and phase number 5. The review is especially important here: scope drift (feature code appearing in an initialization pass) is the most common failure.
