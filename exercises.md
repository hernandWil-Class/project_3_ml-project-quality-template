# Exercises

Use a branch for each exercise. Record the command you ran, the failure or success, and what it taught you.

## Junior

1. Intentionally misformat a Python file, run `make lint`, then run `make format` and inspect the diff.
2. Change a pytest expectation so `pytest` fails. Read the assertion output and restore it.
3. Pass a `str` where `mean_absolute_error` expects numbers. Run mypy and repair the type error.
4. Modify `generate_observations` to add a documented behavior, then add a test for it.
5. Manually run `make test`, `make lint`, and `make type`; explain what each one owns.

## Intermediate

1. Add a unit test for the missing `feature_a` branch in `mean_feature` and observe coverage.
2. Raise the coverage threshold temporarily, make the check fail, and decide whether the threshold is justified.
3. Add a Ruff rule such as `D` or `SIM`, fix the findings, and document the trade-off.
4. Add a CI step that runs a command you can explain, then make it a required check in a proposed branch policy.
5. Modify `.pre-commit-config.yaml` to add a hook, run it against all files, and explain local versus CI responsibility.

## Senior/staff

1. Decide which checks should block merge and which may be advisory. Defend the decision using failure cost and feedback speed.
2. Propose a CI optimization for a large repository: consider dependency caching, changed-path jobs, parallelism, and required status checks.
3. Design a quality strategy for a 20-person DS team with shared templates, ownership, exceptions, dashboards, and migration support.
4. Propose a dependency upgrade strategy covering lockfile updates, Dependabot, vulnerability severity, staging, and rollback.
5. Explain how this template should change for ML training pipelines: data validation, reproducibility, experiment metadata, expensive integration tests, model checks, and artifact promotion.

## Evidence to collect

- A screenshot or log showing a deliberate failure.
- A short explanation of why the tool caught it.
- The smallest fix that restored the gate.
- A note about what CI should enforce that local tooling cannot guarantee.
