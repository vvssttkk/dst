# data science template

in this repo u can look at default template for ds/ml/dl/.. projects or similar

## how to use

* **before creating a new project from this template, u need to install the next dependencies**

  * [cookiecutter](https://github.com/cookiecutter/cookiecutter)

    ```bash
    brew install cookiecutter
    ```

    _or_

    ```bash
    pip install cookiecutter
    ```

  * [github cli](https://cli.github.com/manual/installation)

    * macos

      * install

        ```bash
        brew install gh
        ```
      * upgrade

        ```bash
        brew upgrade gh
        ```

    * linux

      look at the [linux installation instructions](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)

* **after go to the directory where u want to create your project and run**

  ```bash
  cookiecutter gh:vtrokhymenko/dst
  ```

* **follow the instruction**

## using the next project structure

```markdown
├── .github                       <- some actions
│   ├── workflows
│   │   └── ci.yml
│   └── dependabot.yml
│
├── LICENSE                       <- will be created if u choose
├── README.md                     <- the main readme
│
├── config                        <- often it's yaml-files with some parameters
│
├── data
│   ├── external                  <- data from third party sources
│   ├── interim                   <- intermediate data that has been transformed
│   ├── processed                 <- the final, canonical data sets for modeling
│   ├── raw                       <- the original, immutable data dump
│   ├── features                  <- another
│   └── README.md
│
├── docs                          <- a default sphinx project (see sphinx-doc.org for details)
│
├── experiments                   <- for any experiments
│   └── README.md
│
├── models                        <- trained & serialized models, model predictions, or model summaries
│   └── README.md
│
├── notebooks                     <- notebooks for research
│                                    naming convention is a number (for ordering), the creator's initials, and a short `-`
│                                    delimited description, eg `1.0-jqp-initial-data-exploration`
│
├── references                    <- data dictionaries, manuals, and all other explanatory materials
│   └── README.md
│
├── tests                         <- test for project
│
├── {{ cookiecutter.repo_name }}  <- source code
│   ├── __init__.py               <- makes src a python module eg propose generate with `mkinit`
│   │
│   ├── data                      <- scripts to download or generate data
│   │
│   ├── models                    <- scripts to train models and then use trained models to make predictions
│   │
│   └── visualization             <- scripts to create exploratory and results oriented visualizations
│
├── .gitignore                    <- default for python
│
└── .pre-commit-config.yaml       <- custom pcc with `reorder_python_imports`, `black`, `flake8`, `pre-commit-pyright`, `pre-commit-hooks`
```

----

## other similar templates

* [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science)
  * [cdst](https://github.com/crplab/cdst/) by @crplab
  * [python-package-template](https://github.com/TezRomacH/python-package-template) by @TezRomacH
* [ocean](https://github.com/surfstudio/Ocean)
* [kedro](https://github.com/quantumblacklabs/kedro/)

## propose to use next tools

* [gh](https://cli.github.com) – github on the terminal
* [dvc](https://dvc.org) – open-source version control system for ds projects
* [cml](https://cml.dev) – continuous machine learning | ci/cd for ml/dl
* [renovate](https://www.whitesourcesoftware.com/free-developer-tools/renovate/) - yet another dependency management
* [hydra](https://hydra.cc) – to configuring complex applications
* [pipreqs](https://github.com/bndr/pipreqs) – autogenerate pip requirements
* [pre-commit](https://pre-commit.com) – framework for managing & maintaining multi-language pre-commit hooks
* code style/review/formatter/typer
  * [codefactor](https://www.codefactor.io)
  * [snyk](https://snyk.io)
  * [deepsource](https://deepsource.io)
  * [prettier](https://github.com/prettier/prettier)
  * [pycodestyle](https://github.com/pycqa/pycodestyle/)
  * [pyre-check](https://github.com/facebook/pyre-check)
  * [pyright](https://github.com/microsoft/pyright)
  * [restyled](https://restyled.io) (autopep8, black, isort, prettier-markdown, reorder-python-imports, yapf)
  * [super-linter](https://github.com/github/super-linter) ([pylint](https://www.pylint.org/), [flake8](https://flake8.pycqa.org/en/latest/), [awesome-flake8-extensions](https://github.com/DmytroLitvinov/awesome-flake8-extensions), [black](https://github.com/psf/black))
  * [yapf](https://github.com/google/yapf)
  * [vulture](https://github.com/jendrikseipp/vulture)
* tests
  * [codecov](https://codecov.io)
  * [coveragepy](https://github.com/nedbat/coveragepy)
  * [pytest](https://docs.pytest.org/en/stable/) ([guide](https://stribny.name/blog/pytest/))
  * [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)
  * [mutmut](https://github.com/boxed/mutmut)
* profiler/debugger
  * [birdseye](https://github.com/alexmojaki/birdseye)
  * [heartrate](https://github.com/alexmojaki/heartrate)
  * [palanteer](https://github.com/dfeneyrou/palanteer)
  * [py-spy](https://github.com/benfred/py-spy)
  * [pyheat](https://github.com/csurfer/pyheat)
  * [snoop](https://github.com/alexmojaki/snoop)
  * [viztracer](https://github.com/gaogaotiantian/viztracer)
* spellcheckers
  * [yaspeller](https://github.com/hcodes/yaspeller)
  * [pyspelling](https://facelessuser.github.io/pyspelling/)
  * [vale](https://github.com/errata-ai/vale)

## citation

```citation
@misc{dst,
  author = {trokhymenko viktor},
  title = {data science template},
  year = {2020},
  publisher = {github},
  howpublished = {\url{https://github.com/vtrokhymenko/dst}}
}
```