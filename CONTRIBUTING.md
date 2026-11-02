# Contributing to Python by Example

Thanks for helping improve this tutorial. The goal is to keep every example **self-contained, runnable, and easy to learn from**.

## Requirements

- Python **3.10 or newer**
- A virtual environment is recommended

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

## How to add or change an example

1. Keep one concept per file.
2. Follow the existing file header (topic, description, key concepts).
3. Include short comments that explain *why*, not only *what*.
4. Use modern type hints (`list[str]`, `dict[str, int]`, `X | None`).
5. Prefer the standard library unless a dependency is already listed in `requirements.txt`.

## Tests

```bash
pytest
```

- Put tests in `11_testing/`
- Name files `test_*.py` so pytest discovers them
- Cover both typical cases and edge cases

## Code style

```bash
black .
isort .
mypy projects/04_weather_cli/solution.py
```

These tools are listed in `requirements.txt`. Match the style of nearby files if you are editing an existing lesson.

## Pull requests

- Describe what you changed and why a learner benefits
- Keep unrelated refactors out of the same PR
- Make sure CI passes

## Questions

Open an issue on GitHub if you are unsure where a new example belongs.
