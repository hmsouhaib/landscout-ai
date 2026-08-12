"""Shared technical tolerances for factual GPU planning overlays."""

from __future__ import annotations

from math import isfinite

# This is the existing one-square-millimetre absolute area guard combined with
# the existing relative guard.  The same numeric behavior is also used for
# line-overlay comparison noise.  It is technical only, never a planning or
# BESS business threshold.
ABSOLUTE_OVERLAY_TOLERANCE = 1e-6
RELATIVE_OVERLAY_TOLERANCE = 1e-12


def technical_overlay_tolerance(reference_value: float) -> float:
    """Return the shared floating-point overlay tolerance for a metric value."""

    if not isfinite(reference_value) or reference_value < 0:
        raise ValueError("Overlay tolerance reference must be finite and non-negative")
    return max(
        ABSOLUTE_OVERLAY_TOLERANCE,
        reference_value * RELATIVE_OVERLAY_TOLERANCE,
    )
