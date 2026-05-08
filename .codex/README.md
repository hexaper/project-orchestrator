# Codex Tool Assets

Tracked Codex-facing Superpowers assets for this template live here.

## What is here

- `hooks.json` — repo-native Codex hook registration
- `hooks/` — vendored bootstrap helper scripts
- `skills/` — vendored Superpowers 5.1.0 mirror kept aligned with `.agents/skills/`
- `commands/init.md` — consolidated initialization command surface mirrored with the sibling tool directories

## Runtime note

Codex uses these repo-native surfaces in this template:

- `AGENTS.md` — repo-wide instructions
- `.codex/hooks.json` — repo-local hook registration
- `.agents/skills/` — repo-local skill discovery

This directory keeps the Codex-specific hook assets plus a vendored mirror of the skill tree for parity with the other assistant directories.
