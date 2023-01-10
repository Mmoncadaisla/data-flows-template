from dataflows.deployments.hello_deployment import deploy_hello_flow
from dataflows.deployments.new_deployment import deploy_new_flow

FLOW_DEPLOYMENT_DICT = flow_deployment_dict = {
    "hello_flow": deploy_hello_flow,
    "new_flow": deploy_new_flow,
}

DEPLOYMENT_FILE_FUNC_DICT = {
    "hello_deployment": deploy_hello_flow,
    "new_deployment": deploy_new_flow,
}
