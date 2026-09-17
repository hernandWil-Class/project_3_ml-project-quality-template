.PHONY: install test lint format type check security clean

install:
	uv sync

test:
	uv run pytest --cov=ml_template --cov-report=term-missing

lint:
	uv run ruff check .
	uv run ruff format --check .

format:
	uv run ruff check --fix .
	uv run ruff format .

type:
	uv run mypy src tests

check: lint type test

security:
	uv export --locked --no-emit-project --format requirements-txt --output-file /tmp/ml-template-requirements.txt
	uv run pip-audit -r /tmp/ml-template-requirements.txt
	rm -f /tmp/ml-template-requirements.txt

clean:
	rm -rf .coverage .pytest_cache .mypy_cache .ruff_cache dist build *.egg-info
