from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pkg.calculator import Calculator


def test_addition():
    assert Calculator().evaluate("3 + 5") == 8


def test_subtraction():
    assert Calculator().evaluate("10 - 4") == 6


def test_multiplication():
    assert Calculator().evaluate("3 * 4") == 12


def test_division():
    assert Calculator().evaluate("10 / 2") == 5


def test_nested_expression():
    assert Calculator().evaluate("3 * 4 + 5") == 17


def test_complex_expression():
    assert Calculator().evaluate("2 * 3 - 8 / 2 + 5") == 7


def test_empty_expression():
    assert Calculator().evaluate("") is None


def test_invalid_token():
    try:
        Calculator().evaluate("$ 3 5")
    except ValueError as exc:
        assert str(exc) == "invalid token: $"
    else:
        raise AssertionError("expected ValueError")


def test_not_enough_operands():
    try:
        Calculator().evaluate("+")
    except ValueError as exc:
        assert str(exc) == "not enough operands for operator +"
    else:
        raise AssertionError("expected ValueError")
