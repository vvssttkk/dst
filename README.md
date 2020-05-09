# data science project generation

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
# or
$ cookiecutter gh:vtrokhymenko/dst
```

`gh` - it's github on the command linets [github cli](https://cli.github.com/manual/)

```bash
brew install github/gh/gh
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
* coding style & review & formatter
  * [restyled](https://restyled.io)
  * [codefactor](https://www.codefactor.io)
  * [deepsource](https://deepsource.io)
  * [prettier](https://github.com/prettier/prettier)
  * [vale](https://errata-ai.gitbook.io/vale/)
