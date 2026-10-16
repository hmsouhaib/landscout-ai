"""One local physical IGN context shared by the two optional screening slices."""

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

from landscout.sources.ign_bdtopo_fr import (
    IgnBdTopoExtraction,
    IgnBdTopoSourceConfig,
    download_ign_bdtopo_archive,
    extract_ign_bdtopo_archive,
)


@dataclass(frozen=True)
class _IgnContext:
    extraction: IgnBdTopoExtraction
    marker_identity: dict[str, str | int]


def _acquire_ign(
    config: IgnBdTopoSourceConfig, cache_dir: Path, extraction_dir: Path | None
) -> _IgnContext:
    download = download_ign_bdtopo_archive(
        config, cache_dir=cache_dir, allow_download=False
    )
    extraction = extract_ign_bdtopo_archive(
        download, config, extraction_dir=extraction_dir, allow_extract=False
    )
    # The extractor owns default selection. Check before resolve hides links.
    actual = extraction.extraction_path
    if any(p.is_symlink() or p.is_junction() for p in (actual, *actual.parents)):
        raise ValueError("IGN extraction path contains a link or junction")
    actual = actual.resolve()
    if actual == cache_dir or cache_dir.is_relative_to(actual):
        raise ValueError("IGN extraction target collides with archive cache")
    marker = actual / ".landscout-extraction.json"
    raw = marker.read_bytes()
    return _IgnContext(
        extraction,
        {
            "path": str(marker),
            "size_bytes": len(raw),
            "sha256": sha256(raw).hexdigest(),
        },
    )
