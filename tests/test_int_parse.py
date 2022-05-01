import os

from pytest import raises

from . import TypeMismatchError, getenv

VAR_NAME = "TEST_INT"


def test_parse_valid_integer() -> None:
    os.environ[VAR_NAME] = "123"
    assert getenv(VAR_NAME, var_type=int) == 123


def test_parse_invalid_integer() -> None:
    os.environ[VAR_NAME] = "foo"

    with raises(TypeMismatchError):
        getenv(VAR_NAME, var_type=int)
