# data science template

in this repo can look at default template for ds/ml/dl/.. projects or similar

## how run

* **before creating a new project from this template, need to install the next dependencies**

  * https://github.com/cookiecutter/cookiecutter

    ```bash
    pip install cookiecutter
    ```

   * https://cli.github.com

     look at the installation instructions - https://github.com/cli/cli?tab=readme-ov-file#installation

* **after go to the directory where want to create your project and run**

  ```bash
  cookiecutter gh:vvssttkk/dst
  ```

* **follow the instruction**

## using the next project structure

```markdown
├── .github/                           <- some actions
│   ├── workflows/  
│   │   ├── ci.yml  
│   │   └── dependency-review.yml  
│   └── dependabot.yml  
│  
├── config/                            <- often it's yaml-files with some parameters
│  
├── data/  
│   ├── external/                      <- data from third party sources
│   ├── interim/                       <- intermediate data that has been transformed
│   ├── processed/                     <- the final, canonical data sets for modeling
│   ├── raw/                           <- the original, immutable data dump
│   ├── features/                      <- another
│   └── README.md  
│  
├── docs/                              <- a default sphinx project (see sphinx-doc.org for details)
│  
├── experiments/                       <- for any experiments
│   └── README.md  
│  
├── models/                            <- trained & serialized models, model predictions, or model summaries
│   └── README.md  
│  
├── notebooks/                         <- notebooks for research naming convention is a number (for ordering), the creator's initials,
│                                         and a short `-` delimited description, eg `1.0-jqp-initial-data-exploration`
│  
├── references/                        <- data dictionaries, manuals, and all other explanatory materials
│   └── README.md  
│  
├── tests/                             <- test for project
│   └── __init__.py
│  
├── {{ cookiecutter.project_name }}/   <- source code
│   ├── __init__.py                    <- propose generate with `mkinit`
│   ├── data/                          <- scripts to download or generate data
│   ├── models/                        <- scripts to train models and then use trained models to make predictions
│   └── visualization/                 <- scripts to create exploratory and results oriented visualizations
│  
├── .gitignore                         <- default for python
├── .pre-commit-config.yaml            <- custom pcc with `reorder_python_imports`, `black`, `flake8`, `pyright`, `mypy`, `pre-commit-hooks`..  
├── LICENSE                            <- will be created if u choose
├── README.md
└── requirements.txt                   <- propose generate with `pipreqs`
```

## other similar templates

* https://github.com/drivendata/cookiecutter-data-science
* https://github.com/quantumblacklabs/kedro
