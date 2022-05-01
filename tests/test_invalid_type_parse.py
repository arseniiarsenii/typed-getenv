import os

from pytest import raises

from . import TypeMismatchError, getenv

VAR_NAME = "TEST_VAR"


def test_parse_invalid_type() -> None:
    os.environ[VAR_NAME] = "foo"

    with raises(TypeMismatchError):
        getenv(VAR_NAME, var_type=int)
