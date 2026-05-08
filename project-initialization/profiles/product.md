# Profile: Product

Use for customer-facing or externally shipped products.

## Activation triggers

- Project type = "product"
- Or: project type = other + regulatory posture = light or heavy

## Artifact defaults by phase

### Phase 1 — Intent

| Artifact | Default mode |
| --- | --- |
| project-brief | interview |
| business-case | interview |

### Phase 2 — Specification

| Artifact | Default mode |
| --- | --- |
| prd | interview |
| requirements-catalog | interview |
| journeys | interview |
| acceptance-catalog | interview |

### Phase 3 — Design

| Artifact | Default mode |
| --- | --- |
| solution-design | interview |
| adr | interview |
| c4 | interview — context level only |

### Phase 4 — Govern & Operate

| Artifact | Default mode | Override rule |
| --- | --- | --- |
| ai-use-policy | skipped | activate if AI involvement = core or consumer |
| test-strategy | interview | always active |
| security-baseline | interview | always active |
| delivery-plan | interview | always active |

### Phase 5 — Adapt

| Artifact | Default mode |
| --- | --- |
| language-adaptation | interview |
| repo-sync | extract |
