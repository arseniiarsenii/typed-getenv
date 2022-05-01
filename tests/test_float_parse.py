import os

from pytest import raises

from . import TypeMismatchError, getenv

VAR_NAME = "TEST_FLOAT"


def test_parse_valid_float() -> None:
    os.environ[VAR_NAME] = "1.23"
    assert getenv(VAR_NAME, var_type=float) == 1.23


def test_parse_invalid_float() -> None:
    os.environ[VAR_NAME] = "foo"

    with raises(TypeMismatchError):
        getenv(VAR_NAME, var_type=float)
