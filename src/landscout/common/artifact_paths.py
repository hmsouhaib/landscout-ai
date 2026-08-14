"""Internal portable filename contracts for byte-sealed artifacts."""

from __future__ import annotations

from pathlib import PurePosixPath, PureWindowsPath


def validate_portable_parquet_filename(value: object, label: str) -> str:
    """Return one portable local Parquet basename or raise ``ValueError``."""

    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{label} must be an exact non-empty string")
    posix = PurePosixPath(value)
    windows = PureWindowsPath(value)
    if (
        posix.is_absolute()
        or windows.is_absolute()
        or posix.name != value
        or windows.name != value
        or posix.suffix.lower() != ".parquet"
        or windows.suffix.lower() != ".parquet"
    ):
        raise ValueError(f"{label} must be one portable local Parquet basename")
    return value
