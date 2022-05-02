import os
import typing as tp

from ._exceptions import TypeMismatchError, UnprocessableValueError, VariableUnsetError

VarType = tp.TypeVar("VarType")


def _parse_bool_var(value: str) -> bool:
    """Convert the provided string into a boolean"""
    value = value.lower().strip()

    if value in {"1", "yes", "true", "on", "enable"}:
        return True
    elif value in {"0", "no", "false", "off", "disable"}:
        return False
    else:
        raise UnprocessableValueError(
            f'Value "{value}" set for env var cannot be interpreted neither as true nor false.'
        )


CONVERTERS: tp.Dict[tp.Union[tp.Type], tp.Callable[[str], tp.Any]] = {
    str: str,
    int: int,
    float: float,
    bool: _parse_bool_var,
    tp.Optional[str]: lambda x: x,
}


def getenv(
    env_name: str,
    default: VarType = None,
    *,
    var_type: tp.Type = tp.Optional[str],
    optional: bool = False,
) -> tp.Optional[VarType]:
    """
    A wrapper over standard os.getenv() that automatically
    converts provided strings into values of the desired type.

    Same interface as os.getenv(), but with additional var_type and optional arguments.
    """
    if var_type not in CONVERTERS:
        raise UnprocessableValueError(
            f'Type "{var_type.__name__}" cannot be parsed. Supported types are: {list(CONVERTERS.keys())}'
        )

    value = os.getenv(env_name, "NOT_FOUND")

    if value == "NOT_FOUND":
        if optional:
            return default
        else:
            raise VariableUnsetError(
                f'Environment variable "{env_name}" has not been set and is marked as mandatory.'
            )

    try:
        parser = CONVERTERS[var_type]
        return parser(value)
    except ValueError as e:
        raise TypeMismatchError(
            f'An error occurred during type conversion. Failed to convert "{value}" to {var_type.__name__} type. {e}'
        )
