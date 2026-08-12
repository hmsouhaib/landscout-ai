"""Stable French literal-search normalization with raw Unicode span fidelity."""

from __future__ import annotations

import unicodedata

SEARCH_NORMALIZATION_PROFILE = "fr_literal_v1"

_APOSTROPHES = frozenset("'’‘ʼ‛＇ꞌ")
_DASHES = frozenset("-‐‑‒–—―−﹘﹣－")
_SPECIAL_EXPANSIONS = {"œ": "oe", "Œ": "oe", "æ": "ae", "Æ": "ae"}


def normalize_planning_search_text_with_mapping(
    value: str,
) -> tuple[str, tuple[tuple[int, int], ...]]:
    """Normalize literal-search text and map each output character to a raw span."""

    output: list[str] = []
    raw_spans: list[tuple[int, int]] = []
    pending_space_span: tuple[int, int] | None = None
    pending_ignored_start: int | None = None
    raw_position = 0
    while raw_position < len(value):
        raw_character = value[raw_position]
        if raw_character == "\u00ad":
            if raw_spans:
                previous_start, _ = raw_spans[-1]
                raw_spans[-1] = (previous_start, raw_position + 1)
            if pending_ignored_start is None:
                pending_ignored_start = raw_position
            raw_position += 1
            continue
        raw_end = raw_position + 1
        while raw_end < len(value) and unicodedata.combining(value[raw_end]):
            raw_end += 1
        cluster = value[raw_position:raw_end]
        expanded = _SPECIAL_EXPANSIONS.get(raw_character, raw_character)
        emitted: list[str] = []
        for character in unicodedata.normalize("NFKD", expanded + cluster[1:]):
            if unicodedata.combining(character):
                continue
            if character in _APOSTROPHES:
                folded = "'"
            elif character in _DASHES:
                folded = "-"
            else:
                folded = character.casefold()
            emitted.extend(folded)
        if not emitted:
            raw_position = raw_end
            continue
        if all(character.isspace() for character in emitted):
            if output:
                if pending_space_span is None:
                    pending_space_span = (raw_position, raw_end)
                else:
                    pending_space_span = (pending_space_span[0], raw_end)
            raw_position = raw_end
            continue
        if pending_space_span is not None:
            output.append(" ")
            raw_spans.append(pending_space_span)
            pending_space_span = None
        for normalized_character in emitted:
            output.append(normalized_character)
            raw_spans.append(
                (
                    pending_ignored_start
                    if pending_ignored_start is not None
                    else raw_position,
                    raw_end,
                )
            )
        pending_ignored_start = None
        raw_position = raw_end
    return "".join(output), tuple(raw_spans)


def normalize_planning_search_text(value: str) -> str:
    """Normalize text using the stable ``fr_literal_v1`` search profile."""

    return normalize_planning_search_text_with_mapping(value)[0]


def raw_context_from_spans(
    raw_text: str,
    raw_spans: tuple[tuple[int, int], ...],
    normalized_start: int,
    normalized_end: int,
) -> str:
    """Return the exact raw substring covering a normalized-text range."""

    if normalized_start >= normalized_end:
        return ""
    raw_start = raw_spans[normalized_start][0]
    raw_end = raw_spans[normalized_end - 1][1]
    return raw_text[raw_start:raw_end]
