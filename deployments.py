import os
import logging
import argparse
from dataflows.deployments._constants import (
    FLOW_DEPLOYMENT_DICT,
    DEPLOYMENT_FILE_FUNC_DICT,
)


def get_file_name_file_extension(file_path: str) -> tuple:
    """Function to extract the file name and extension from a file URI
    Args:
        file_uri (str): URL pointing to the file
    Returns:
        tuple: file name and extension
    """
    file_name_with_ext = os.path.basename(file_path)
    file_name, file_ext = os.path.splitext(file_name_with_ext)
    return (file_name, file_ext)


def get_deploy_function(file_name: str) -> callable:
    """Function to get the deployment function for a flow

    Args:
        flow (str): flow file name without extension

    Returns:
        callable: deployment function
    """
    deploy_function = FLOW_DEPLOYMENT_DICT.get(file_name)

    if not deploy_function:
        deploy_function = DEPLOYMENT_FILE_FUNC_DICT.get(file_name)
    return deploy_function


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "-f",
        "--file_path",
        help="File path",
        required=True,
    )

    args = parser.parse_args()
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    file_name, _ = get_file_name_file_extension(args.file_path)

    deploy_function = get_deploy_function(file_name)

    if deploy_function:
        logger.info(f"Deploying {file_name} using {deploy_function.__name__}")
        deploy_function()
        logger.info(f"{file_name} has been deployed!")
    else:
        logger.info(
            f"No deployment function found for {file_name},"
            "skipping..."
        )
