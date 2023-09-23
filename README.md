# Typed getenv

A simple package for minimalistic environment-based configurations. No dependencies required.

---

## What this module is for

As microservices become more and more popular there's a need for environment based configuration.

**Why not use a config ini/YAML/JSON/etc. file?** Microservices are mostly run in containers. Sometimes you might not
have access to the host environment to build containers yourself with filled config files embedded into them or mount
files into the container. The most logical option then is to provide a prebuilt container image and a set of environment
variables that define it's behaviour.

**Why not use standard `os.getenv()`?** Getenv is mostly for storing strings, however configurations often need to
include integers, floats and logical values. Getenv would require some very trivial custom logic to be rewritten over
and over again to convert strings into the desired types of values and validate them. This library provides this code.

**Why create a new package?** Indeed there are already solutions to the problems listed above.
[environ-config](https://pypi.org/project/environ-config/) and [Pydantic](https://pypi.org/project/pydantic/) are nice
tools that would be great for that job, but they're clearly an overkill for the task when you have a lightweight
microservice application with only a few environment variables to parse. This package on the other hand has **no
dependencies** and provides global access to the needed variables across all your application **no initialization and
configuration required**.

## Installation

To acquire the module head over to the terminal and install the module using your favourite package manager e.g.
`pip instal typed_getenv` or `poetry add typed_getenv`.

## Usage

Typed getenv has a very simple interface that is pretty much just a wrapper over standard `os.getenv()` with a couple
additional arguments and some custom exceptions.

This example demonstrates the usage of the module.

```python
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
```

## Contributing

If you want to contribute to the development - file an issue or create a pull request on the GitHub page for this
module.
