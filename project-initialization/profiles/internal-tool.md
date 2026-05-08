# Profile: Internal Tool

Use for tooling built for internal teams, not external customers.

## Activation triggers

- Project type = "internal tool"

## Artifact defaults by phase

### Phase 1 — Intent

| Artifact | Default mode |
| --- | --- |
| project-brief | interview |
| business-case | skipped |

### Phase 2 — Specification

| Artifact | Default mode |
| --- | --- |
| prd | interview |
| requirements-catalog | skipped |
| journeys | interview |
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
| security-baseline | skipped | activate if regulatory posture = light or heavy |
| delivery-plan | interview | always active |

### Phase 5 — Adapt

| Artifact | Default mode |
| --- | --- |
| language-adaptation | interview |
| repo-sync | extract |
