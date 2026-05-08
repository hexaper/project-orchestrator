---
name: GitHub Automation Rules
description: Use for work under .github/. Covers CODEOWNERS, workflows, and branch protection related guidance.
applyTo: ".github/**"
---

# GitHub Automation Rules

This directory controls repository automation and ownership metadata.

## Most Important Rules

- Keep CODEOWNERS aligned with real ownership boundaries.
- Keep CI commands current and runnable.
- Preserve branch protection intent: required checks, required review, and no force-push assumptions.

## Editing Guidance

- Prefer small, auditable workflow changes.
- Document behavior changes elsewhere if workflow expectations for contributors or operators change.
- Avoid adding unnecessary automation or infrastructure complexity.
