"""Data validation and synthetic observation generation."""

import pandas as pd

REQUIRED_COLUMNS = ("feature_a", "feature_b", "target")


def validate_observations(observations: pd.DataFrame) -> None:
    """Raise ValueError when observations lack required numeric columns."""
    missing = [column for column in REQUIRED_COLUMNS if column not in observations]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    if observations.empty:
        raise ValueError("Observations must contain at least one row")

    if observations[list(REQUIRED_COLUMNS)].isna().any().any():
        raise ValueError("Required columns cannot contain missing values")


def generate_observations(count: int = 10) -> pd.DataFrame:
    """Generate deterministic observations for tests and examples."""
    if count < 1:
        raise ValueError("count must be positive")

    values = range(1, count + 1)
    return pd.DataFrame(
        {
            "feature_a": values,
            "feature_b": [value * 2 for value in values],
            "target": [value * 3 for value in values],
        }
    )
