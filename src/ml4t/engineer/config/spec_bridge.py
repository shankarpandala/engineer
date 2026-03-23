"""Compatibility bridge from shared market-data specs to engineer contracts."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from ml4t.engineer.config.data_contract import DataContractConfig


def _get_field(source: Mapping[str, Any] | object | None, *names: str) -> Any:
    """Return the first available field value from a mapping or object."""
    if source is None:
        return None

    if isinstance(source, Mapping):
        for name in names:
            if name in source:
                return source[name]
        return None

    for name in names:
        if hasattr(source, name):
            return getattr(source, name)
    return None


def data_contract_from_market_data_spec(
    spec: Mapping[str, Any] | object,
) -> DataContractConfig:
    """Build a dataframe contract from a shared market-data spec shape.

    The bridge accepts either a nested mapping produced by ``MarketDataSpec.to_dict()``
    or an object exposing a ``schema`` attribute with the same field names.
    """

    schema = _get_field(spec, "schema")

    timestamp_col = _get_field(schema, "timestamp_col") or _get_field(spec, "timestamp_col")
    symbol_col = _get_field(schema, "entity_col", "symbol_col") or _get_field(
        spec, "entity_col", "symbol_col"
    )
    close_col = _get_field(schema, "close_col", "price_col") or _get_field(
        spec, "close_col", "price_col"
    )

    return DataContractConfig(
        timestamp_col=timestamp_col or "timestamp",
        symbol_col=symbol_col or "symbol",
        price_col=close_col or "close",
        open_col=_get_field(schema, "open_col") or _get_field(spec, "open_col") or "open",
        high_col=_get_field(schema, "high_col") or _get_field(spec, "high_col") or "high",
        low_col=_get_field(schema, "low_col") or _get_field(spec, "low_col") or "low",
        close_col=close_col or "close",
        volume_col=_get_field(schema, "volume_col") or _get_field(spec, "volume_col") or "volume",
    )


__all__ = ["data_contract_from_market_data_spec"]
