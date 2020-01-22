from aws_cdk import (
    aws_lambda as _lambda,
    aws_dynamodb as _dynamo_db,
    aws_events as _events,
    aws_events_targets as _targets,
    aws_iam as _iam,
    core,
)


class AvailabilityReportsStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        table_partition_key = _dynamo_db.Attribute(
            name='id',
            type=_dynamo_db.AttributeType.STRING
        )

        availability_report_table = _dynamo_db.Table(
            self,
            id='availabilityReportSTable',
            table_name='AvailabilityReports',
            partition_key=table_partition_key,
            billing_mode=_dynamo_db.BillingMode.PROVISIONED,
            read_capacity=1,
            write_capacity=1
        )

        # Lambda to call application health endpoints
        lambda_av_checker = _lambda.Function(
            self,
            id="lambda_availability_checker",
            function_name='lambda_availability_checker',
            code=_lambda.Code.asset("lambda_availability_report_checker_asset"),
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler="index.lambda_handler"
        )
        # grant dynamo db write permission to lambda
        availability_report_table.grant_write_data(lambda_av_checker)

        # Lambda to call checker lambda
        lambda_av_requester = _lambda.Function(
            self,
            id="lambda_availability_requester",
            function_name='lambda_availability_requester',
            code=_lambda.Code.asset("lambda_availability_report_requester_asset"),
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler="index.lambda_handler"
        )
        # grant invoke permission to downstream lambda
        lambda_av_checker.grant_invoke(lambda_av_requester)

        event_rule = _events.Rule(
            self, id='lambda_availability_requester_schedule',
            rule_name='lambda_availability_requester_schedule',
            schedule=_events.Schedule.cron(),
            description='Cloud Watch Event Rule to schedule availability requester lambda'
        )
        event_rule.add_target(_targets.LambdaFunction(lambda_av_requester))
