from aws_cdk import (
    aws_lambda as _lambda,
    aws_sns as _sns,
    aws_events as _events,
    aws_events_targets as _targets,
    aws_sns_subscriptions as _sns_subscription,
    core,
)


class LambdaPipelineAlertsStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create lambda function
        lambda_pipeline_alerts = _lambda.Function(
            self,
            id="lambda_pipeline_alerts_asset",
            function_name='lambda_pipeline_alerts_asset',
            code=_lambda.Code.asset("lambda_pipeline_alerts_asset"),
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler="index.lambda_handler"
        )
        # add Env Vars
        lambda_pipeline_alerts.add_environment(
            'SLACK_WEB_HOOK_URL',
            'https://hooks.slack.com/services/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'
        )
        lambda_pipeline_alerts.add_environment('SLACK_CHANNEL', '#tech-pay-deploys')

        # Create sns topic for the pipeline events
        sns_topic_pipeline_alerts = _sns.Topic(self, id='sns_pipeline_alerts', display_name='pipelines-events',
                                               topic_name='pipelines-events')
        # add lambda to sns subscription
        sns_topic_pipeline_alerts.add_subscription(_sns_subscription.LambdaSubscription(lambda_pipeline_alerts))

        # Create the event rule
        event_rule = _events.Rule(
            self, id='pipeline_alerts',
            rule_name='pipeline_alerts',
            description='Cloud Watch Event Rule to check pipeline events'
        )

        # Cloud watch event configuration
        event_source = ["aws.codepipeline"]
        event_detail_type = ["CodePipeline Pipeline Execution State Change"]
        event_detail = {
            "state": [
                "FAILED"
            ]
        }

        # add event pattern to send to target
        event_rule.add_event_pattern(detail=event_detail, detail_type=event_detail_type, source=event_source)

        # add target
        pipeline_name = _events.EventField.from_path('$.detail.pipeline')

        event_rule.add_target(
            _targets.SnsTopic(
                sns_topic_pipeline_alerts,
                message=_events.RuleTargetInput.from_text(
                    f':rotating_light:The Pipeline `{pipeline_name}` has failed.:rotating_light:')))
