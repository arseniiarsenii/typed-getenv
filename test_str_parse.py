import os

import typed_getenv

VAR_NAME = "TEST_STR"


def test_parse_valid_string() -> None:
    value = "foo"
    os.environ[VAR_NAME] = value
    assert typed_getenv.getenv(VAR_NAME) == value


def test_parse_string_with_default() -> None:
    default = "bar"
    os.environ.clear()
    assert typed_getenv.getenv(VAR_NAME, default) == default
