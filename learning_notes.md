# Learning notes

## `pyproject.toml`

This file is declarative configuration for packaging and tools. The project dependency list contains what the package needs at runtime. The `dev` group contains tools used to develop and verify it. A lockfile resolves both into exact versions for repeatability.

## Packages and `src`

`src/ml_template` is an importable package. The `src` layout makes accidental imports from the repository root less likely and tests the installed-package path. `__init__.py` defines the small public surface in this example.

## Tests and coverage

Pytest discovers test functions and gives readable failures. Parametrization runs one test shape against many inputs. Exception tests verify invalid contracts. Coverage reports which executable lines tests reached; it is a signal, not a guarantee of correctness. This project requires 90%, while the current suite reaches 95%.

## Ruff and mypy

Ruff combines fast lint rules and formatting. Mypy checks whether annotated values agree across calls. Neither replaces code review or tests: they answer different questions.

## Pre-commit and Make

Pre-commit installs hooks at the commit boundary. The Makefile is a friendly command catalog. `make check` is deliberately close to the CI gate, so a developer can catch most failures before pushing.

## CI quality gate

The workflow checks out source, installs a declared Python version and locked dependencies, then runs lint, type checks, tests with coverage, and a dependency audit. Pull requests and pushes both run it. Branch protection can make the status required.

## Security

Tests ask whether known examples behave correctly. pip-audit asks whether resolved packages have published vulnerability advisories. Both matter. A passing audit does not mean application code is secure, and a passing test suite does not mean dependencies are safe.

## TODO: teach-back

Write the complete pipeline in your own words:

`write code -> lint -> type check -> unit tests -> pre-commit -> git push -> GitHub Actions -> quality gates -> merge`
