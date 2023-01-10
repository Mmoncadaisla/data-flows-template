from dataflows.deployments.hello_deployment import deploy_hello_flow

FLOW_DEPLOYMENT_DICT = flow_deployment_dict = {
    "hello_flow": deploy_hello_flow,
}

DEPLOYMENT_FILE_FUNC_DICT = {
    "hello_deployment": deploy_hello_flow,
}
