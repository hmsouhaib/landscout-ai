"""Deterministic pandas/GeoPandas frame-schema integrity helpers."""

from __future__ import annotations

import geopandas as gpd  # type: ignore[import-untyped]
import pandas as pd  # type: ignore[import-untyped]
from pyproj import CRS


def deterministic_frame_schema_signature(
    frame: pd.DataFrame,
) -> dict[str, object]:
    """Return the complete ordered schema identity used by integrity envelopes."""

    if not isinstance(frame, pd.DataFrame):
        raise TypeError("Frame schema signature requires a pandas DataFrame")
    index = frame.index
    if isinstance(index, pd.MultiIndex):
        index_dtypes = [str(dtype) for dtype in index.dtypes]
    else:
        index_dtypes = [str(index.dtype)]
    signature: dict[str, object] = {
        "columns": [str(column) for column in frame.columns],
        "dtypes": [str(dtype) for dtype in frame.dtypes],
        "index_class": f"{type(index).__module__}.{type(index).__qualname__}",
        "index_names": [None if name is None else str(name) for name in index.names],
        "index_level_dtypes": index_dtypes,
    }
    if isinstance(frame, gpd.GeoDataFrame):
        geometry_column = frame.geometry.name
        if geometry_column not in frame.columns:
            raise ValueError("GeoDataFrame active geometry column is missing")
        signature["geometry_column"] = str(geometry_column)
        if frame.crs is None:
            raise ValueError("GeoDataFrame CRS is missing")
        signature["crs"] = CRS.from_user_input(frame.crs).to_json_dict()
    return signature
