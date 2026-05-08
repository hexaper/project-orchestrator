---
title: User Journeys — project--orchestrator
status: active
record_class: canonical
audience: [internal, manager]
owner: product-owner
capability: product
phase: planning
cadence: per-release
last_reviewed: 2026-05-08
---

# User Journeys — project--orchestrator

## Personas

**Project Initiator** — a team lead, architect, project manager, or solo developer who is starting a new software project and needs to produce complete, review-ready documentation before implementation planning begins. Their defining characteristic is IT adjacency: they understand software delivery but do not necessarily know what a complete documentation set looks like.

**Reviewer** — a person (human or automated agent) who inspects phase artifacts, classifies findings by severity, and returns structured feedback to the Project Initiator. In this system the Reviewer role may be filled by the `init-reviewer` agent, a human colleague, or both.

---

## User journeys

### J-001 — Project Initiator: Complete a new project documentation set

| Attribute | Detail |
| --- | --- |
| **Persona** | Project Initiator |
| **Goal** | Produce a complete, gate-passing documentation set that enables implementation planning to begin |
| **Start point** | Initiator runs `/init` in a fresh clone of the repository with no initialization plan present |
| **Success outcome** | All phase gates pass, no `[NEEDS-REVIEW]` markers remain, and an implementation plan can be created from the produced artifacts |

**Steps:**

| Step | Actor | Action | Observable result |
| --- | --- | --- | --- |
| 1 | Project Initiator | Runs `/init` with no arguments | System announces Phase 0 (Triage) and begins asking structured questions about the project |
| 2 | Project Initiator | Answers questions about project type, team shape, regulatory posture, and scope | System captures answers as Project Facts and selects the appropriate documentation profile |
| 3 | Project Initiator | Responds to follow-up questions per artifact rubric, one phase at a time | System produces documentation artifacts from the answers and populates the canonical templates |
| 4 | System | Detects conflicting information between answers (e.g., stated scope contradicts a constraint) | System surfaces the conflict, explains the inconsistency, and asks the initiator to resolve it before continuing |
| 5 | Project Initiator | Reviews the first draft of each produced artifact jointly with the system | System flags any gaps, ambiguities, or `[NEEDS-REVIEW]` markers; initiator clarifies or confirms each one |
| 6 | System | Dispatches `init-reviewer` at the end of each phase | Reviewer returns structured findings classified by severity; critical and important findings are resolved before the phase closes |
| 7 | Project Initiator | Runs `/init` again after each phase completes | System routes to the next incomplete phase and resumes without data loss |
| 8 | Project Initiator | Completes all active phases through Phase 6 | All artifacts exist at their output paths, pass `docs_validator`, and contain no unresolved markers |

**Pain point being eliminated:** Without this journey, architectural and scoping decisions accumulate informally during development. The project loses track of its original intent, slows down, or restarts entirely when the gap between what was assumed and what was needed becomes unrecoverable.

---

### J-002 — Project Initiator: Revisit and update a completed artifact

| Attribute | Detail |
| --- | --- |
| **Persona** | Project Initiator |
| **Goal** | Update a specific artifact after concepts evolve without resetting downstream work |
| **Start point** | At least one phase is complete; the initiator has new information or a changed decision to incorporate |
| **Success outcome** | The target artifact is updated to reflect the current understanding; plan state is consistent; no other artifact is corrupted |

**Steps:**

| Step | Actor | Action | Observable result |
| --- | --- | --- | --- |
| 1 | Project Initiator | Runs `/init` and selects `revisit` from the status menu | System renders a flat list of completed phases and their artifacts |
| 2 | Project Initiator | Selects a specific artifact by number (e.g., `1b` for business-case) | System loads only that artifact's rubric in append/extend mode |
| 3 | Project Initiator | Provides updated or clarifying information | System incorporates changes into the artifact and records the session date as `Last Revisited` in the plan |
| 4 | System | Re-evaluates the artifact against its gating criteria | Updated artifact passes gating criteria with no new unresolved markers |
| 5 | Project Initiator | Confirms the update is complete | Plan state is updated; no other artifact or phase status is changed |

---

### J-003 — Reviewer: Inspect phase artifacts and return structured findings

| Attribute | Detail |
| --- | --- |
| **Persona** | Reviewer (human or `init-reviewer` agent) |
| **Goal** | Validate that a completed phase's artifacts meet quality and completeness standards and communicate actionable findings to the initiator |
| **Start point** | A phase has completed and its artifacts have been produced |
| **Success outcome** | All critical and important findings are resolved; the phase can be marked `done` with confidence |

**Steps:**

| Step | Actor | Action | Observable result |
| --- | --- | --- | --- |
| 1 | System | Dispatches Reviewer with artifact file paths, plan path, phase number, and review checklist | Reviewer receives a defined scope and checklist to evaluate against |
| 2 | Reviewer | Reads each artifact and evaluates it against the phase review checklist | Reviewer produces a findings list classified by severity (critical, important, minor, advisory) |
| 3 | Reviewer | Returns structured findings to the system | System receives the findings report and presents it to the Project Initiator |
| 4 | Project Initiator | Addresses each critical and important finding | Artifacts are updated to resolve the finding; the change is visible in the output file |
| 5 | System | Confirms no critical or important findings remain | Phase is marked `done` in the plan; minor and advisory findings are recorded for reference |

---

## Related documents

- [01_prd.md](01_prd.md) — PRD defining the product problem, users, and requirements this journey set supports.
- [02_requirements_catalog_TEMPLATE.md](02_requirements_catalog_TEMPLATE.md) — requirements catalog for detailed requirement tracing.
- [05_acceptance_catalog_TEMPLATE.md](05_acceptance_catalog_TEMPLATE.md) — acceptance catalog where these journey paths become verifiable scenarios.
