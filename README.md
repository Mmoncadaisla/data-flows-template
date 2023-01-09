# Data flows

This repository holds the flows and deployments for the data pipelines that are built using [Prefect](https://www.prefect.io/) using Prefect Cloud and Google Cloud Platform setup based on [this resource](https://github.com/anna-geller/prefect-cloud-gcp).

Please find more information around how Prefect works in the [Prefect documentation](https://docs.prefect.io/).

>**NOTE**: For first time setup, please follow the [initial setup guide](docs/INITIAL_SETUP.md).

The repository is structured as follows:

- `dataflows` - Python package that contains the flows and deployments for the data pipelines
  - `flows` - Python module that contains the [flows](https://docs.prefect.io/concepts/flows/) for the data pipelines
  - `deployments` - Python module that has the [deployment definition](https://docs.prefect.io/concepts/deployments/) files
- `setup.py` - Python `dataflows` package setup file
- `tests` - Python tests for the flows. Uses `pytest`, tests are ran using `tox` as part of the CI/CD pipeline.
- `docs` - Documentation for the repository

CI/CD pipeline:

- `.github/actions` - GitHub Actions for running the CI/CD pipeline
- `.github/workflows` - GitHub Actions workflows for running the CI/CD pipeline
- `deployments.py` - Python script that contains the logic for deploying the flows and deployments used by the CI/CD pipeline

Infrastructure:

- `Dockerfile` - *Dockerfile* for the Prefect Agent
- `requirements.txt` - Python requirements for the Prefect Agent applied via `Dockerfile`

Other files of interest:

- `docs` - Documentation for the repository
- `docker-compose.yml` - Docker Compose file that contains the services for running Prefect Cloud, Prefect Orion, and Prefect Agent, as well as a CLI container for running flows locally

```
.
├── Dockerfile
├── README.md
├── dataflows
│   ├── __init__.py
│   ├── deployments
│   │   ├── __init__.py
│   │   ├── _constants.py
│   │   └── hello_deployment.py
│   └── flows
│       ├── __init__.py
│       └── hello_flow.py
├── deployments.py
├── docker-compose.yml
├── docs
│   ├── INITIAL_SETUP.md
│   ├── LOCAL_DEVELOPMENT.md
│   ├── assets
│   │   └── setup_logs
│   └── img
├── requirements.txt
├── setup.py
├── tests
│   ├── README.md
│   ├── conftest.py
│   └── unit
│       ├── __init__.py
│       └── flows
│           ├── __init__.py
│           └── test_hello_flow.py
└── tox.ini
```

## Contributing

Please see the [contributing guidelines](docs/CONTRIBUTING.md) for more information.
