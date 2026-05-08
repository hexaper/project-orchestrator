# config

Purpose: Configuration files for local-first TypeScript workflow execution and CI verification.

Current guidance:

- Keep configuration explicit and environment-scoped.
- Separate shared defaults from environment-specific overrides.
- Commit examples and templates, not secrets.

Recommended shape:

- `config/base/` for shared defaults
- `config/environments/` for environment overlays such as `dev`, `staging`, or `prod`
- `config/local.example.*` for developer-local examples
- secret material should stay outside git or be injected at deploy time
