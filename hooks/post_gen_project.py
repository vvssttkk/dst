"""this module is called after project is created"""

import os
import textwrap
from pathlib import Path

# get the root project directory:
PROJECT_DIRECTORY = Path.cwd().absolute()
PROJECT_NAME = "{{ cookiecutter.project_name }}"

# generate correct license:
LICENSE = "{{ cookiecutter.license }}"
ORGANIZATION = "{{ cookiecutter.github_username }}"

# generate github repository:
GITHUB_USER = "{{ cookiecutter.github_username }}"


def generate_license() -> None:
    """generates license file for the project"""
    license_result = os.system(f"lice {LICENSE} -o '{ORGANIZATION}' -p {PROJECT_NAME} > {PROJECT_DIRECTORY}/LICENSE")
    if license_result:  # it means that return code is not 0, print exception
        print(license_result)


def print_futher_instuctions() -> None:
    """shows user what to do next after project creation."""
    message = f"""
    your project `{PROJECT_NAME}` is created.

    [0] now u can start working on it:

        $ cd {PROJECT_NAME} && git init

    [1] upload initial code to github (ensure you've run `make install` to use `pre-commit`):

        $ git add .git
        $ git add ./
        $ git commit -m "initial commit"
        $ git remote add origin https://github.com/{GITHUB_USER}/{PROJECT_NAME}.git
        $ git push -u origin master
    """
    print(textwrap.dedent(message))


generate_license()
print_futher_instuctions()
