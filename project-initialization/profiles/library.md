# Profile: Library / Utility

Use for reusable packages, libraries, CLIs, and utilities without a primary user-facing product surface.

## Activation triggers

- Project type = "library" or "utility"

## Artifact defaults by phase

### Phase 1 — Intent

| Artifact | Default mode |
| --- | --- |
| project-brief | interview |
| business-case | skipped |

### Phase 2 — Specification

| Artifact | Default mode |
| --- | --- |
| prd | interview — focus on API/interface contract, not user journeys |
| requirements-catalog | skipped |
| journeys | skipped |
| acceptance-catalog | skipped |

### Phase 3 — Design

| Artifact | Default mode |
| --- | --- |
| solution-design | interview |
| adr | interview |
| c4 | skipped |

### Phase 4 — Govern & Operate

| Artifact | Default mode | Override rule |
| --- | --- | --- |
| ai-use-policy | skipped | activate if AI involvement = core |
| test-strategy | interview | always active |
| security-baseline | skipped | activate if regulatory posture is not none |
| delivery-plan | skipped | activate if team shape = multi-team |

### Phase 5 — Adapt

| Artifact | Default mode |
| --- | --- |
| language-adaptation | interview |
| repo-sync | extract |
