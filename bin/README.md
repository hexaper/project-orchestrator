# bin

Purpose: thin Node.js command wrappers for local workflow operations in the TypeScript runtime.

Use this directory for user-facing command entrypoints only.

- Keep wrappers minimal and delegate behavior to modules in `src/`.
- Prefer Node.js CLI entrypoints or package-script wrappers that invoke TypeScript workflow modules.
- Avoid embedding orchestration logic directly in shell scripts.
- Keep command names aligned with documentation workflow operations.
