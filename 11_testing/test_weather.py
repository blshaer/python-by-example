"""Tests for the weather CLI helpers (no live network calls)."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any

import pytest

SOLUTION_PATH = (
    Path(__file__).resolve().parents[1] / "projects" / "04_weather_cli" / "solution.py"
)


def load_weather_module():
    spec = importlib.util.spec_from_file_location("weather_solution", SOLUTION_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


weather = load_weather_module()


def test_known_weather_code() -> None:
    icon, description = weather.get_weather_description(0)
    assert "Clear sky" in description
    assert icon


def test_unknown_weather_code() -> None:
    icon, description = weather.get_weather_description(9999)
    assert description == "Unknown"
    assert icon == "❓"


def test_cache_decorator_avoids_second_call() -> None:
    calls = {"count": 0}

    @weather.cache_response
    def lookup(city: str) -> dict[str, Any]:
        calls["count"] += 1
        return {"city": city}

    first = lookup("Gaza")
    second = lookup("Gaza")

    assert first == second
    assert calls["count"] == 1


def test_geocode_city_not_found(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(weather, "fetch_json", lambda url: {"results": []})
    weather.geocode_city.cache.clear()
    assert weather.geocode_city("NotARealCityXYZ") is None


def test_geocode_city_parses_result(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        weather,
        "fetch_json",
        lambda url: {
            "results": [
                {
                    "name": "Gaza",
                    "country": "Palestinian Territory",
                    "latitude": 31.5,
                    "longitude": 34.47,
                }
            ]
        },
    )
    weather.geocode_city.cache.clear()
    result = weather.geocode_city("Gaza")
    assert result is not None
    assert result["name"] == "Gaza"
    assert result["latitude"] == 31.5
