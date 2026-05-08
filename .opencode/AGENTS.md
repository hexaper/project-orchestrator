---
name: OpenCode Tool Assets
description: Use for work under .opencode/. Covers tracked OpenCode skills, plugins, commands, and local-only workspace support files.
applyTo: ".opencode/**"
---

# OpenCode Tool Assets

This directory now contains tracked repository assets plus a few ignored local-only support paths.

## Most Important Rules

- Keep tracked OpenCode assets aligned with current repository behavior.
- Prefer minimal, high-signal instruction files.
- Avoid duplicating rules that belong in root or closer scoped `AGENTS.md` files.
- Keep vendored Superpowers assets aligned with `.claude/`, `.copilot/`, and `.codex/` unless OpenCode requires an intentional divergence.

## Routing

- Read `.opencode/instructions/AGENTS.md` before editing `.opencode/instructions/**`.

## Editing Guidance

- Update tracked tool assets when agent workflow, standards, or repository conventions actually change.
- Keep local tooling metadata concise and maintainable.
