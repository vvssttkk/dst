# {{ cookiecutter.project_name }}

source code for use in this project

----
examples structure:

```
{{ cookiecutter.repo_name }}
├── __init__.py           <- makes src a python module
│
├── data                  <- scripts to download or generate data
│   └── make_dataset.py
│
├── features              <- scripts to turn raw data into features for modeling
│   └── build_features.py
│
├── models                <- scripts to train models and then use trained models to make predictions
│   ├── predict_model.py
│   └── train_model.py
│
├── visualization         <- scripts to create exploratory and results oriented visualizations
│   └── visualize.py
│
└── README.md
```
