---
name: Project Initialization Rules
description: Use for work under project-initialization/. Covers phase content, artifact rubrics, profile defaults, and shared contract maintenance.
applyTo: "project-initialization/**"
---

# Project Initialization Rules

Apply these rules when editing files under `project-initialization/`.

## Most important rules

- Keep tool-neutral. Nothing in this directory references `.claude/`, `.copilot/`, or `.codex/` by name.
- One file per artifact rubric. Artifact rubrics in `artifacts/` define questions, gating, and review hooks. Phase files in `phases/` define walk order and orchestration only.
- When changing stage names, stop rules, concern framing, or the output format, update `contract.md` first; then update any phase or artifact files that reference those rules.
- When changing the plan file structure, update `plan-template.md`; then update `phases/0-triage.md` which initializes it.
- Profile defaults in `profiles/` are starting points. Users override them at triage. Do not add tool-specific logic to profiles.
- Run `npx -y markdownlint-cli2 project-initialization/**/*.md` before committing changes here.
