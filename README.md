# Python ML Project Quality Template

A deliberately small synthetic-data package that demonstrates how a Python ML repository can enforce engineering quality.

## Quick start

Install [uv](https://docs.astral.sh/uv/), then run:

```bash
make install
make check
```

The package is intentionally simple: the important artifact is the quality system around it. Use the roadmap below to work through the learning materials in order.

## Learning roadmap

These files have different jobs; they are not four books to read from beginning to end:

1. **Start with [junior_learning_path.md](junior_learning_path.md).** Follow its numbered reading order to learn the project pieces and how a change moves from your computer through checks and into CI.
2. **Practice with the Junior section of [exercises.md](exercises.md).** Do these after the matching topic in the learning path. Make one small change, run the command, observe the result, and write down what you learned. The Intermediate and Senior/staff sections are later challenges, not prerequisites for getting started.
3. **Use [debugging_scenarios.md](debugging_scenarios.md) when something fails.** This is a troubleshooting reference, not a stage you must finish in order. Pick the scenario that matches the error, then investigate it using the hints.
4. **Use [interview_questions.md](interview_questions.md) to check your understanding.** Try answering without looking at the code, and include an example from this project. Questions 1–9 review core concepts; questions 10–18 are stretch topics about larger systems and operational decisions.

In short: **Quick start (this README instructions) → learning path → Junior exercises → interview questions 1–9.** Use debugging scenarios whenever you get stuck. After the basics feel familiar, move to the Intermediate exercises and remaining interview questions, then try the Senior/staff exercises.

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
