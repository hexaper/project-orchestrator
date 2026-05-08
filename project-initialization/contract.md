# Project Initialization Contract

All initialization runs follow these rules exactly. This file is the single authority for cross-phase behavior.

## Per-run stop rules

1. Read the plan file. If missing, stop — tell the user to run `/init`.
2. Verify the previous phase is `done` unless `/init <name>` explicitly routed into a revisit of a completed phase or artifact. If a required prior phase is incomplete, stop — name the incomplete phase.
3. Run all active artifacts end-to-end without intra-phase pauses.
4. Run end-of-phase review before updating the plan.
5. Update the plan in one batch at the end of the run, never incrementally.
6. After the plan update, stop. Do not begin the next phase or read ahead for it. Tell the user to run `/init` to continue.

## Cross-phase fact capture

While a user is providing input for any artifact, classify each statement:

- **Current-artifact fact** — use it to produce the active artifact.
- **Current-phase other-artifact fact** — note it; it will be used when that artifact runs in this phase.
- **Future-phase fact** — write it to `Future-Phase Facts` in the plan under the relevant phase/artifact sub-section, formatted as: `- (captured during Phase N, YYYY-MM-DD): "verbatim or close paraphrase"`.
- **Off-topic** — acknowledge and redirect.

Future-phase facts may promote an artifact's mode at run time. Announce promotions: "I see we captured [X] during Phase N — promoting [artifact] from interview to confirm."

## Concern handling

When a user choice is weak, risky, or inconsistent with project facts already captured, say:

1. **Concern**: what the issue is, stated plainly.
2. **Why it matters here**: one sentence tied to the specific project context.
3. **Stronger option**: one concrete alternative.
4. **Trade-off**: what adopting the stronger option costs.
5. **Acceptable if intentional**: yes or no, with any conditions.

Record the concern in `Concerns And Recommendations` in the plan immediately — do not wait for end-of-phase. Concerns do not block the phase from completing.

## End-of-phase review

After producing all active artifacts, dispatch the `init-reviewer` agent with:

- File paths of all artifacts produced or modified this phase
- Plan file path
- Phase number
- `project-initialization/review-checklist.md`

Apply all critical and important findings before closing the run. Record minor and advisory findings in `Review Findings` and continue.

## End-of-run output format

Output these sections in order:

```text
Stage Completed: Phase N — <Phase Name>
Docs Updated: <comma-separated list of files written or modified>
Review Fixes Applied: <list of critical/important findings that were fixed, or "none">
Concerns And Recommendations: <list of five-part concerns raised this run, or "none">
Parked Questions: <questions raised but not fitting any active artifact, or "none">
Next Recommended Step: Run `/init` to continue. The command will route to the next incomplete phase or revisit target.
```
