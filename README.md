# Python ML Project Quality Template

A deliberately small synthetic-data package that demonstrates how a Python ML repository can enforce engineering quality.

## Quick start

Install [uv](https://docs.astral.sh/uv/), then run:

```bash
make install
make check
```

The recommended reading order is in [junior_learning_path.md](junior_learning_path.md). The package is intentionally simple: the important artifact is the quality system around it.

## Commands

- `make install`: create/update the uv environment and install the project with development dependencies
- `make test`: run pytest
- `make lint`: check Ruff lint and formatting
- `make format`: format code with Ruff
- `make type`: run mypy
- `make check`: run the pre-PR quality gate locally
- `make security`: audit locked dependencies with pip-audit
- `make clean`: remove generated caches and coverage output

The checks are intentionally strict enough to teach failure diagnosis. See [debugging_scenarios.md](debugging_scenarios.md) when one fails.

## Portfolio statement

This repository demonstrates that I understand how to engineer and govern a production-quality Python ML repository, not only how to train models.

## TODOs

- [ ] Intentionally break formatting and fix it.
- [ ] Introduce a type error and make mypy catch it.
- [ ] Add one unit test.
- [ ] Add one CI quality gate.
- [ ] Change the coverage threshold and observe the result.
- [ ] Explain the complete pipeline in my own words.
