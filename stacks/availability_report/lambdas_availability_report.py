from aws_cdk import (
    aws_lambda as _lambda,
    aws_dynamodb as _dynamo_db,
    core,
)


class AvailabilityReportsStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # TODO: lambda (checker and requester)
        # Checker
        lambda_av_checker = _lambda.Function(
            self,
            id="lambda_availability_checker",
            function_name='lambda_availability_checker',
            code=_lambda.Code.asset("lambda_availability_report_checker_asset"),
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler="index.lambda_handler"
        )

        # TODO: DynamoDB Table
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
