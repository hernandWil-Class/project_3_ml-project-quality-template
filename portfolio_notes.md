# Portfolio notes

## Portfolio claim

> I understand how to engineer and govern a production-quality Python ML repository, not only how to train models.

## Evidence this repository shows

- A modern `pyproject.toml` with uv-managed runtime and development dependencies.
- A typed `src` package with validation, feature engineering, and a metric.
- Unit, parametrized, exception, and edge-case tests.
- Ruff linting and formatting, mypy strict typing, pytest-cov, and pre-commit.
- A Makefile that gives contributors a consistent local workflow.
- A locked dependency graph and pip-audit security check.
- GitHub Actions checks on pushes and pull requests.
- Learning material that explains ownership, timing, failure behavior, and trade-offs.

## How to discuss it

Describe one intentional failure for each tool: a formatter change, a wrong test expectation, a type mismatch, a coverage threshold failure, and a vulnerable dependency report. Explain which feedback is local and which status is authoritative for merging.

## Extensions to complete

- [ ] Add a small command-line entry point.
- [ ] Add a data schema object and test it.
- [ ] Add a CI matrix for supported Python versions.
- [ ] Add a separate security job and compare its trade-offs.
- [ ] Add a simple changelog and release process.
- [ ] Write a one-page architecture decision record for the quality gate.

## Interview-ready summary

The package is intentionally uncomplicated so the engineering system stays visible. A contributor gets fast IDE and pre-commit feedback, a documented Makefile workflow, and a clean CI gate that is reproducible because dependencies are locked. The organization can reuse the pattern while adapting thresholds, ownership, and expensive ML-specific checks.
