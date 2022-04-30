import os

from pytest import raises

import typed_getenv

VAR_NAME = "TEST_BOOL"


def test_parse_valid_bool_true() -> None:
    for value in ["1", "yes", "true", "on", "enable"]:
        os.environ[VAR_NAME] = value
        assert typed_getenv.getenv(VAR_NAME, var_type=bool)


def test_parse_valid_bool_false() -> None:
    for value in ["0", "no", "false", "off", "disable"]:
        os.environ[VAR_NAME] = value
        assert not typed_getenv.getenv(VAR_NAME, var_type=bool)


def test_parse_invalid_bool() -> None:
    os.environ[VAR_NAME] = "foo"

    with raises(typed_getenv.UnprocessableValueError):
        typed_getenv.getenv(VAR_NAME, var_type=bool)
