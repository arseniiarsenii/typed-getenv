import os

from pytest import raises

import typed_getenv

VAR_NAME = "TEST_VAR"


def test_parse_invalid_type() -> None:
    os.environ[VAR_NAME] = "foo"

    with raises(typed_getenv.TypeMismatchError):
        typed_getenv.getenv(VAR_NAME, var_type=int)
