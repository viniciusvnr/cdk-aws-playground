from aws_cdk import (
    aws_elasticbeanstalk as _beanstalk
)

deployment_policy = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:elasticbeanstalk:command",
    option_name='DeploymentPolicy',
    value='Rolling'  # TODO: change to immutable
)


def get_deployment_policy():
    return [deployment_policy]
