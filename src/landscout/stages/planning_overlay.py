"""Compatibility import for shared technical planning-overlay tolerances."""

from __future__ import annotations

from landscout.common.planning_overlay import (
    ABSOLUTE_OVERLAY_TOLERANCE,
    RELATIVE_OVERLAY_TOLERANCE,
    technical_overlay_tolerance,
)

__all__ = [
    "ABSOLUTE_OVERLAY_TOLERANCE",
    "RELATIVE_OVERLAY_TOLERANCE",
    "technical_overlay_tolerance",
]
