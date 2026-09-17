"""Simple feature calculations."""

import pandas as pd


def mean_feature(observations: pd.DataFrame) -> float:
    """Return the mean of feature_a after validating the input."""
    if "feature_a" not in observations:
        raise ValueError("observations must contain feature_a")
    if observations.empty:
        raise ValueError("observations must contain at least one row")
    return float(observations["feature_a"].mean())


def add_ratio_feature(observations: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with feature_a divided by feature_b."""
    required = {"feature_a", "feature_b"}
    missing = required.difference(observations.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
    if (observations["feature_b"] == 0).any():
        raise ValueError("feature_b cannot contain zero")

    result = observations.copy()
    result["feature_ratio"] = result["feature_a"] / result["feature_b"]
    return result
