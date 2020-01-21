from aws_cdk import (
    aws_elasticbeanstalk as _beanstalk
)

asg_min_size = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:autoscaling:asg",
    option_name='MinSize',
    value='1'
)
asg_max_size = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:autoscaling:asg",
    option_name='MaxSize',
    value='4'
)


def get_asg_options():
    return [asg_min_size, asg_max_size]
