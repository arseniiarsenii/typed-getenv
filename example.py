from typing import Optional

# Import the getenv function from the package
from typed_getenv import getenv

# Get an optional string parameter
# Variable name and the default value are positional (as in os.getenv()) but "var_type" and "optional"
# arguments are strictly keyword. "var_type" defaults to Optional[str] and "optional" defaults to False.
TEST_OPTIONAL_STR_VALUE: Optional[str] = getenv("TEST_OPTIONAL_STR_VALUE", optional=True)

# Get a mandatory string parameter (if unset raises VariableUnsetError)
# Note that although the default is set it will still raise an exception unless the "optional" argument is set to True
TEST_STR_VALUE: str = getenv("TEST_STR_VALUE", default="foo", var_type=str)

# Get an integer (can also be optional).
# If type conversion is not possible - raises TypeMismatchError
TEST_INT_VALUE: int = getenv("TEST_INT_VALUE", 42, var_type=int)

# Get a float (can also be optional)
TEST_FLOAT_VALUE: float = getenv("TEST_FLOAT_VALUE", 4.2, var_type=float)

# Get a bool value
# Strings "1", "yes", "true", "on" and "enable" will be interpreted as True
# Strings "0", "no", "false", "off" and "disable" will be interpreted as False
# Case doesn't matter. Other values will result in raise of UnprocessableValueError
TEST_BOOL_VALUE: bool = getenv("TEST_BOOL_VALUE", False, var_type=bool)
