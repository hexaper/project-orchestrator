---
name: Claude Tool Assets
description: Use for work under .claude/. Covers vendored Superpowers skills, hook helpers, and tracked Claude-specific repository assets.
applyTo: ".claude/**"
---

# Claude Tool Assets

This directory is part of the tracked template contract.

## Most Important Rules

- Keep vendored Superpowers assets aligned with `.copilot/`, `.codex/`, and `.opencode/` unless a harness requires an intentional divergence.
- Treat `.claude/skills/` and `.claude/hooks/` as vendored upstream content from Superpowers 5.1.0. Do not hand-edit skill behavior unless intentionally forking the vendor copy.
- Keep machine-specific overrides local-only. `settings.local.json` stays untracked; `settings.json` is the tracked repo default.

## Editing Guidance

- Do not use `CLAUDE.md` files in this repository.
- Put repository-wide workflow rules in root `AGENTS.md`, not here.
- Document any vendoring source/version change in this directory's `README.md` and the root docs updated in the same task.
