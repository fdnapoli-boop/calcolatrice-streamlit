"""Test della funzione calculate."""

import pytest

from task_app.calculator import calculate


def test_addition() -> None:
    assert calculate(2, 3, "+") == 5


def test_subtraction() -> None:
    assert calculate(8, 3, "-") == 5


def test_multiplication() -> None:
    assert calculate(4, 2.5, "*") == 10


def test_division() -> None:
    assert calculate(10, 4, "/") == 2.5


def test_division_by_zero() -> None:
    with pytest.raises(
        ZeroDivisionError, match="Non è possibile dividere per zero"
    ):
        calculate(10, 0, "/")


def test_unknown_operation() -> None:
    with pytest.raises(ValueError):
        calculate(2, 3, "%")
