# config

Purpose: Configuration files and environment templates.

Template default:

- Keep configuration language/tool neutral until project choices are explicit.
- Separate shared defaults from environment-specific overrides.
- Commit examples and templates, not secrets.

Recommended shape:

- `config/base/` for shared defaults
- `config/environments/` for environment overlays such as `dev`, `staging`, or `prod`
- `config/local.example.*` for developer-local examples
- secret material should stay outside git or be injected at deploy time
