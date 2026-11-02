"""
================================================================================
Project 04: Real-time Weather CLI
Difficulty: 🚀 Professional
================================================================================

A professional command-line weather application that fetches real-time data
from the Open-Meteo API (free, no API key needed) and displays it beautifully.

Concepts Used:
- HTTP Requests (urllib — no external dependencies)
- Decorators (caching)
- Type Hinting
- Error Handling (network, API, data)
- JSON parsing
- String formatting and CLI design

================================================================================
"""

import json
import urllib.error
import urllib.parse
import urllib.request
from functools import wraps
from typing import Any, Optional, TypedDict


# -----------------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------------

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

class CityInfo(TypedDict):
    name: str
    country: str
    latitude: float
    longitude: float


class WeatherData(TypedDict):
    temperature: float
    wind_speed: float
    weather_code: int
    humidity: Optional[int]


# WMO Weather interpretation codes
WMO_CODES: dict[int, tuple[str, str]] = {
    0: ("☀️", "Clear sky"),
    1: ("🌤️", "Mainly clear"),
    2: ("⛅", "Partly cloudy"),
    3: ("☁️", "Overcast"),
    45: ("🌫️", "Fog"),
    48: ("🌫️", "Depositing rime fog"),
    51: ("🌦️", "Light drizzle"),
    53: ("🌦️", "Moderate drizzle"),
    55: ("🌧️", "Dense drizzle"),
    61: ("🌧️", "Slight rain"),
    63: ("🌧️", "Moderate rain"),
    65: ("🌧️", "Heavy rain"),
    71: ("🌨️", "Slight snow"),
    73: ("🌨️", "Moderate snow"),
    75: ("❄️", "Heavy snow"),
    80: ("🌧️", "Slight rain showers"),
    81: ("🌧️", "Moderate rain showers"),
    82: ("⛈️", "Violent rain showers"),
    95: ("⛈️", "Thunderstorm"),
    96: ("⛈️", "Thunderstorm with slight hail"),
    99: ("⛈️", "Thunderstorm with heavy hail"),
}


# -----------------------------------------------------------------------------
# Caching Decorator
# -----------------------------------------------------------------------------

def cache_response(func):
    """
    Decorator that caches function responses based on arguments.
    
    This avoids making redundant API calls for the same city
    within a single session.
    """
    _cache: dict[str, Any] = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a cache key from the arguments
        key = str(args) + str(sorted(kwargs.items()))
        if key not in _cache:
            _cache[key] = func(*args, **kwargs)
        else:
            print("  ⚡ Using cached data...")
        return _cache[key]

    # Expose cache for testing / inspection
    wrapper.cache = _cache
    return wrapper


# -----------------------------------------------------------------------------
# API Functions
# -----------------------------------------------------------------------------

def fetch_json(url: str) -> dict[str, Any]:
    """Fetch JSON data from a URL using urllib (no external deps)."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "PythonByExample/1.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.URLError as e:
        raise ConnectionError(f"Network error: {e}")
    except json.JSONDecodeError:
        raise ValueError("Failed to parse API response.")


@cache_response
def geocode_city(city_name: str) -> Optional[CityInfo]:
    """
    Look up a city's coordinates using the Open-Meteo Geocoding API.
    Returns dict with name, country, latitude, longitude or None if not found.
    """
    params = urllib.parse.urlencode({"name": city_name, "count": 1, "language": "en"})
    url = f"{GEOCODING_URL}?{params}"

    data = fetch_json(url)

    if "results" not in data or not data["results"]:
        return None

    result = data["results"][0]
    return {
        "name": result.get("name", city_name),
        "country": result.get("country", "Unknown"),
        "latitude": result["latitude"],
        "longitude": result["longitude"],
    }


@cache_response
def get_weather(latitude: float, longitude: float) -> WeatherData:
    """
    Fetch current weather data for given coordinates.
    Returns dict with temperature, humidity, wind_speed, and weather_code.
    """
    params = urllib.parse.urlencode({
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true",
        "hourly": "relativehumidity_2m",
        "timezone": "auto",
    })
    url = f"{WEATHER_URL}?{params}"

    data = fetch_json(url)

    current = data.get("current_weather", {})
    hourly = data.get("hourly", {})

    # Get current hour's humidity
    humidity = None
    if "relativehumidity_2m" in hourly and hourly["relativehumidity_2m"]:
        from datetime import datetime
        try:
            current_time = datetime.fromisoformat(current.get("time", ""))
            times = hourly.get("time", [])
            for i, t in enumerate(times):
                if datetime.fromisoformat(t) >= current_time:
                    humidity = hourly["relativehumidity_2m"][i]
                    break
        except (ValueError, IndexError):
            humidity = hourly["relativehumidity_2m"][0] if hourly["relativehumidity_2m"] else None

    return {
        "temperature": current.get("temperature", 0),
        "wind_speed": current.get("windspeed", 0),
        "weather_code": current.get("weathercode", 0),
        "humidity": humidity,
    }


# -----------------------------------------------------------------------------
# Display Functions
# -----------------------------------------------------------------------------

def get_weather_description(code: int) -> tuple[str, str]:
    """Get weather icon and description from WMO code."""
    return WMO_CODES.get(code, ("❓", "Unknown"))


def display_weather(city_info: CityInfo, weather: WeatherData) -> None:
    """Display weather data in a beautiful formatted box."""
    icon, condition = get_weather_description(weather["weather_code"])
    location = f"{city_info['name']}, {city_info['country']}"

    # Calculate box width based on content
    box_width = max(38, len(location) + 8)
    inner = box_width - 4

    print()
    print(f"  ╔{'═' * (box_width - 2)}╗")
    print(f"  ║  📍 {location:<{inner - 4}} ║")
    print(f"  ╠{'═' * (box_width - 2)}╣")
    print(f"  ║  🌡️  Temperature:  {weather['temperature']:>6.1f}°C{' ' * (inner - 26)}║")

    if weather["humidity"] is not None:
        print(f"  ║  💧 Humidity:      {weather['humidity']:>5}%{' ' * (inner - 25)}║")
    else:
        print(f"  ║  💧 Humidity:        N/A{' ' * (inner - 23)}║")

    print(f"  ║  💨 Wind Speed:   {weather['wind_speed']:>6.1f} km/h{' ' * (inner - 29)}║")
    print(f"  ║  {icon}  Condition:    {condition:<{inner - 17}}║")
    print(f"  ╚{'═' * (box_width - 2)}╝")


def display_welcome() -> None:
    """Display the welcome banner."""
    print("""
╔══════════════════════════════════════════╗
║        🌤️  WEATHER CLI 🌤️               ║
║    Real-time weather at your terminal    ║
╚══════════════════════════════════════════╝

  Powered by Open-Meteo API (free, no API key needed!)
  Type 'quit' to exit.
    """)


# -----------------------------------------------------------------------------
# Main Application
# -----------------------------------------------------------------------------

def main() -> None:
    """Main entry point for the Weather CLI."""
    display_welcome()

    while True:
        city_name = input("\n  🔍 Enter city name: ").strip()

        if not city_name:
            print("  ⚠️  Please enter a city name.")
            continue

        if city_name.lower() in ("quit", "exit", "q"):
            print("\n  👋 Goodbye! Stay dry out there!")
            break

        try:
            # Step 1: Geocode the city
            print(f"  🔄 Looking up '{city_name}'...")
            city_info = geocode_city(city_name)

            if city_info is None:
                print(f"  ❌ City '{city_name}' not found. Try a different name.")
                continue

            # Step 2: Fetch weather
            weather = get_weather(city_info["latitude"], city_info["longitude"])

            # Step 3: Display
            display_weather(city_info, weather)

        except ConnectionError as e:
            print(f"  ❌ Connection error: {e}")
            print("  💡 Check your internet connection and try again.")
        except Exception as e:
            print(f"  ❌ An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
