# Contributing guidelines

## Overview

## Steps to contribute

1. Clone the repository
2. Set up your local environment (see [Getting started with local Development](LOCAL_DEVELOPMENT.md#getting-started))
3. Create a new branch from the `development` branch (e.g. `Mmoncadaisla/feature/my-new-feature`)
4. Create your flow in the `dataflow` package and run it locally (see [Running flows locally](LOCAL_DEVELOPMENT.md#running-flows-locally-with-the-prefect-cli))
    >NOTE: If your flow requires a new dependency, add it to the `requirements.txt` file
5. Once you are happy with your flow, make sure you add unit tests for it within the `tests` directory (see [Testing](../tests/README.md))
6. If desired, add a deployment definition file to the `deployments` module (e.g: `flow_name_deployment.py`). It is recommended to use parameters to have a separate deployment for production and staging environments.
7. If you have added a deployment definition file to the `deployments` module, add it to the `deployments._constants` module so that the CI can deploy your flow automatically upon flow/deployment file changes.
8. Open a pull request towards the `development` branch and add at least one reviewer. When the PR is created, the CI will run the unit tests and the linter.
9. After tests have passed and the PR has been approved, merge the PR into the `development` branch. If The CI will automatically deploy your flow to Prefect Cloud.

## Troubleshooting