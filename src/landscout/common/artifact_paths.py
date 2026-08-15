"""Internal portable filename contracts for byte-sealed artifacts."""

from __future__ import annotations

from pathlib import PurePosixPath, PureWindowsPath

_WINDOWS_FORBIDDEN_CHARACTERS = frozenset('<>:"/\\|?*')
_WINDOWS_RESERVED_BASENAMES = frozenset(
    {"con", "prn", "aux", "nul", "clock$"}
    | {f"com{number}" for number in range(1, 10)}
    | {f"lpt{number}" for number in range(1, 10)}
    | {f"com{number}" for number in "¹²³"}
    | {f"lpt{number}" for number in "¹²³"}
)


def validate_portable_parquet_filename(value: object, label: str) -> str:
    """Return one portable local Parquet basename or raise ``ValueError``."""

    if not isinstance(value, str) or not value or value != value.strip():
        raise ValueError(f"{label} must be an exact non-empty string")
    if any(ord(character) <= 0x1F or ord(character) == 0x7F for character in value):
        raise ValueError(f"{label} contains a control character")
    if any(character in _WINDOWS_FORBIDDEN_CHARACTERS for character in value):
        raise ValueError(f"{label} contains a Windows-forbidden character")
    if value.endswith((".", " ")):
        raise ValueError(f"{label} must not end in a dot or space")
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
    reserved_stem = value.split(".", 1)[0].casefold()
    if reserved_stem in _WINDOWS_RESERVED_BASENAMES:
        raise ValueError(f"{label} uses a Windows-reserved basename")
    return value
