# Production trade-offs

## Strict typing versus developer speed

Strict typing catches contract drift early and improves refactoring confidence. It adds annotation work and can be awkward around dynamic pandas operations. Start strict at stable boundaries, use precise types for public functions, and isolate unavoidable dynamic code instead of disabling mypy broadly.

## High coverage versus useful coverage

Coverage is evidence about execution, not correctness. A high number built from trivial tests can hide weak assertions. Set a meaningful threshold, require tests for important behavior and failure paths, and review exceptions explicitly.

## One large CI job versus parallel jobs

One job is simple, cheap to maintain, and easy for beginners to understand. Separate jobs can reduce wall-clock time and show whether lint, tests, or security failed, but they repeat setup and increase workflow complexity. Start with one job; split when runtime or ownership justifies it.

## Pinned versus flexible dependencies

Flexible ranges receive fixes automatically but can change behavior during a build. A committed lockfile gives reproducible installs while declared ranges express supported intent. Update the lockfile in a visible, tested change.

## Blocking versus advisory checks

Block merges on checks with high confidence and high consequence: formatting/lint, type contracts, behavior tests, minimum useful coverage, and known serious dependency vulnerabilities. Make noisy or informational checks advisory until their signal is trustworthy. Document temporary exceptions with owners and expiry dates.

## Dependency update strategies

Automated weekly updates reduce drift. Grouping safe patch updates lowers review volume; separating major or security updates improves diagnosis. Run the full gate for every update and keep rollback straightforward.

## CI runtime and cost

Cache uv downloads, avoid rebuilding unchanged environments, and parallelize only after measuring. Path filters can skip irrelevant jobs in a monorepo, but required checks must not become accidentally bypassable. Optimize the feedback loop without hiding failures.

## ML-specific extensions

Training pipelines add data and model quality gates: schema validation, leakage checks, reproducible seeds, experiment metadata, model performance thresholds, artifact integrity, and expensive integration tests. Keep fast unit checks on pull requests and schedule or stage resource-heavy training validation appropriately.
