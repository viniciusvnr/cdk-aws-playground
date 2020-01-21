from aws_cdk import core
from stacks.lambda_new_relic_deployment_marker import LambdaNewRelicDeploymentStack
from stacks.lambda_pipeline_alerts import LambdaPipelineAlertsStack
from stacks.payments_streamer.stack_infra_payments_streamer import PaymentsStreamerStack
from stacks.availability_report.lambdas_availability_report import AvailabilityReportsStack


app = core.App()

CdkAwsPlaygroundStack(app, "cdk-aws-playground")

LambdaNewRelicDeploymentStack(
    app, "Lambda-New-Relic-Deployment-Marker-Stack", env={'region': 'us-east-1'},
    tags={'ManageBy': 'payops-cdk'},
    description='CDK Stack: LambdaFn to mark deployments on new relic APM for a specified application'
)

LambdaPipelineAlertsStack(
    app, "Lambda-Pipeline-Alerts-Stack", env={'region': 'us-east-1'},
    tags={'ManageBy': 'payops-cdk'},
    description='CDK Stack: LambdaFn to alert if any CodePipeline Pipeline Execution State Change to Failed.'
)

PaymentsStreamerStack(
    app, 'Payments-Streamer-Infra-Stack', env={'region': 'us-east-1'},
    tags={'ManageBy': 'payops-cdk'},
    description='CDK Stack: Payments Streamer Application Infrastructure'
)

AvailabilityReportsStack(
    app, 'AvailabilityReports-Stack', env={'region': 'us-east-1'},
    tags={'ManageBy': 'payops-cdk'},
    description='CDK Stack: Get application status for generating Availability reports'
)

app.synth()
