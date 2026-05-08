# Artifact Rubric: Repository Sync

- Phase: 5 (Adapt)
- Output paths: `README.md`, `AGENTS.md`, `bin/README.md`, `diagrams/README.md`, `examples/README.md`
- Template: n/a — updates existing files to match canonical docs
- Prerequisites: language-adaptation (must be done first)

## Gating criteria

Repository sync is complete when:
- `README.md` project name and description match the project brief.
- `AGENTS.md` directory inventory includes all new directories and removes template-only guidance.
- All slot READMEs (`bin/`, `diagrams/`, `examples/`) describe their role in the specific project.
- No entry surface still references the template's default initialization guidance.

## Mode: extract only

Repo sync always runs in extract mode — it reads canonical docs and updates entry surfaces to match. It does not ask questions.

Steps:
1. Read `docs/00_governance/00_project_brief.md` for project name and one-line summary.
2. Update `README.md`: replace template description with project name and summary; update the layout table to reflect actual directories in use; remove the initialization journey diagram (it is no longer needed post-init).
3. Update `AGENTS.md`: update directory inventory; update routing guidance to reference project-specific docs instead of template guidance.
4. Update slot READMEs to describe their actual role in this project.
5. Verify repository entry surfaces and tracked tool-specific `/init` wrappers now point users at the consolidated `/init` workflow instead of any retired `/init-*` command.

## Review hooks

- No template boilerplate remains in `README.md` or `AGENTS.md`.
- `README.md` project description matches the brief verbatim or closely paraphrased.
- Slot READMEs are project-specific, not generic template guidance.
- No broken links introduced in any updated file.
