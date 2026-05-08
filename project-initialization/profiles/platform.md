# Profile: Platform / Regulated

Use for multi-team platforms, regulated-industry products, or systems with heavy compliance requirements.

## Activation triggers

- Project type = "platform"
- Or: regulatory posture = heavy (regardless of project type)

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
| c4 | interview — context and container levels; component level if team = multi-team |

### Phase 4 — Govern & Operate

| Artifact | Default mode | Override rule |
| --- | --- | --- |
| ai-use-policy | interview | activate if AI involvement = core or consumer |
| test-strategy | interview | always active |
| security-baseline | interview | always active |
| delivery-plan | interview | always active |

### Phase 5 — Adapt

| Artifact | Default mode |
| --- | --- |
| language-adaptation | interview |
| repo-sync | extract |
