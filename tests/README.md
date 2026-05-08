# tests

Purpose: Verification and quality checks for implementation behavior.

Template default:

- Add test files only alongside real behavior changes.

Recommended shape:

- mirror `src/` where practical so ownership stays obvious
- split by scope when needed: `unit/`, `integration/`, and `e2e/`
- keep fixtures and helpers close to the tests that use them
