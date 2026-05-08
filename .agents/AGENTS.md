---
name: Codex Repo Skills
description: Use for work under .agents/. Covers repo-native Codex skill discovery files.
applyTo: ".agents/**"
---

# Codex Repo Skills

This directory exists for Codex's repo-native skill discovery surface.

## Most Important Rules

- Keep `.agents/skills/` aligned with the vendored mirror in `.codex/skills/`.
- Treat skill content here as tracked vendor content unless intentionally updating the vendored Superpowers version.
- Keep Codex hook registration in `.codex/hooks.json`; this directory is for repo-local skill discovery only.

## Editing Guidance

- Update `.agents/skills/`, `.codex/skills/`, and the related assistant docs together.
- Do not mix personal or machine-local Codex settings into this directory.
