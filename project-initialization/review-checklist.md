# Project Initialization Review Checklist

Read this file before running any review pass. This is the rubric for the `init-reviewer` agent and for end-of-phase self-review.

## Standards review (run on every artifact produced)

- Frontmatter is present and complete: `title`, `status`, `record_class`, `audience`, `owner`, `capability` are all populated. No field is left as a placeholder string.
- `status` is one of: `draft`, `proposed`, `accepted`, `active`, `superseded`, `archived`.
- `record_class` is one of: `canonical`, `supporting`, `historical`.
- `audience` contains at least one of: `internal`, `manager`, `client`, `end_user`, `auditor`.
- All internal links (`[text](path)`) resolve to existing files.
- No `[TBD: ...]` markers remain in required sections. Optional sections may carry `[TBD: ...]` only if labeled as optional.
- No implementation code, version pins, or feature stubs appear in documentation-only artifacts.
- No content from a later phase has leaked into an earlier-phase artifact (e.g., no stack choices in the project brief).

## Coherence review (run across all artifacts produced in the phase)

- Project name is identical across all artifacts produced so far.
- Target users described in the PRD match the users named in the project brief.
- Deployment target is consistent across PRD, solution design, and any ADRs.
- Tech stack choices in the solution design are covered by accepted ADRs.
- The plan file's `Project Facts` section reflects what was confirmed this phase.
- `README.md` and `AGENTS.md` still accurately describe the repository state. If not, note as `important` so the Adapt phase can fix them.
- Source-of-truth ownership in `docs/00-source-of-truth.md` covers all new canonical docs produced.

## Final review only (Phase 6)

- All produced docs are reachable from `docs/INDEX.md`.
- `README.md` project description matches the brief's one-line summary.
- `AGENTS.md` directory inventory includes all directories added during Adapt.
- Tracked repository entry surfaces and tool-specific `/init` wrappers match the current initialization workflow.
- No slot-template placeholder text remains unfilled in any adapted file.
- All `src/AGENTS.md`, `bin/README.md`, `diagrams/README.md`, `examples/README.md` slot guidance reflects the chosen stack.

## Severity guide

- `critical` — artifact cannot serve its purpose: missing required section, factual contradiction with another canonical doc, broken link that blocks further work.
- `important` — quality problem that will cause downstream issues: vague unmeasurable requirement, ambiguous scope boundary, orphaned decision not captured in an ADR.
- `minor` — standards violation that does not block: missing optional frontmatter field, inconsistent heading level, formatting issue.
- `advisory` — concern about a user choice already recorded in `Concerns And Recommendations` in the plan. Do not duplicate.
