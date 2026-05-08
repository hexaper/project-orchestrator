# tests

Purpose: Verification for workflow correctness, resumability, and adapter conformance.

Current strategy:

- Use Vitest for test execution.
- Keep deterministic checks first, then targeted higher-cost review scenarios.

Recommended shape:

- mirror `src/` where practical so ownership stays obvious
- keep `unit/`, `integration/`, and `e2e/` split by validation scope
- include resumability and phase-gate blocking scenarios as required coverage
- keep fixtures and helpers close to the tests that use them
