---
name: Source Coding Practices
description: Use for work under src/. Covers code quality, implementation style, and change discipline. Most fields are slot placeholders that the language-adaptation prompt fills.
applyTo: "src/**"
---

# Source Coding Practices

Apply these rules when editing files under `src/`.

This file is a **slot template**. A fresh clone of the template is language-agnostic, so the placeholders below are intentionally unfilled. Run the [project-initialization Adapt phase](../project-initialization/phases/5-adapt.md) to populate them, or fill them by hand if you skip that workflow.

**If you encounter unfilled `<<FILL IN at adaptation: ...>>` slots: stop. Do not guess or infer values. Inform the user that the repository has not been adapted yet and direct them to run `/init` first.**

## Most Important Rules

- Prefer simple, explicit code over clever abstractions.
- Keep changes tightly scoped to the requested behavior.
- Fix root causes instead of layering symptom patches.
- Match existing project patterns, naming, and structure.
- Avoid unnecessary dependencies, configuration, or framework complexity.
- Do not mix unrelated responsibilities into one file or module.

## Commands

`<<FILL IN at adaptation: build command(s)>>`
`<<FILL IN at adaptation: test command(s)>>`
`<<FILL IN at adaptation: lint command(s)>>`
`<<FILL IN at adaptation: format command(s)>>`
`<<FILL IN at adaptation: type-check command(s) if applicable>>`

## Project structure

`<<FILL IN at adaptation: where new modules, packages, or features should live; naming conventions; import boundaries>>`

## Code style

`<<FILL IN at adaptation: style rules specific to the chosen language; one short canonical example showing the preferred pattern>>`

## Testing

`<<FILL IN at adaptation: where tests live; framework; what to test (unit, integration, e2e); how to run a single test; coverage expectations>>`

## Git workflow

`<<FILL IN at adaptation: commit-message format; branch naming; review and merge expectations>>`

## Quality rules

- Write code that is easy to read, review, and verify.
- Prefer maintainability over micro-optimizations.
- Add or update tests with behavior changes unless explicitly told not to.
- Call out edge cases, compatibility risks, and verification gaps in the final response.
- Do not claim success without verification evidence; if verification cannot run, state what was not run, why, and the residual risk.
