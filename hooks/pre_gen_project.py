import re
import sys
from typing import Callable
from typing import List


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
project_name = "{{ cookiecutter.project_name }}"


def validate_project_name() -> None:
    """this validator is used to ensure that `project_name` is valid

    valid inputs starts with the lowercase letter
    followed by any lowercase letters, numbers or underscores

    raises
        valueerror: if module_name is not a valid project name
    """

    if not re.match(MODULE_REGEX, project_name):
        message = f"error: the project name `{project_name}` is not a valid project name"

        raise ValueError(message)


validators: List[Callable[[], None]] = [validate_project_name]

for validator in validators:
    try:
        validator()
    except ValueError as ex_value_error:
        print(ex_value_error)
        sys.exit(1)
