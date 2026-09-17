"""Tests for metrics."""

import pytest

from ml_template.metrics import mean_absolute_error


def test_mean_absolute_error_returns_average_distance() -> None:
    assert mean_absolute_error([1, 3, 5], [2, 1, 8]) == pytest.approx(2.0)


@pytest.mark.parametrize(
    "actual, predicted, message",
    [
        ([], [1], "must not be empty"),
        ([1], [], "must not be empty"),
        ([1], [1, 2], "equal lengths"),
    ],
)
def test_mean_absolute_error_rejects_invalid_inputs(
    actual: list[float], predicted: list[float], message: str
) -> None:
    with pytest.raises(ValueError, match=message):
        mean_absolute_error(actual, predicted)
