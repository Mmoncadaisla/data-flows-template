import os
import logging
import argparse
from dataflows.deployments._constants import FLOW_DEPLOYMENT_DICT


def get_file_name_file_extension(file_path: str) -> tuple:
    """Function to extract the file name and extension from a file URI
    Args:
        file_uri (str): URL pointing to the file
    Returns:
        tuple: file name and extension
    """
    file_name_with_ext = os.path.basename(file_path)
    file_name, file_ext = os.path.splitext(file_name_with_ext)
    return file_name, file_ext


def get_deploy_function(flow_file_name: str) -> callable:
    """Function to get the deployment function for a flow

    Args:
        flow (str): flow file name without extension

    Returns:
        callable: deployment function
    """
    return FLOW_DEPLOYMENT_DICT.get(flow_file_name)


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

    flow_file_name, _ = get_file_name_file_extension(args.file_path)

    deploy_function = get_deploy_function(flow_file_name)

    if deploy_function:
        logger.info(f"Deploying {flow_file_name}...")
        deploy_function()
        logger.info(f"Flow {flow_file_name} has been deployed!")
    else:
        logger.info(
            f"No deployment function found for {flow_file_name},"
            "skipping..."
        )
