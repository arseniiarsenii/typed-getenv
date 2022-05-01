import os

import pytest

from . import VariableUnsetError, getenv

VAR_NAME = "TEST_STR"


def test_parse_valid_string() -> None:
    value = "foo"
    os.environ[VAR_NAME] = value
    assert getenv(VAR_NAME) == value


def test_parse_optional_string_with_default() -> None:
    default = "bar"
    os.environ.clear()
    assert getenv(VAR_NAME, default, optional=True) == default


def test_parse_mandatory_string_with_default() -> None:
    default = "bar"
    os.environ.clear()

    with pytest.raises(VariableUnsetError):
        getenv(VAR_NAME, default, optional=False)
