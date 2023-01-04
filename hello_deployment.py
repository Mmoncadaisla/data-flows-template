from prefect.deployments import Deployment
from prefect.blocks.core import Block
from prefect.orion.schemas.schedules import CronSchedule
from dataflows.flows.hello_flow import hello

storage = Block.load("gcs/default")
infrastructure = Block.load("cloud-run-job/default")


def deploy_hello_flow():
    deployment = Deployment.build_from_flow(
        flow=hello,
        name="hello_flow_deployment",
        work_queue_name="default",
        storage=storage,
        path="hello",
        infrastructure=infrastructure,
        schedule=CronSchedule(cron="* * * * *", timezone="UTC"),
    )
    deployment.apply()


if __name__ == "__main__":
    deploy_hello_flow()
