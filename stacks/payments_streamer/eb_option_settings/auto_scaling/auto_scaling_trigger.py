from aws_cdk import (
    aws_elasticbeanstalk as _beanstalk
)

trigger_measure_name = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:autoscaling:trigger",
    option_name='MeasureName',
    value='CPUUtilization'
)

trigger_unit = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:autoscaling:trigger",
    option_name='Unit',
    value='Percent'
)

trigger_upper_threshold = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:autoscaling:trigger",
    option_name='UpperThreshold',
    value='60'
)

trigger_lower_threshold = _beanstalk.CfnEnvironment.OptionSettingProperty(
    namespace="aws:autoscaling:trigger",
    option_name='LowerThreshold',
    value='20'
)


def get_auto_scaling_trigger_options():
    return [
        trigger_measure_name,
        trigger_unit,
        trigger_upper_threshold,
        trigger_lower_threshold
    ]
