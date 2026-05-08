---
name: Codex Tool Assets
description: Use for work under .codex/. Covers vendored Superpowers assets and Codex-specific repository helpers.
applyTo: ".codex/**"
---

# Codex Tool Assets

This directory is part of the tracked template contract.

## Most Important Rules

- Keep vendored Superpowers assets aligned with `.claude/`, `.copilot/`, and `.opencode/` unless Codex requires an intentional difference.
- Treat `.codex/skills/` and `.codex/hooks/` as vendored upstream content from Superpowers 5.1.0.
- Codex's repo-native runtime surface is root `AGENTS.md`, `.codex/hooks.json`, and `.agents/skills/`.
- Keep repo-wide instructions in root `AGENTS.md`; use this directory for Codex-specific hook assets and notes.

## Editing Guidance

- Update `.agents/skills/` together with `.codex/skills/` when vendoring changes.
- Document vendoring source/version changes in `.codex/README.md`, `.agents/README.md`, and the root docs updated in the same task.
- Avoid mixing personal Codex config with tracked repository assets.
