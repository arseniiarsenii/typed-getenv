import os

from pytest import raises

import typed_getenv

VAR_NAME = "TEST_INT"


def test_parse_valid_integer() -> None:
    os.environ[VAR_NAME] = "123"
    assert typed_getenv.getenv(VAR_NAME, var_type=int) == 123


def test_parse_invalid_integer() -> None:
    os.environ[VAR_NAME] = "foo"

    with raises(typed_getenv.TypeMismatchError):
        typed_getenv.getenv(VAR_NAME, var_type=int)
