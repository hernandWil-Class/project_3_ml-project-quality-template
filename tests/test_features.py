"""Tests for feature helpers."""

import pandas as pd
import pytest

from ml_template.features import add_ratio_feature, mean_feature


def test_mean_feature_returns_numeric_mean() -> None:
    observations = pd.DataFrame({"feature_a": [2, 4, 8]})

    assert mean_feature(observations) == pytest.approx(14 / 3)


def test_add_ratio_feature_does_not_mutate_input() -> None:
    observations = pd.DataFrame({"feature_a": [2, 6], "feature_b": [1, 3]})

    result = add_ratio_feature(observations)

    assert result["feature_ratio"].tolist() == [2.0, 2.0]
    assert "feature_ratio" not in observations


@pytest.mark.parametrize(
    "observations, message",
    [
        (pd.DataFrame({"feature_a": [1]}), "Missing required columns"),
        (pd.DataFrame({"feature_a": [1], "feature_b": [0]}), "zero"),
    ],
)
def test_feature_helpers_reject_invalid_data(
    observations: pd.DataFrame, message: str
) -> None:
    with pytest.raises(ValueError, match=message):
        add_ratio_feature(observations)
