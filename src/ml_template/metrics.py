"""Small metrics used by the example tests."""

from collections.abc import Sequence


def mean_absolute_error(actual: Sequence[float], predicted: Sequence[float]) -> float:
    """Return mean absolute error for equally sized sequences."""
    if not actual or not predicted:
        raise ValueError("actual and predicted must not be empty")
    if len(actual) != len(predicted):
        raise ValueError("actual and predicted must have equal lengths")

    errors = [
        abs(actual_value - predicted_value)
        for actual_value, predicted_value in zip(actual, predicted, strict=True)
    ]
    return sum(errors) / len(errors)
