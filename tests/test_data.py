"""Tests for data helpers."""

import pandas as pd
import pytest

from ml_template.data import generate_observations, validate_observations


@pytest.mark.parametrize("count", [1, 3, 10])
def test_generate_observations_has_expected_shape(count: int) -> None:
    observations = generate_observations(count)

    assert len(observations) == count
    assert list(observations.columns) == ["feature_a", "feature_b", "target"]


def test_validate_observations_accepts_generated_data() -> None:
    validate_observations(generate_observations())


@pytest.mark.parametrize(
    "observations, message",
    [
        (pd.DataFrame({"feature_a": [1]}), "Missing required columns"),
        (
            pd.DataFrame(columns=["feature_a", "feature_b", "target"]),
            "at least one row",
        ),
        (
            pd.DataFrame({"feature_a": [1], "feature_b": [2], "target": [None]}),
            "missing values",
        ),
    ],
)
def test_validate_observations_rejects_invalid_data(
    observations: pd.DataFrame, message: str
) -> None:
    with pytest.raises(ValueError, match=message):
        validate_observations(observations)


def test_generate_observations_rejects_non_positive_count() -> None:
    with pytest.raises(ValueError, match="positive"):
        generate_observations(0)
