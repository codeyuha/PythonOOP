"""Tests for StringLengthChecker."""

import pytest
from task.task1_1 import StringLengthChecker


@pytest.fixture
def checker():
    return StringLengthChecker(min_length=3, max_length=10)


def test_valid_length(checker):
    assert checker.check("hello") is True
    assert checker.get_length("hello") == 5


def test_too_short(checker):
    assert checker.check("hi") is False
    with pytest.raises(ValueError, match="too short"):
        checker.validate("hi")


def test_too_long(checker):
    assert checker.check("this is too long") is False
    with pytest.raises(ValueError, match="too long"):
        checker.validate("this is too long")


def test_boundaries(checker):
    assert checker.check("abc") is True          # exactly min
    assert checker.check("a" * 10) is True       # exactly max


def test_invalid_input(checker):
    with pytest.raises(TypeError):
        checker.check(123)
    with pytest.raises(TypeError):
        checker.get_length(None)


def test_invalid_configuration():
    with pytest.raises(ValueError):
        StringLengthChecker(min_length=-1)
    with pytest.raises(ValueError):
        StringLengthChecker(min_length=10, max_length=5)
