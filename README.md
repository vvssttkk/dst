# data science template

in this repo u can look at default template for ds/ml/dl/.. projects or similar

## how to use

before creating a new project from this template, u need to install the dependencies

```bash
$ brew install -U cookiecutter
# or
$ pip install cookiecutter
```

go to the directory where u want to create your project and run

```bash
$ cookiecutter https://github.com/vtrokhymenko/dst
# or from cli.github.com
$ cookiecutter gh:vtrokhymenko/dst
```

## using the next project structure

```markdown
├── LICENSE
├── README.md                       <- the main readme
│
├── config                          <- often it's yaml-files with some parameters
│
├── data
│   ├── external                    <- data from third party sources
│   ├── interim                     <- intermediate data that has been transformed
│   ├── processed                   <- the final, canonical data sets for modeling
│   ├── raw                         <- the original, immutable data dump
│   └── features                    <- another
│
├── docs                            <- a default sphinx project (see sphinx-doc.org for details)
│
├── models                          <- trained & serialized models, model predictions, or model summaries
│
├── notebooks                       <- notebooks for research
│                                      naming convention is a number (for ordering), the creator's initials, and a short `-`
│                                      delimited description, eg `1.0-jqp-initial-data-exploration`
│
├── references                      <- data dictionaries, manuals, and all other explanatory materials
│
├── tests                           <- test for project
│
├── {{ cookiecutter.repo_name }}    <- source code
│   ├── __init__.py                 <- makes src a python module eg propose generate with `mkinit`)
│   │
│   ├── data                        <- scripts to download or generate data
│   │
│   ├── models                      <- scripts to train models and then use trained models to make predictions
│   │
│   └── visualization               <- scripts to create exploratory and results oriented visualizations
│
├── .gitignore                      <- default for python
│
├── .pre-commit-config.yaml         <- custom pcc with `isort`, `pre-commit-hooks`, `flake8` & `black`
│
└── requirements.txt                <- dependent libraries, eg propose generate with `pipreqs`
```

## another similar templates

* [cookiecutter](https://github.com/drivendata/cookiecutter-data-science)
  * [cdst](https://github.com/crplab/cdst/) by @crplab
  * [python-package-template](https://github.com/TezRomacH/python-package-template) by @TezRomacH
* [ocean](https://github.com/surfstudio/Ocean)
* [kedro](https://github.com/quantumblacklabs/kedro/)

## propose to use next tools

* [dvc](http://dvc.org) – open-source version control system for ds projects
* [hydra](https://hydra.cc) – to configuring complex applications
* [pre-commit](https://pre-commit.com) – framework for managing & maintaining multi-language pre-commit hooks
* spellcheckers
  * [vale](https://errata-ai.gitbook.io/vale/)
  * [pyspelling](https://facelessuser.github.io/pyspelling/)
  * [yaspeller](https://github.com/hcodes/yaspeller)
* coding style & review & formatter
  * [restyled](https://restyled.io)
  * [codefactor](https://www.codefactor.io)
  * [deepsource](https://deepsource.io)
  * [prettier](https://github.com/prettier/prettier)

## citation

```text
@misc{dst,
  author = {viktor trokhymenko},
  title = {data science template},
  year = {2020},
  publisher = {github},
  howpublished = {\url{https://github.com/vtrokhymenko/dst}}
}
```

## license

`dst` is mit licensed. see the [license](./LICENSE) file for details
