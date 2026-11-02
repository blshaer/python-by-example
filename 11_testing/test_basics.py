"""
================================================================================
File: test_basics.py
Topic: Introduction to Unit Testing with pytest
================================================================================

This file introduces unit testing, a professional practice used to ensure that
code behaves as expected. We use pytest, the industry standard for Python.

Key Concepts:
- Writing test functions (names start with test_)
- Assertions (checking that a condition is True)
- Parametrized tests
- Expected exceptions
- Running tests from the terminal: pytest
================================================================================
"""

from __future__ import annotations

import pytest


def add(a: int, b: int) -> int:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def grade(score: int) -> str:
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (2, 3, 5),
        (-1, -1, -2),
        (5, 0, 5),
        (0, 0, 0),
        (100, -40, 60),
    ],
)
def test_add(a: int, b: int, expected: int) -> None:
    assert add(a, b) == expected


def test_divide_normal() -> None:
    assert divide(10, 2) == 5


def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(10, 0)


@pytest.mark.parametrize(
    ("score", "letter"),
    [
        (95, "A"),
        (80, "B"),
        (70, "C"),
        (60, "D"),
        (59, "F"),
        (0, "F"),
        (100, "A"),
    ],
)
def test_grade(score: int, letter: str) -> None:
    assert grade(score) == letter


def test_grade_rejects_invalid_scores() -> None:
    with pytest.raises(ValueError):
        grade(-1)
    with pytest.raises(ValueError):
        grade(101)


if __name__ == "__main__":
    print("Run this file using: pytest")
