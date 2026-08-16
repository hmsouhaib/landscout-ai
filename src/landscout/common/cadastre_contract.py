"""Internal contracts shared by normalized cadastral stages."""

from collections.abc import Iterable

CADASTRE_GEOMETRY_STATUSES = frozenset({"VALID", "INVALID"})


def validate_cadastre_geometry_statuses(values: Iterable[object]) -> None:
    """Require the exact geometry-status vocabulary emitted by normalization."""

    if any(
        type(value) is not str or value not in CADASTRE_GEOMETRY_STATUSES
        for value in values
    ):
        raise ValueError(
            "geometry_status must contain only exact VALID or INVALID strings"
        )
