# Junior learning path

This project is a tiny laboratory for professional Python ML repository habits. The data functions are intentionally ordinary. The valuable part is the repeatable path from a code change to a trustworthy merge.

## The complete flow

1. Write a small change in `src/`.
2. Run Ruff to find style and likely mistakes.
3. Run mypy to check type contracts.
4. Run pytest and coverage to check behavior and test reach.
5. Run pre-commit before creating a commit.
6. Push a branch.
7. GitHub Actions repeats the checks in a clean Linux environment.
8. Required checks become quality gates, so the pull request cannot merge until they pass.

## Recommended reading order

### 1. `pyproject.toml`

**Why it exists:** It is the central project contract: package metadata, runtime and development dependencies, and tool settings. **Who uses it:** uv, Python build tools, Ruff, mypy, pytest, and coverage. **When it executes:** tools read it whenever they run. **Without it:** there is no single reliable definition of how to install or check this project. **Exercise:** change `line-length` to `100`, run `make lint`, and decide whether the new rule helps.

### 2. `Makefile`

**Why it exists:** It gives developers short, memorable commands that encode the workflow. **Who uses it:** developers and CI-like local workflows. **When it executes:** only when you request a target such as `make check`. **Without it:** every developer has to remember longer tool commands and their flags. **Exercise:** run `make test`, then read which underlying command it invokes.

### 3. `src/`

**Why it exists:** The package contains typed behavior that tools can inspect. **Who uses it:** Python, tests, packaging, and downstream users. **When it executes:** imports and function calls execute it. **Without it:** there is no product code for quality tools to validate. **Exercise:** add a `median_feature` function and write its contract before its implementation.

### 4. `tests/`

**Why it exists:** Tests record expected behavior and protect refactoring. **Who uses it:** pytest locally and GitHub Actions. **When it executes:** `make test`, `make check`, and CI. **Without it:** lint can pass while behavior is wrong. **Exercise:** change one expected value in a test and observe pytest's failure output.

### 5. `.pre-commit-config.yaml`

**Why it exists:** It runs fast, repeatable checks at the commit boundary. **Who uses it:** pre-commit and every contributor who installs its hooks. **When it executes:** usually on `git commit`, and manually with `pre-commit run --all-files`. **Without it:** broken formatting and simple quality failures reach review more often. **Exercise:** run `uv run pre-commit run --all-files` and inspect which hooks run.

### 6. `.github/workflows/ci.yml`

**Why it exists:** It repeats the quality gate on a clean hosted machine. **Who uses it:** GitHub Actions for pushes and pull requests. **When it executes:** on every configured push or pull request. **Without it:** local checks are optional and merge quality depends on individual habits. **Exercise:** add a harmless CI step, push it, and read its log.

## Tool boundaries

- **IDE checks:** immediate feedback while editing; excellent for navigation and small errors, but not a trusted shared result.
- **Pre-commit:** a contributor-side commit gate; fast and close to the change, but it depends on hooks being installed and can be bypassed.
- **Makefile checks:** a documented local interface; easy to remember and close to CI, but still voluntary.
- **GitHub Actions CI:** the shared, repeatable gate on a clean machine; it is slower and costs compute, but branch protection can require it before merge.

Pre-commit improves feedback speed. CI is the authority. `make check` should approximate the CI quality checks so failures are found before a push.

## CI job shape

This template uses one job because it is easy to understand and has low setup duplication. In a larger repository, lint/type/test/security can become separate jobs that run in parallel. Parallel jobs reduce wall-clock time but add workflow YAML, repeated dependency setup, artifact coordination, and more failure surfaces. Keep checks that must all pass as required status checks either way.

## What to notice

`uv.lock` records a reproducible resolution, while `pyproject.toml` expresses the intended ranges. Runtime dependencies are separate from the `dev` dependency group because deployed code should not need Ruff or pytest. The `src` layout prevents tests from accidentally importing the working directory instead of the installed package.

## TODO checklist

- [ ] Intentionally break formatting and fix it.
- [ ] Intentionally introduce a type error and fix it.
- [ ] Add one unit test.
- [ ] Add one CI quality gate.
- [ ] Change the coverage threshold and explain the result.
- [ ] Explain the complete pipeline without reading this file.
