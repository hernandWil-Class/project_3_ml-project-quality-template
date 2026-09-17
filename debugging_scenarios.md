# Debugging scenarios

These are prompts, not complete solutions. Start with the symptom, identify the owning tool, and run the narrowest check first.

## 1. Works locally but CI fails

**Symptoms:** local tests pass, but the pull request fails on GitHub. **Hints:** compare Python versions, lockfile state, environment variables, operating system assumptions, and the exact CI command. Confirm the local run used `uv run` and the same coverage flags.

## 2. pytest succeeds but mypy fails

**Symptoms:** behavior tests are green, but the type job is red. **Hints:** tests exercise runtime values; mypy checks declared contracts and paths that tests may never call. Read the first mypy error, inspect the function annotation, and avoid silencing it until the contract is understood.

## 3. pre-commit modifies files and rejects the commit

**Symptoms:** a commit stops and the working tree changes. **Hints:** formatters can repair files; inspect the diff, stage the intended modifications, and rerun the hooks. A modifying hook is feedback, not proof that the commit should be bypassed.

## 4. CI suddenly fails after a dependency update

**Symptoms:** no application code changed, but installation, tests, or security checks fail. **Hints:** inspect the lockfile diff and release notes, identify whether the failure is compatibility or vulnerability-related, reproduce with the locked environment, and decide whether to upgrade, pin, or roll back.

## 5. Coverage falls below the required threshold

**Symptoms:** tests pass but the coverage command exits non-zero. **Hints:** read the missing line report. Add behavior-focused tests for valuable branches; do not add empty assertions only to inflate a number. Reconsider the threshold if it measures unimportant code.

## 6. `uv sync --locked` fails in CI

**Symptoms:** CI refuses to install because the lockfile is out of date. **Hints:** compare `pyproject.toml` and `uv.lock`, run `uv lock` locally after dependency changes, and commit the resulting lockfile intentionally.

## 7. Security audit fails while tests pass

**Symptoms:** pip-audit reports a vulnerable transitive package. **Hints:** application tests cannot prove dependency safety. Identify the package path, check the advisory severity and fixed version, update the lockfile, and record any accepted exception explicitly.
