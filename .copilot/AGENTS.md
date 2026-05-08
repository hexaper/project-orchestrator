---
name: Copilot Tool Assets
description: Use for work under .copilot/. Covers vendored Superpowers assets that back the repository's Copilot integration surface.
applyTo: ".copilot/**"
---

# Copilot Tool Assets

This directory is part of the tracked template contract.

## Most Important Rules

- Keep vendored Superpowers assets aligned with `.claude/`, `.codex/`, and `.opencode/` unless a harness-specific difference is required.
- Treat `.copilot/skills/` and `.copilot/hooks/` as vendored upstream content from Superpowers 5.1.0.
- Keep actual Copilot repository instructions in `.github/copilot-instructions.md` and use this directory for vendored workflow assets and reference material.

## Editing Guidance

- Prefer root docs or `.github/copilot-instructions.md` for behavior guidance that Copilot must actually read.
- Document vendoring source/version changes in `.copilot/README.md` and the root docs updated in the same task.
