from aws_cdk import (
    aws_elasticbeanstalk as _beanstalk,
    core,
)
from .eb_option_settings import get_config_list


class PaymentsStreamerStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        beanstalk_application = _beanstalk.CfnApplication(
            self, id='PaymentsStreamer-eb', application_name='Payments-Streamer',
            description='Payments Streamer Beanstalk'
        )

        eb_tier = _beanstalk.CfnEnvironment.TierProperty(name='WebServer', type='Standard')
        eb_env_option_settings = get_config_list()

        eb_staging_environment = _beanstalk.CfnEnvironment(
            self, id='Payments-streamer-Staging', application_name=beanstalk_application.application_name,
            solution_stack_name='64bit Amazon Linux 2018.03 v2.10.1 running Java 8',
            environment_name='PaymentsStreamer-Staging',
            cname_prefix='Payments-streamer-Staging',
            tier=eb_tier,
            option_settings=eb_env_option_settings
        )
