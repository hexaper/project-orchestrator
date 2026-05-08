# Artifact Rubric: Language Adaptation

- Phase: 5 (Adapt)
- Output paths: `src/`, `tests/`, `config/`, `.gitignore`, `.editorconfig`, `src/AGENTS.md`
- Template: n/a — adapts existing slot directories based on canonical docs
- Prerequisites: solution-design, all accepted ADRs

## Gating criteria

Language adaptation is complete when:
- Language/runtime is chosen and reflected in `src/` structure.
- Primary framework is chosen and reflected in `src/` structure.
- Test runner is chosen and reflected in `tests/`.
- `.gitignore` covers the chosen language's runtime artifacts.
- `src/AGENTS.md` slot placeholders are filled with the chosen stack's conventions.

## Interview mode

Read all accepted ADRs first. For any stack decision not yet captured in an ADR:
1. "What language and runtime version will this project use?"
2. "What is the primary framework?"
3. "What test runner and assertion library will you use?"
4. "What package manager: npm, yarn, pip, cargo, go modules, or other?"
5. "What CI platform — GitHub Actions, GitLab CI, or other?"

If an ADR already captures a decision, confirm it rather than re-asking.

## Confirm mode

Present ADR-captured stack decisions. Ask only for what is missing.

## Extract mode

Read ADRs and build adapted directory structure from them. Do not add feature code, dependency version pins not in ADRs, or implementation stubs. Add `[NEEDS-REVIEW: decision required]` for any structural choice not covered by an ADR. Files with `[NEEDS-REVIEW]` markers do not pass the phase gate — resolve every marker before marking the artifact complete.

## Review hooks

- No feature code added — only structural scaffolding.
- `.gitignore` covers the runtime's artifact patterns.
- `src/AGENTS.md` slot guidance names the actual language and framework, not placeholder text.
- Adapted structure matches what the solution design described.
- Frontmatter in `src/AGENTS.md` is complete per schema (`docs/00_operating_model/04_frontmatter_schema.md`).
