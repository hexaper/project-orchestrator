#!/usr/bin/env python3
"""
Check that the consolidated init workflow and bootstrap wiring exist across
tracked tool surfaces and that retired phase wrappers are gone. Run from repo root.
"""

from pathlib import Path
import json
import sys

TOOL_DIRS = [".claude", ".copilot", ".codex", ".opencode"]
RETIRED = [
    "init-triage.md",
    "init-intent.md",
    "init-spec.md",
    "init-design.md",
    "init-govern.md",
    "init-adapt.md",
    "init-review.md",
]

COMMAND_TEXT_CHECKS = [
    "project-initialization/phases/",
    "project-initialization/artifacts/",
    "project-initialization/contract.md",
    "[Enter] continue · revisit · show plan · q",
    "Last Revisited",
]

HOOK_FILES = {
    ".claude": Path(".claude/settings.json"),
    ".copilot": Path(".copilot/hooks/hooks.json"),
    ".codex": Path(".codex/hooks.json"),
}

HOOK_COMMAND_SNIPPETS = {
    ".claude": '.claude/hooks/run-hook.cmd" session-start',
    ".copilot": '${CLAUDE_PLUGIN_ROOT}/hooks/run-hook.cmd" session-start',
    ".codex": '.codex/hooks/run-hook.cmd" session-start',
}

OPENCODE_PLUGIN_PATH = Path(".opencode/plugins/superpowers.js")

OPENCODE_PLUGIN_TEXT_CHECKS = [
    "using-superpowers",
    "config.skills.paths",
    "experimental.chat.messages.transform",
    "EXTREMELY_IMPORTANT",
]

errors = []

for tool in TOOL_DIRS:
    init_path = Path(tool) / "commands" / "init.md"
    if not init_path.exists():
        errors.append(f"MISSING: {init_path}")
        continue

    content = init_path.read_text()
    for phrase in COMMAND_TEXT_CHECKS:
        if phrase not in content:
            errors.append(f"MISSING PHRASE in {init_path}: {phrase!r}")

    for retired in RETIRED:
        retired_path = Path(tool) / "commands" / retired
        if retired_path.exists():
            errors.append(f"RETIRED FILE STILL PRESENT: {retired_path}")

for tool, path in HOOK_FILES.items():
    if not path.exists():
        errors.append(f"MISSING HOOK REGISTRATION: {path}")
        continue
    data = json.loads(path.read_text())
    hooks = data.get("hooks", {}).get("SessionStart", [])
    if not hooks:
        errors.append(f"NO SessionStart hook in {path}")
        continue
    commands = [
        hook.get("command", "")
        for entry in hooks
        for hook in entry.get("hooks", [])
        if hook.get("type") == "command"
    ]
    if not any(HOOK_COMMAND_SNIPPETS[tool] in command for command in commands):
        errors.append(f"SessionStart command mismatch in {path}")

if not OPENCODE_PLUGIN_PATH.exists():
    errors.append(f"MISSING OPENCODE BOOTSTRAP: {OPENCODE_PLUGIN_PATH}")
else:
    plugin_content = OPENCODE_PLUGIN_PATH.read_text()
    for phrase in OPENCODE_PLUGIN_TEXT_CHECKS:
        if phrase not in plugin_content:
            errors.append(
                f"MISSING OPENCODE BOOTSTRAP PHRASE in {OPENCODE_PLUGIN_PATH}: {phrase!r}"
            )

if errors:
    print("Parity check FAILED:")
    for error in errors:
        print(f"  {error}")
    sys.exit(1)

print(
    "Parity check PASSED: consolidated init workflow and bootstrap wiring present across tracked tool surfaces."
)
