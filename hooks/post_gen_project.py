import os
import textwrap
from pathlib import Path


# get the root project directory
PROJECT_DIRECTORY = Path.cwd().absolute()
REPO_NAME = "{{ cookiecutter.repo_name }}"

# generate correct license
LICENSE = "{{ cookiecutter.license }}"
ORGANIZATION = "{{ cookiecutter.github_username }}"


def generate_license() -> None:
    """generates license file for the project"""

    license_result = os.system(f"lice {LICENSE} -o '{ORGANIZATION}' -p {REPO_NAME} > {PROJECT_DIRECTORY}/LICENSE")
    if license_result:  # it means that return code is not 0, print exception
        print(license_result)


def print_futher_instuctions() -> None:
    """shows user what to do next after project creation."""

    message = f"""
    your project `{REPO_NAME}` is created

    [0] init & crete repo

        $ cd {REPO_NAME} && git init
        $ gh repo create
            choose "Push an existing local repository to GitHub"

    [1] upload template to github

        $ git add ./ && git commit -m "initial commit"
        $ git push --set-upstream origin master
    """
    print(textwrap.dedent(message))


if LICENSE != "not open source":
    generate_license()
print_futher_instuctions()
