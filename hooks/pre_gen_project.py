import re
import sys


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

module_name = "{{ cookiecutter.module_name }}"

if not re.match(MODULE_REGEX, module_name):
    print(f"error: {module_name} is not a valid module name!")

    # exits with status 1 to indicate failure
    sys.exit(1)
