# Data flows

This repository holds the flows and deployments for the data pipelines that are built using [Prefect](https://www.prefect.io/) using Prefect Cloud and Google Cloud Platform setup based on [this resource](https://github.com/anna-geller/prefect-cloud-gcp).

## Main components

This setup is based on Prefect Cloud & Google Cloud Platform services. The main components are:

- Prefect Cloud
- [Prefect Agent](https://docs.prefect.io/concepts/work-queues/#agent-overview) (via Google Compute Engine): The agent is responsible for deploying the flow runs to the Prefect Cloud
- Prefect Runner (via [Google Cloud Run](https://cloud.google.com/run)): Serverless service responsible for processing the flows

Please find more information around how Prefect works in the [Prefect documentation](https://docs.prefect.io/).

## Initial setup

Please see the [initial setup guide](docs/INITIAL_SETUP.md) for more information if this is the first time you're spinning up the repository's associated infrastructure.

## Repository structure

The repository contains the following main folders:

- `dataflows` - Python package that contains the flows and deployments for the data pipelines
  - `flows` - Python module that contains the [flows](https://docs.prefect.io/concepts/flows/) for the data pipelines
  - `deployments` - Python module that has the [deployment definition](https://docs.prefect.io/concepts/deployments/) files
- `tests` - Python tests for the flows. Uses `pytest`, tests are ran using `tox` as part of the CI/CD

```
.
├── README.md
├── config
│   ├── agent
│   │   └── Dockerfile
│   └── runner
│       └── Dockerfile
├── dataflows
│   ├── __init__.py
│   ├── _version.py
│   ├── deployments
│   │   ├── __init__.py
│   │   ├── _constants.py
│   │   └── hello_deployment.py
│   └── flows
│       ├── __init__.py
│       ├── hello_flow.py
│       └── utils
├── deployments.py
├── docker-compose.yml
├── docs
│   ├── CONTRIBUTING.md
│   ├── INITIAL_SETUP.md
│   ├── LOCAL_DEVELOPMENT.md
│   ├── assets
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
