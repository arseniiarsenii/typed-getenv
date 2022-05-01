from pytest import raises

from . import VariableUnsetError, getenv

VAR_NAME = "TEST_UNSET"


def test_parse_unset_var() -> None:
    with raises(VariableUnsetError):
        getenv(VAR_NAME, var_type=str)
