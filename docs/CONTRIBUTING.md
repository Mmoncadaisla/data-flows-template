# Contributing guidelines

## Overview

This repository contains the flows and deployments for the data pipelines. The flows are written in Python using the Prefect 2 library.

In order to contribute to this repository, you will need to have a basic understanding of the Prefect library and how it works. Please find more information around how Prefect works in the [Prefect documentation](https://docs.prefect.io/).

## Steps to contribute

1. Clone the repository using git

    ```bash
    git clone https://github.com/Mmoncadaisla/data-flows.git
    ```

2. Set up your local environment using docker-compose (see [Getting started with local Development](LOCAL_DEVELOPMENT.md#getting-started))

3. Create a new branch from the `development` branch (e.g. `YourUsername/feature/my-new-feature`)

    ```bash
    git checkout -b YourUsername/feature/my-new-feature
    ```

4. Create your flow in the `dataflow` package and run it locally (see [Running flows locally](LOCAL_DEVELOPMENT.md#running-flows-locally-with-the-prefect-cli))

    >NOTE: If your flow requires a new dependency, add it to the `setup.py` file, requirements will be automatically added to the `runner` and `agent` containers.

5. Once you are happy with your flow, make sure you add unit tests for it within the `tests` directory (tests are designed using `pytest`, please see [Testing](../tests/README.md) for reference)

6. If desired, add a deployment definition file to the `deployments` module (e.g: `flow_name_deployment.py`). It is recommended to use parameters to have a separate deployment for production and staging environments. For example (find the full example [here](../dataflows/deployments/hello_deployment.py)):

    ```python
    def deploy_hello_flow():
        deployment = Deployment.build_from_flow(
            flow=hello_flow,
            name="hello_flow_deployment",
            work_queue_name="default",
            storage=storage,
            path="hello_flow",
            tags=["staging"],
            infrastructure=infrastructure,
            schedule=CronSchedule(cron="0 12 1 * *", timezone="UTC"),
        )
        deployment.apply()
    ```

    The files to be committed at this point would be:

    ```bash
    ❯ git status
    On branch Mmoncadaisla/add-new-flow
    Untracked files:
    (use "git add <file>..." to include in what will be committed)
        dataflows/deployments/new_deployment.py
        dataflows/flows/new_flow.py
        tests/unit/flows/test_new_flow.py

    nothing added to commit but untracked files present (use "git add" to track)
    ```

7. If you have added a deployment definition file to the `deployments` module, add it to the `deployments._constants` module so that the CI can deploy your flow automatically upon flow/deployment file changes.

   ```python
    from dataflows.deployments.hello_deployment import deploy_hello_flow
    from dataflows.deployments.my_new_deployment import deploy_new_flow

    FLOW_DEPLOYMENT_DICT = flow_deployment_dict = {
        "hello_flow": deploy_hello_flow,
        "new_flow": deploy_new_flow
    }

    DEPLOYMENT_FILE_FUNC_DICT = {
        "hello_deployment": deploy_hello_flow,
        "new_deployment": deploy_new_flow
    }
   ```

    The files to be committed after modifying `_constants.py`:

    ```bash
    ❯ git status
    On branch Mmoncadaisla/add-new-flow
    Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git restore <file>..." to discard changes in working directory)
        modified:   dataflows/deployments/_constants.py

    Untracked files:
    (use "git add <file>..." to include in what will be committed)
        dataflows/deployments/new_deployment.py
        dataflows/flows/new_flow.py
        tests/unit/flows/test_new_flow.py

    no changes added to commit (use "git add" and/or "git commit -a")
    ```

    ```bash
    git add --all
    git commit -m "Add new flow"
    git push --set-upstream origin Mmoncadaisla/add-new-flow
    ```

    After the changes are pushed, the CI will run the unit tests and the linter. If the tests pass, you can create a pull request against the `development` branch.

    ![CI](/docs/img/CI_push.png)

8. Open a pull request against the `development` branch and add at least one reviewer. When the PR is created, the CI will run the unit tests and the linter.

    ![PR](/docs/img/PR_staging.png)

    ![PR_checks](/docs/img/pr_checks.png)

9. After tests have passed and the PR has been approved, merge the PR into the `development` branch and delete your branch. If a deployment file has been created, and the proper references were added to the `_constants` module, it will automatically deploy your flow to Prefect Cloud!

    You can check this from the GitHub actions tab.

    ![Deployment](/docs/img/flow_deployment.png)

10. Congratulations! You have successfully contributed to the data pipelines! 🚀
