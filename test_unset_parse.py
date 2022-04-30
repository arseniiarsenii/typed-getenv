from pytest import raises

import typed_getenv

VAR_NAME = "TEST_UNSET"


def test_parse_unset_var() -> None:
    with raises(typed_getenv.VariableUnsetError):
        typed_getenv.getenv(VAR_NAME, var_type=str)
