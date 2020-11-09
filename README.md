# data science template

in this repo u can look at default template for ds/ml/dl/.. projects or similar

## how to use

**[0]** before creating a new project from this template, u need to install the next dependencies

* [cookiecutter](https://github.com/cookiecutter/cookiecutter)

  ```bash
  $ brew install cookiecutter
  # or
  $ pip install cookiecutter
  ```

* [github cli](https://cli.github.com/manual/installation)

  * mac os

    ```bash
    # install
    $ brew install gh

    # upgrade
    $ brew upgrade gh
    ```

  * linux

    see [linux installation instructions](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)

**[1]** after go to the directory where u want to create your project and run

```bash
cookiecutter gh:vtrokhymenko/dst
```

## using the next project structure

```markdown
├── .github
│   ├── workflows
│   │   ├── pre-commit.yml
│   │   └── vale.yml
│   └── dependabot.yml
│
├── LICENSE                         <- will be created if u choose
├── README.md                       <- the main readme
│
├── config                          <- often it's yaml-files with some parameters
│
├── data
│   ├── external                    <- data from third party sources
│   ├── interim                     <- intermediate data that has been transformed
│   ├── processed                   <- the final, canonical data sets for modeling
│   ├── raw                         <- the original, immutable data dump
│   ├── features                    <- another
│   └── README.md
│
├── docs                            <- a default sphinx project (see sphinx-doc.org for details)
│
├── experiments                     <- for any experiments
│   └── README.md
│
├── models                          <- trained & serialized models, model predictions, or model summaries
│   └── README.md
│
├── notebooks                       <- notebooks for research
│                                      naming convention is a number (for ordering), the creator's initials, and a short `-`
│                                      delimited description, eg `1.0-jqp-initial-data-exploration`
│
├── references                      <- data dictionaries, manuals, and all other explanatory materials
│   └── README.md
│
├── tests                           <- test for project
│
├── {{ cookiecutter.repo_name }}    <- source code
│   ├── __init__.py                 <- makes src a python module eg propose generate with `mkinit`
│   │
│   ├── data                        <- scripts to download or generate data
│   │
│   ├── models                      <- scripts to train models and then use trained models to make predictions
│   │
│   └── visualization               <- scripts to create exploratory and results oriented visualizations
│
├── .gitignore                      <- default for python
│
└── .pre-commit-config.yaml         <- custom pcc with `reorder_python_imports`, `black`, `flake8`, `pre-commit-pyright`, `pre-commit-hooks`
```

----

## another similar templates

* [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science)
  * [cdst](https://github.com/crplab/cdst/) by @crplab
  * [python-package-template](https://github.com/TezRomacH/python-package-template) by @TezRomacH
* [ocean](https://github.com/surfstudio/Ocean)
* [kedro](https://github.com/quantumblacklabs/kedro/)

## propose to use next tools

* [dvc](https://dvc.org) – open-source version control system for ds projects
* [cml](https://cml.dev) – continuous machine learning | ci/cd for ml/dl
* [hydra](https://hydra.cc) – to configuring complex applications
* [dependabot](https://dependabot.com) – automated dependency updates
* [act](https://github.com/nektos/act) – run github actions locally
* [pre-commit](https://pre-commit.com) – framework for managing & maintaining multi-language pre-commit hooks
* coding style/review/formatter/typer
  * [codefactor](https://www.codefactor.io)
  * [deepsource](https://deepsource.io)
  * [prettier](https://github.com/prettier/prettier)
  * [pyright](https://github.com/microsoft/pyright)
  * [super-linter](https://github.com/github/super-linter) ([pylint](https://www.pylint.org/), [flake8](https://flake8.pycqa.org/en/latest/), [black](https://github.com/psf/black))
  * [restyled](https://restyled.io) (autopep8, black, isort, prettier-markdown, reorder-python-imports, yapf
* tests
  * [codecov](https://codecov.io)
* spellcheckers
  * [vale](https://errata-ai.gitbook.io/vale/)
  * [pyspelling](https://facelessuser.github.io/pyspelling/)
  * [yaspeller](https://github.com/hcodes/yaspeller)

## citation

```citation
@misc{dst,
  author = {viktor trokhymenko},
  title = {data science template},
  year = {2020},
  publisher = {github},
  howpublished = {\url{https://github.com/vtrokhymenko/dst}}
}
```

## license

this project licensed under the terms of the `mit` license. see the [license](./LICENSE) file for details
