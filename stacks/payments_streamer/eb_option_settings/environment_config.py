from aws_cdk import (
    aws_elasticbeanstalk as _beanstalk
)

environment_system_type = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:elasticbeanstalk:environment",
    option_name='EnvironmentType',
    value='LoadBalanced'
)

environment_load_balancer_type = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:elasticbeanstalk:environment",
    option_name='LoadBalancerType',
    value='application'
)

environment_service_role = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:elasticbeanstalk:environment",
    option_name='ServiceRole',
    value='arn:aws:iam::505047608760:role/aws-elasticbeanstalk-service-role'
)


def get_environment_policy():
    return [environment_system_type, environment_load_balancer_type, environment_service_role]
