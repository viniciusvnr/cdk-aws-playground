from aws_cdk import (
    aws_lambda as _lambda,
    core,
)


class LambdaNewRelicDeploymentStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        lambda_deploy_marker = _lambda.Function(
            self,
            id="lambda_newrelic_deploy_marker",
            function_name='lambda_newrelic_deploy_marker',
            code=_lambda.Code.asset("lambda_new_relic_deployment_mark_asset"),
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler="index.lambda_handler"
        )
        # TODO: Add IAM Policy to allow code pipeline Put/job Results (failure and success)
