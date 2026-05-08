---
name: Repository Agent Routing
description: Global instructions for all work in this repository. Keep this file minimal and route detailed rules to the closest subdirectory AGENTS.md.
applyTo: "**"
---
If you use superpowers commands never use git worktree

# Repository Agent Routing

Use this file for repo-wide rules only. Read the closest deeper `AGENTS.md` before editing files in that area.

## Reply Style

- Keep replies short, straight to the point, and limited to relevant information.
- Preserve important context, decisions, risks, and verification details.
- Put the most important information first.

## Repository Structure

- Root purpose: repository scaffold and governance baseline.
- Main directories: `docs/`, `project-initialization/`, `.github/`, `.agents/`, `.claude/`, `.copilot/`, `.codex/`, `.opencode/`, `bin/`, `config/`, `diagrams/`, `examples/`, `scripts/`, `src/`, `tests/`.
- Terms used in this repo: `template` is a reusable `_TEMPLATE.md` starter file, `active document` is a project-specific document that governs current work, and `historical record` is a non-canonical planning or archive document.
- Assistant-native tooling directories `.claude/`, `.copilot/`, `.codex/`, and `.opencode/` are part of the tracked template contract. Codex also uses `.agents/skills/` as a tracked repo-native skill surface. Keep only machine-specific files inside assistant directories ignored.

## Before You Start

Run these checks before doing any non-trivial work:

1. **Check for an existing plan or spec.** Look in `docs/superpowers/plans/` and `docs/superpowers/specs/` for a file that covers the current task. If one exists, read it before writing any code or docs — do not duplicate planning that is already done.
2. **Read relevant ADRs.** Before making any architectural or cross-cutting decision, check `docs/adr/` for ADRs that apply. ADRs are binding. If an accepted ADR conflicts with your intended approach, follow the ADR or explicitly supersede it with a new one.
3. **Check the source-of-truth map for structural changes.** Before adding new directories, moving files, or creating new documentation areas, read [`docs/00-source-of-truth.md`](docs/00-source-of-truth.md) to confirm the correct canonical owner for the content.
4. **Recognize unfilled adaptation slots.** If you encounter `<<FILL IN at adaptation: ...>>` placeholders in any file, do not silently fill them with guesses. Stop, inform the user, and point them to run `/init` so it can route into the Adapt phase first.

## When to Write an ADR

Write an ADR when a decision is **durable** and **cross-cutting** — it will bind future contributors and is not easily reversed. Use this threshold:

| Signal | Action |
|--------|--------|
| Affects shared interfaces, data contracts, or deployment topology | Write an ADR |
| Constrains choices in more than one area of the codebase | Write an ADR |
| Will need to be justified to a future contributor or reviewer | Write an ADR |
| Single-file or single-module change with no shared impact | No ADR needed |
| Reverting it would cost less than an hour | No ADR needed |

For proposals that are not yet decided, open an RFC in `docs/03_architecture/rfcs/` instead. Graduate the RFC to an ADR once the decision is settled.

## Global Workflow

- A fresh clone of this template is unspecialized. The adoption sequence is documented in the root [`README.md`](README.md): run `/init`; it will start triage, then resume the next incomplete initialization phase on subsequent runs. Phase logic lives in [`project-initialization/`](project-initialization/README.md).
- Define scope before editing and avoid unrelated changes.
- Prefer root-cause fixes and explicit, simple changes.
- Keep `AGENTS.md` files up to date when workflow or context-management guidance changes, or when new instructions would materially improve future work.
- For cross-cutting changes that touch docs, src, and tests, apply changes in this order: ADR first (if the decision is durable), then documentation, then code. Never update code before the decision record exists.
- Update documentation in the same task when behavior, workflow, or structure changes.
- Do not claim success without verification evidence.
- If verification cannot run, state what was not run, why, and the residual risk.
- Do not make canonical repository behavior depend on ignored local tooling.

## Model Selection

Use the right model for the task to balance cost and quality:

| Model | Best for | Cost |
|-------|----------|------|
| Haiku | Default subagent work — file reading, simple lookups, exploration | Lowest |
| Sonnet | Default main-session model — day-to-day coding, reviews, test writing, implementation | Medium |
| Opus | Complex architecture, multi-step reasoning, debugging subtle issues | Highest |

Rules:
- **Haiku is the default for subagents** (Task tool dispatches). It reads files and returns summaries cheaply without polluting main context.
- **Sonnet is the default for the main session**. Most coding, review, and writing tasks do not need Opus.
- **Switch to Opus only when genuinely stuck** — subtle bugs with no obvious root cause, cross-cutting architectural decisions, or reasoning chains that require holding many constraints simultaneously. Switch back to Sonnet once the hard part is done.
- Never use Opus for file reads, simple lookups, or mechanical edits.

## Token Hygiene

Context is money. Keep it clean:

- **`/clear`** — run between unrelated tasks. Stale context from a previous task inflates token cost on every subsequent message.
- **`/compact`** — run at logical breakpoints (after planning, after a debugging session, before switching focus). Summarises context without clearing it.
- **`/cost`** — check token spend for the session. Use it to notice drift before it gets expensive.
- **Delegate exploration to subagents.** A subagent that reads 20 files and returns a two-line summary costs far less than loading those files into the main session. Use the Task tool for any broad codebase search or unfamiliar-territory discovery.
- **Read targeted ranges, not whole files.** When you know the rough location of what you need, pass `offset` and `limit` to the Read tool rather than loading the entire file.
- **Avoid re-reading files you already have.** If you read a file earlier in the session, work from that content — re-reading burns tokens for no gain.
- **Stop before you diverge.** If the task is done, stop. Don't add speculative cleanup, extra comments, or unrequested refactors — each additional tool call compounds context cost.
- **Scope prompts tightly.** Vague or open-ended instructions produce long, exploratory responses. Be specific about what you want, what you've already tried, and what the success condition is.

## Git And Safety

- Never commit credentials, keys, or secrets.
- Keep commits and PRs logically scoped.
- Do not use destructive git actions unless explicitly requested.
- Preserve backward compatibility unless the task explicitly changes the contract.

## Routing Map

- `docs/AGENTS.md` — documentation rules and doc update expectations.
- `docs/adr/AGENTS.md` — ADR authoring and durable implementation decision rules.
- `docs/superpowers/AGENTS.md` — specs, plans, and historical implementation record rules.
- `.github/AGENTS.md` — CI, CODEOWNERS, and branch protection guidance.
- `.agents/AGENTS.md` — Codex repo-native skill discovery guidance.
- `.claude/AGENTS.md` — Claude-specific vendored skills and hook asset guidance.
- `.copilot/AGENTS.md` — Copilot-specific vendored asset guidance.
- `.codex/AGENTS.md` — Codex-specific vendored asset guidance.
- `.opencode/AGENTS.md` — OpenCode-specific vendored asset and local-only path guidance.
- `src/AGENTS.md` — coding practices and implementation rules for source files.
