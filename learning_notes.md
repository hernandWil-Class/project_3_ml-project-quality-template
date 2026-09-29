# Learning notes

## `pyproject.toml`

This file is declarative configuration for packaging and tools. The `[project].dependencies` list contains what the package needs at runtime; here, that is `pandas`. The `[dependency-groups].dev` list contains tools used to develop and verify the project, such as pytest, Ruff, and mypy. They are separate categories, but `uv` can install both into the same virtual environment. The `uv.lock` lockfile records exact versions for repeatable installs.

Use `uv sync --no-dev` to install the project and its runtime dependencies without the development tools. Use `uv sync` to install the project, its runtime dependencies, and the default `dev` group together. In this repository, `make install` runs `uv sync`. (`uv install` is not the command; use `uv sync`.)

```bash
# Runtime dependencies only
uv sync --no-dev

# Runtime and development dependencies
uv sync

# Show the resolved packages, including the dev group
uv tree --all-groups --depth 1
```

In the dependency tree, runtime packages appear under the project, while development tools are marked `(group: dev)`. Remove `--depth 1` to see more of the transitive dependency tree. `uv lock --check` checks that the lockfile still matches the project configuration.

## Packages and `src`

`src/ml_template` is an importable package. The `src` layout makes accidental imports from the repository root less likely and tests the installed-package path. `__init__.py` defines the small public surface in this example.

## Tests and coverage

Pytest discovers test functions and gives readable failures. Parametrization runs one test shape against many inputs. Exception tests verify invalid contracts. Coverage reports which executable lines tests reached; it is a signal, not a guarantee of correctness. This project requires 90%, while the current suite reaches 95%.

## Ruff and mypy

**Linting** is an automated review of source code against a set of rules. It looks for suspicious code, unused items, and inconsistent practices before the program runs. A linter reports where a rule is broken and identifies the rule; it does not run the program, fix every possible bug, or normally rewrite code formatting. In this project, Ruff lint rules are selected from the `E`, `F`, `I`, `B`, and `UP` families. Run `uv run ruff check .` to inspect the project.

For example, the rule `F401` flags an import that the code never uses:

```python
import os
```

Ruff reports that `os` is unused so you can remove it.

**Formatting** changes how code is laid out, such as spaces and quote style. It does not look for suspicious logic or check types. This project's Ruff formatter uses double quotes and consistent spacing. `uv run ruff format --check .` reports files that need formatting; `uv run ruff format .` rewrites them. For example:

`message='hello'` becomes `message = "hello"` after formatting.

The commands for linting and formatting are:

```bash
uv run ruff check .          # Find lint violations
uv run ruff check --fix .    # Apply safe lint fixes
uv run ruff format --check . # Check formatting without changing files
uv run ruff format .         # Apply formatting
```

**Type checking:** Mypy uses annotations to check that values passed to and returned from functions have compatible types. It does not run the code. This function promises an integer but returns a string, so `uv run mypy src tests` reports a type error:

```python
def get_count() -> int:
    return "3"
```

Returning `3` instead of `"3"` fixes the mismatch. This is mypy's job; Ruff formatting would only adjust code style, and Ruff linting checks its configured rules.

```bash
uv run mypy src tests
```

## Pre-commit and Make

Pre-commit is a tool that Git runs automatically just before it records a commit. In this project, the hooks run Ruff lint with safe fixes, Ruff formatting, and mypy on the files being committed. If a hook reports a problem or changes a file, the commit pauses; review the change, stage it with `git add` again, and retry the commit.

After installing the project tools with `make install`, activate the hooks once in this clone of the repository:

```bash
uv run pre-commit install
```

This sets up Git to call Pre-commit before each commit. To run the hooks manually on every tracked file instead, use `uv run pre-commit run --all-files`. Pre-commit is a local early check; GitHub Actions still runs its own checks after you push.

## CI quality gate

The workflow checks out source, installs a declared Python version and locked dependencies, then runs lint, type checks, tests with coverage, and a dependency audit. Pull requests and pushes both run it. Branch protection can make the status required.

## Security

Tests ask whether known examples behave correctly. pip-audit asks whether resolved packages have published vulnerability advisories. Both matter. A passing audit does not mean application code is secure, and a passing test suite does not mean dependencies are safe.

## TODO: teach-back

Write the complete pipeline in your own words:

`write code -> lint -> type check -> unit tests -> pre-commit -> git push -> GitHub Actions -> quality gates -> merge`
