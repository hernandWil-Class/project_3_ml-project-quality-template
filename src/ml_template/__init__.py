"""Small examples used to teach Python ML repository quality practices."""

from ml_template.data import generate_observations, validate_observations
from ml_template.features import add_ratio_feature, mean_feature
from ml_template.metrics import mean_absolute_error

__all__ = [
    "add_ratio_feature",
    "generate_observations",
    "mean_absolute_error",
    "mean_feature",
    "validate_observations",
]
