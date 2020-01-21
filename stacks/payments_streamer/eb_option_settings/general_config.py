from aws_cdk import (
    aws_elasticbeanstalk as _beanstalk
)

health_reporting_system_type = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:elasticbeanstalk:healthreporting:system",
    option_name='SystemType',
    value='enhanced'
)


def get_general_options():
    return [health_reporting_system_type]
